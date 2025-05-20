from typing import Self

import pynamodb.attributes as attr

from app.core.db import ModelBase

class User(ModelBase):    
    name: str = attr.UnicodeAttribute()
    email: str = attr.UnicodeAttribute()
    password_hash: str = attr.UnicodeAttribute()

    @classmethod
    def get(cls, id: str) -> Self | None:
        try:
            return super().get('USER', f'USER#{id}')
        except cls.DoesNotExist:
            return None
        
    @classmethod
    def get_by_email(cls, email: str) -> Self | None:
        results = super().query('USER', filter_condition=(cls.email == email))
        return next(results, None)