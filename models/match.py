from pydantic import BaseModel

class Match(BaseModel):
    home: str
    away: str
    score: str
    home_score: int
    away_score: int
    championship: str
    match: str
    minutes: str | None
