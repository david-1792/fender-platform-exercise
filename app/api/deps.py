from typing import Annotated

from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer

import jwt

from app.core.config import settings
from app.api.users.models import User
from app.api.login.models import AccessToken

oauth_2_scheme = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_PREFIX}/login'
)

TokenDep = Annotated[str, Depends(oauth_2_scheme)]

def get_current_user(token: TokenDep) -> User:
    try:
        claims = jwt.decode(
            jwt=token,
            key=settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        if not (user := User.get(claims['sub'])):
            raise HTTPException(
                status_code=401,
                detail='Invalid token'
            )
        
        if not AccessToken.get(user.id, token):
            raise HTTPException(
                status_code=401,
                detail='Invalid token'
            )
        
        return user

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail='Invalid token'
        )
    
UserDep = Annotated[User, Depends(get_current_user)]