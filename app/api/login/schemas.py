from pydantic import BaseModel

# Output schemas
class TokenResponse(BaseModel):
    access_token: str