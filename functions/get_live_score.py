import requests
from bs4 import BeautifulSoup

from models.match import Match


def get_live_score():
    url = f"https://www.besoccer.com/livescore/2024-11-17/live"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")

    match_details = []
    championships = soup.find("div", {'id': 'tableMatches'}).find_all("div", {'id': 'mod_panel'})

    for i in range(len(championships)):
        championship_title = championships[i].contents[1].find("span", {'class': 'va-m'}).text.strip()
        matches = championships[i].contents[1].find_all("a", {'class': 'match-link'})

        for match in matches:
            home_team = match.find("div", {'class': 'team_left'}).text.strip()
            away_team = match.find("div", {'class': 'team_right'}).text.strip()
            score = match.find("div", {'class': 'marker'}).text.strip()
            minutes = match.find("b").text.strip()
            match_detail = Match(
                home= home_team,
                away= away_team,
                score= score,
                home_score= score[0],
                away_score= score[-1],
                championship= championship_title,
                match= f"{home_team} {score} {away_team}",
                minutes=minutes
            )
            match_details.append(match_detail)
        if i == 5:  # Limit the number of championships processed to 5
            break



    return match_details

