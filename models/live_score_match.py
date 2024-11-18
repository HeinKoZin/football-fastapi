from typing import Optional

from pydantic import BaseModel

class LivescoreTeam(BaseModel):
    name: Optional[str] = None
    img: Optional[str] = None
    abr: Optional[str] = None
    news_tag: Optional[str] = None


class LivescoreMatch(BaseModel):
    home_team: LivescoreTeam
    away_team: LivescoreTeam
    home_score: Optional[int] = None
    home_pen_score: Optional[int] = None
    away_score: Optional[int] = None
    away_pen_score: Optional[int] = None
    status:  Optional[str] = None

class LivescoreLeagueGroup(BaseModel):
    league_name: Optional[str] = None
    group_name: Optional[str] = None
    badge_url: Optional[str] = None
    abr: Optional[str] = None
    matches: Optional[list[LivescoreMatch]] | None



