"""Authentication router — register, login, user info."""

from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.models import User
from app.config import settings

router = APIRouter(prefix="/api/auth", tags=["auth"])

# Security config
SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login", auto_error=False)


# --- Schemas ---

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: dict

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    credits: int
    is_admin: int
    created_at: datetime

# --- Helpers ---

def create_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
) -> User | None:
    """Get current user from JWT token. Returns None if not authenticated."""
    if not token:
        return None
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id_str = payload.get("sub"); user_id = int(user_id_str) if user_id_str else None
        if user_id is None:
            return None
    except JWTError:
        return None
    
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()


async def require_user(user: User | None = Depends(get_current_user)) -> User:
    """Require authentication. Raises 401 if not logged in."""
    if not user:
        raise HTTPException(status_code=401, detail="请先登录")
    return user


async def require_admin(user: User = Depends(require_user)) -> User:
    """Require admin privileges. Raises 403 if not admin."""
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="需要管理员权限")
    return user


# --- Endpoints ---

@router.post("/register", response_model=TokenResponse)
async def register(req: RegisterRequest, db: AsyncSession = Depends(get_db)):
    """Register a new user."""
    # Validate
    if len(req.username) < 2 or len(req.username) > 50:
        raise HTTPException(400, "用户名需要2-50个字符")
    if len(req.password) < 6:
        raise HTTPException(400, "密码至少6个字符")
    if "@" not in req.email:
        raise HTTPException(400, "请输入有效邮箱")
    
    # Check duplicates
    existing = await db.execute(
        select(User).where((User.username == req.username) | (User.email == req.email))
    )
    if existing.scalar_one_or_none():
        raise HTTPException(400, "用户名或邮箱已存在")
    
    # Create user
    user = User(
        username=req.username,
        email=req.email,
        password_hash=pwd_context.hash(req.password),
        credits=100,  # New user bonus
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    
    token = create_token({"sub": str(user.id)})
    return TokenResponse(
        access_token=token,
        user={"id": user.id, "username": user.username, "email": user.email, "credits": user.credits, "is_admin": user.is_admin},
    )


@router.post("/login", response_model=TokenResponse)
async def login(req: LoginRequest, db: AsyncSession = Depends(get_db)):
    """Login with email and password."""
    result = await db.execute(select(User).where(User.email == req.email))
    user = result.scalar_one_or_none()

    if not user or not pwd_context.verify(req.password, user.password_hash):
        raise HTTPException(401, "邮箱或密码错误")

    token = create_token({"sub": str(user.id)})
    return TokenResponse(
        access_token=token,
        user={"id": user.id, "username": user.username, "email": user.email, "credits": user.credits, "is_admin": user.is_admin},
    )


@router.get("/me", response_model=UserResponse)
async def get_me(user: User = Depends(require_user)):
    """Get current user info."""
    return user


# --- User Self-Service Endpoints ---

class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str

class ChangeEmailRequest(BaseModel):
    email: str
    password: str

class ChangeUsernameRequest(BaseModel):
    username: str
    password: str


@router.put("/change-password")
async def change_password(
    req: ChangePasswordRequest,
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """修改当前用户密码"""
    if not pwd_context.verify(req.old_password, user.password_hash):
        raise HTTPException(400, "原密码错误")
    if len(req.new_password) < 6:
        raise HTTPException(400, "新密码至少6个字符")
    if req.old_password == req.new_password:
        raise HTTPException(400, "新密码不能与原密码相同")

    user.password_hash = pwd_context.hash(req.new_password)
    await db.commit()

    return {"success": True, "message": "密码修改成功"}


@router.put("/change-email")
async def change_email(
    req: ChangeEmailRequest,
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """修改当前用户邮箱"""
    if not pwd_context.verify(req.password, user.password_hash):
        raise HTTPException(400, "密码错误")

    if "@" not in req.email:
        raise HTTPException(400, "请输入有效邮箱")

    # Check if email is already taken by another user
    existing = await db.execute(
        select(User).where(User.email == req.email, User.id != user.id)
    )
    if existing.scalar_one_or_none():
        raise HTTPException(400, "该邮箱已被其他用户使用")

    user.email = req.email
    await db.commit()
    await db.refresh(user)

    return {
        "success": True,
        "message": "邮箱修改成功",
        "email": user.email,
    }


@router.put("/change-username")
async def change_username(
    req: ChangeUsernameRequest,
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """修改当前用户名（每3个月可改一次）"""
    from datetime import timedelta
    if not pwd_context.verify(req.password, user.password_hash):
        raise HTTPException(400, "密码错误")
    if len(req.username) < 2 or len(req.username) > 50:
        raise HTTPException(400, "用户名需要2-50个字符")
    if req.username == user.username:
        raise HTTPException(400, "新用户名不能与当前用户名相同")

    # 3-month restriction
    if user.username_changed_at:
        next_allowed = user.username_changed_at + timedelta(days=90)
        if datetime.utcnow() < next_allowed:
            days_left = (next_allowed - datetime.utcnow()).days
            raise HTTPException(400, f"每90天只能修改一次用户名，还需等待 {days_left} 天")

    # Check if username is already taken by another user
    existing = await db.execute(
        select(User).where(User.username == req.username, User.id != user.id)
    )
    if existing.scalar_one_or_none():
        raise HTTPException(400, "该用户名已被其他用户使用")

    user.username = req.username
    user.username_changed_at = datetime.utcnow()
    await db.commit()
    await db.refresh(user)

    return {
        "success": True,
        "message": "用户名修改成功",
        "username": user.username,
    }
