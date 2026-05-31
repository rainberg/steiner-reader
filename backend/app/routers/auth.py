"""Authentication router — delegates to Auth Service.

Registration, login, and token refresh are handled directly by the frontend
calling the auth-service. This router only provides:
- Current user info proxy (GET /me)
- Dependency injection helpers (get_current_user, require_user, require_admin)
"""

import logging
from typing import Optional

import httpx
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from app.config import settings
from app.db.database import get_db as _get_db

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/auth", tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login", auto_error=False)


class AuthUser(BaseModel):
    id: str
    display_name: str = ""
    email: Optional[str] = None
    phone: Optional[str] = None
    role: str = "user"
    credits: float = 0.0
    is_active: bool = True
    raw_token: str = ""


async def _verify_token(token: str) -> Optional[dict]:
    async with httpx.AsyncClient(timeout=10) as client:
        try:
            resp = await client.get(
                f"{settings.AUTH_SERVICE_URL}/api/auth/verify",
                headers={"Authorization": f"Bearer {token}"},
            )
            if resp.status_code == 200:
                return resp.json()
            return None
        except httpx.HTTPError as e:
            logger.error("Auth service verify failed: %s", e)
            return None


async def _fetch_user_info(token: str) -> Optional[dict]:
    async with httpx.AsyncClient(timeout=10) as client:
        try:
            resp = await client.get(
                f"{settings.AUTH_SERVICE_URL}/api/auth/me",
                headers={"Authorization": f"Bearer {token}"},
            )
            if resp.status_code == 200:
                return resp.json()
            return None
        except httpx.HTTPError as e:
            logger.error("Auth service /me failed: %s", e)
            return None


async def get_current_user(
    token: str = Depends(oauth2_scheme),
) -> Optional[AuthUser]:
    """Resolve current user from auth-service JWT. Returns None if unauthenticated."""
    if not token:
        return None

    identity = await _verify_token(token)
    if not identity:
        return None

    if not identity.get("is_active", True):
        return None

    if not identity.get("display_name"):
        info = await _fetch_user_info(token)
        if info:
            identity.update(info)

    return AuthUser(
        id=identity["user_id"] if "user_id" in identity else identity.get("id", ""),
        display_name=identity.get("display_name", ""),
        email=identity.get("email"),
        phone=identity.get("phone"),
        role=identity.get("role", "user"),
        credits=float(identity.get("credits", "0.00")),
        is_active=identity.get("is_active", True),
        raw_token=token,
    )


async def require_user(user: Optional[AuthUser] = Depends(get_current_user)) -> AuthUser:
    """Require authentication. Raises 401 if not logged in."""
    if not user:
        raise HTTPException(status_code=401, detail="请先登录")
    return user


async def require_admin(user: AuthUser = Depends(require_user)) -> AuthUser:
    """Require admin privileges. Raises 403 if not admin."""
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="需要管理员权限")
    return user


@router.get("/me")
async def get_me(user: AuthUser = Depends(require_user)):
    """Proxy: get current user full info from auth-service."""
    info = await _fetch_user_info(user.raw_token)
    if not info:
        raise HTTPException(status_code=401, detail="获取用户信息失败")

    return {
        "id": info.get("id", user.id),
        "display_name": info.get("display_name", ""),
        "email": info.get("email"),
        "phone": info.get("phone"),
        "role": info.get("role", user.role),
        "credits": float(info.get("credits", "0.00")),
        "credits_reserved": float(info.get("credits_reserved", "0.00")),
        "is_active": info.get("is_active", user.is_active),
    }


async def _proxy_auth_post(path: str, token: str, body: dict) -> dict:
    async with httpx.AsyncClient(timeout=15) as client:
        resp = await client.post(
            f"{settings.AUTH_SERVICE_URL}/api/auth{path}",
            headers={"Authorization": f"Bearer {token}"},
            json=body,
        )
        data = resp.json()
        if resp.status_code >= 400:
            raise HTTPException(status_code=resp.status_code, detail=data.get("detail", "操作失败"))
        return data


class BindPhoneBody(BaseModel):
    phone: str
    code: str
    password: Optional[str] = None


class BindEmailBody(BaseModel):
    email: str
    password: Optional[str] = None


class UnbindBody(BaseModel):
    password: Optional[str] = None


class DeleteAccountBody(BaseModel):
    password: Optional[str] = None


@router.post("/bind/phone")
async def bind_phone(body: BindPhoneBody, user: AuthUser = Depends(require_user)):
    return await _proxy_auth_post("/bind/phone", user.raw_token, body.model_dump(exclude_none=True))


@router.post("/bind/email")
async def bind_email(body: BindEmailBody, user: AuthUser = Depends(require_user)):
    return await _proxy_auth_post("/bind/email", user.raw_token, body.model_dump(exclude_none=True))


@router.post("/unbind/phone")
async def unbind_phone(body: UnbindBody, user: AuthUser = Depends(require_user)):
    return await _proxy_auth_post("/unbind/phone", user.raw_token, body.model_dump(exclude_none=True))


@router.post("/unbind/email")
async def unbind_email(body: UnbindBody, user: AuthUser = Depends(require_user)):
    return await _proxy_auth_post("/unbind/email", user.raw_token, body.model_dump(exclude_none=True))


@router.post("/delete-account")
async def delete_account(body: DeleteAccountBody, user: AuthUser = Depends(require_user), db=Depends(_get_db)):
    result = await _proxy_auth_post("/delete-account", user.raw_token, body.model_dump(exclude_none=True))

    from app.db.models import Contribution, LectureAccess, UserTranslationJob
    from sqlalchemy import delete as sql_delete

    await db.execute(sql_delete(Contribution).where(Contribution.user_id == user.id))
    await db.execute(sql_delete(LectureAccess).where(LectureAccess.user_id == user.id))
    await db.execute(sql_delete(UserTranslationJob).where(UserTranslationJob.user_id == user.id))
    await db.commit()

    return result
