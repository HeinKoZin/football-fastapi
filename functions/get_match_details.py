import requests
from bs4 import BeautifulSoup

from models.match import Match


def get_match_details(date: str):
    url = f"https://www.besoccer.com/livescore/{date}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")

    match_details: list[Match] = []
    championships = soup.find("div", {'id': 'tableMatches'}).find_all("div", {'id': 'mod_panel'})

    for i in range(len(championships)):
        championship_title = championships[i].contents[1].find("span", {'class': 'va-m'}).text.strip()
        matches = championships[i].contents[1].find_all("a", {'class': 'match-link'})

        for match in matches:
            home_team = match.find("div", {'class': 'team_left'}).text.strip()
            away_team = match.find("div", {'class': 'team_right'}).text.strip()
            score = match.find("div", {'class': 'marker'}).text.strip()
            match_time =  match.find("p", {'class': 'match_hour'}).text.strip() if match.find("p", {'class': 'match_hour'}) is not None else None

            home_score, away_score = score.split("-") if match_time is None else [0, 0]

            match_detail = Match(
                home= home_team,
                away= away_team,
                score=  score if match_time is None else None,
                home_score= home_score if match_time is None else None,
                away_score= away_score if match_time is None else None,
                championship= championship_title,
                match= f"{home_team} {score} {away_team}",
                match_time= match_time
            )

            match_details.append(match_detail)


    return match_details
