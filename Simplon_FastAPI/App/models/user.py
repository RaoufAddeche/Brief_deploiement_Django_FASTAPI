from typing import Optional
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, max_length=255)
    hashed_password: str = Field(max_length=255)
    is_active: bool = Field(default=False)
    is_admin: bool = Field(default=False)