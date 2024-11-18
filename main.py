import datetime
from fastapi import FastAPI, Query, HTTPException

from functions.live_score import live_score
from functions.get_live_score import get_live_score
from functions.get_match_details import get_match_details
from models.match import Match

app = FastAPI(title="Clever Scale - Football Livescore", version="1.0.0")




@app.get("/", tags=["Hello"])
async def index():
    return {"greeting": "Hello"}

@app.get("/matches", response_model=list[Match], tags=['Match'] )
async def matches(date: str = Query(None, description="Date in the format yyyy-mm-dd")):
    """
    Fetches match details for a given date.
    """
    if not date:
        date = datetime.datetime.now().isoformat()
        # raise HTTPException(status_code=400, detail="Please provide a date in the format yyyy-mm-dd")

    try:
        match_data = get_match_details(date)
        return match_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/live')
async  def get_live():
    # data = get_live_score()
    data = await live_score()
    return data
# To run the app, use: `uvicorn filename:app --reload`
