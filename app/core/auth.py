from datetime import datetime, timezone, timedelta

import jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(
    schemes=['bcrypt'], 
    deprecated='auto'
)

def generate_access_token(sub: str, exp: datetime = None) -> str:
    if not exp:
        exp = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        
    return jwt.encode(
        {'sub': sub, 'type': 'access', 'exp': exp.timestamp()},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)