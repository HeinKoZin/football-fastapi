from typing import Optional

from pydantic import BaseModel

class Match(BaseModel):
    home: Optional[str] = ''
    away: Optional[str] = ''
    score: Optional[str] = None
    home_score: Optional[int] = None
    away_score: Optional[int]  = None
    championship: Optional[str] = ''
    match: Optional[str] = ''
    minutes: Optional[str] = None
    match_time: Optional[str] = None

