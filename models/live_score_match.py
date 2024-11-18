from pydantic import BaseModel

class LivescoreTeam(BaseModel):
    name: str
    img: str | None
    abr: str
    news_tag: str | None


class LivescoreMatch(BaseModel):
    home_team: LivescoreTeam
    away_team: LivescoreTeam
    home_score: int | None
    away_score: int | None
    status: str

class LivescoreLeagueGroup(BaseModel):
    league_name: str | None
    group_name: str
    badge_url: str | None
    abr: str | None
    matches: list[LivescoreMatch] | None



