from pynamodb.models import Model
import pynamodb.attributes as attr

from app.core.config import settings

class ModelBase(Model):
    class Meta:
        region=settings.AWS_REGION
        host = settings.AWS_DDB_ENDPOINT
        table_name = settings.AWS_DDB_TABLE_NAME

    PK: str = attr.UnicodeAttribute(hash_key=True)
    SK: str = attr.UnicodeAttribute(range_key=True)
    _TYPE: str = attr.UnicodeAttribute()
    id: str = attr.UnicodeAttribute()