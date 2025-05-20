from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.api.deps import UserDep
from app.api.login.service import LoginService as svc
from app.api.login.schemas import TokenResponse

router = APIRouter(
    tags=['login']
)

@router.post(
    '/login',
    status_code=status.HTTP_200_OK,
    response_model=TokenResponse
)
def login(
    form: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> TokenResponse:
    return svc.login(form.username, form.password)

@router.post(
    '/logout',
    status_code=status.HTTP_204_NO_CONTENT
)
def logout(
    current_user: UserDep
) -> None:
    return svc(current_user).logout()