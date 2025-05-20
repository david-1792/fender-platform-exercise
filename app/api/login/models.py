from typing import Self, Iterator

import pynamodb.attributes as attr

from app.core.db import ModelBase

class AccessToken(ModelBase):
    expires_at: int = attr.TTLAttribute()

    @classmethod
    def get(cls, user_id: str, token: str) -> Self | None:
        try:
            return super().get(f'USER#{user_id}', f'TOKEN#{token}')
        except cls.DoesNotExist:
            return None
        
    @classmethod
    def query(cls, user_id: str) -> Iterator[Self]:
        return super().query(f'USER#{user_id}', filter_condition=(cls._TYPE == 'TOKEN'))