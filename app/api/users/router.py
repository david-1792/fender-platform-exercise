from typing import Annotated

from fastapi import APIRouter, Body, status

from app.api.deps import UserDep
from app.api.users.service import UserService as svc
from app.api.users.schemas import (
    UserCreate,
    UserUpdate,
    UserResponse
)

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.post(
    '/register',
    status_code=status.HTTP_204_NO_CONTENT
)
def register(
    user: Annotated[UserCreate, Body(...)]
) -> None:
    return svc.register(user)

@router.get(
    '/me',
    status_code=status.HTTP_200_OK,
    response_model=UserResponse
)
def me(
    current_user: UserDep
) -> UserResponse:
    return svc(current_user).me()

@router.patch(
    '/me',
    status_code=status.HTTP_200_OK,
    response_model=UserResponse
)
def update_me(
    current_user: UserDep,
    user: Annotated[UserUpdate, Body(...)]
) -> UserResponse:
    return svc(current_user).update_me(user)

@router.delete(
    '/me',
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_me(
    current_user: UserDep
) -> None:
    return svc(current_user).delete_me()