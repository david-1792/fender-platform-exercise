from datetime import datetime, timezone, timedelta

from fastapi.exceptions import HTTPException

import app.core.auth as auth
from app.core.config import settings
from app.api.users.models import User
from app.api.login.models import AccessToken
from app.api.login.schemas import TokenResponse

class LoginService:
    def __init__(
        self,
        current_user: User
    ) -> None:
        self.current_user = current_user

    @staticmethod
    def login(email: str, password: str) -> TokenResponse:
        if not (user := User.get_by_email(email)):
            raise HTTPException(
                status_code=401,
                detail='Invalid email or password'
            )
        
        if not auth.verify_password(password, user.password_hash):
            raise HTTPException(
                status_code=401,
                detail='Invalid email or password'
            )
        
        exp: datetime = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        token: str = auth.generate_access_token(user.id, exp)

        AccessToken(
            PK=f'USER#{user.id}',
            SK=f'TOKEN#{token}',
            _TYPE='TOKEN',
            id=token,
            expires_at=exp
        ).save()

        return TokenResponse(
            access_token=token
        )
    
    def logout(self) -> None:
        for token in AccessToken.query(self.current_user.id):
            token.delete()
        return None