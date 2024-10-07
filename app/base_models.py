from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    username: Optional[str] = None
    age: Optional[int] = None


class User2(BaseModel):
    name: Optional[str] = None
