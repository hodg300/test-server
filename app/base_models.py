from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    username: Optional[str] = None
    age: Optional[int] = None


class User2(BaseModel):
    name: Optional[str] = None


class Player(BaseModel):
    name: str
    level: float
    position: str
    goalkeeperNumber: Optional[int] = 1
    isFake: Optional[bool] = False


class HistoryShuffle(BaseModel):
    date: datetime
    teams: str
    firstMatchText: str



