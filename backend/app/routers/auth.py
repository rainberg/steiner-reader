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
        "is_active": info.get("is_active", user.is_active),
    }
