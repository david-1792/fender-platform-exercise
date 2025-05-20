import uuid

from fastapi.exceptions import HTTPException

import app.core.auth as auth
from app.api.login.models import AccessToken
from app.api.users.models import User
from app.api.users.schemas import (
    UserCreate,
    UserUpdate,
    UserResponse
)

class UserService:
    def __init__(
        self,
        current_user: User
    ) -> None:
        self.current_user = current_user

    @staticmethod
    def register(user: UserCreate) -> None:
        if User.get_by_email(user.email):
            raise HTTPException(
                status_code=400,
                detail='Email already exists'
            )
        
        user_id = str(uuid.uuid4())
        model = User(
            PK='USER',
            SK=f'USER#{user_id}',
            _TYPE='USER',
            id=user_id,
            name=user.name,
            email=user.email,
            password_hash=auth.get_password_hash(user.password)
        )

        model.save()

    def me(self) -> UserResponse:
        return UserResponse.model_validate(self.current_user.to_simple_dict())
    
    def update_me(self, user: UserUpdate) -> UserResponse:
        if user.email and user.email != self.current_user.email and User.get_by_email(user.email):
            raise HTTPException(
                status_code=400,
                detail='Email already exists'
            )
        
        # Update the model attributes
        for k, v in user.model_dump(exclude_unset=True, by_alias=True).items():
            setattr(self.current_user, k, v)

        self.current_user.save()
        return UserResponse.model_validate(self.current_user.to_simple_dict())
    
    def delete_me(self) -> None:
        self.current_user.delete()
        for token in AccessToken.query(self.current_user.id):
            token.delete()
        return None

