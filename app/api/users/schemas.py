from typing import Annotated

from pydantic import BaseModel, EmailStr, Field
from pydantic.functional_serializers import PlainSerializer

from app.core.auth import get_password_hash

# Custom data types
Password = Annotated[
    str, 
    Field(min_length=8, max_length=128, serialization_alias='password_hash'),
    PlainSerializer(lambda v: get_password_hash(v), return_type=str)
]

# Base schema
class UserBase(BaseModel):
    name: str
    email: EmailStr

# Input schemas
class UserCreate(UserBase):
    password: Password

class UserUpdate(UserBase):
    name: str = None
    email: EmailStr = None
    password: Password = None

# Output schemas
class UserResponse(UserBase):
    id: str