import datetime
import json
import time
import requests


from models.live_score_match import LivescoreLeagueGroup, LivescoreMatch, LivescoreTeam


def live_score(date: str):

    url = f"https://prod-public-api.livescore.com/v1/api/app/date/soccer/{date}/6.30?MD=3&counryCode=MM"

    page = requests.get(url)

    data = page.json()

    stages = data['Stages']

    leagues: list[LivescoreLeagueGroup] = []

    for i in range(len(stages)):
        badge_url = None
        cs_nm = None
        comp_d = None
        if "badgeUrl" in stages[i]:
            badge_url = 'https://static.livescore.com/competition/high/' + stages[i]['badgeUrl']
        if "Csnm" in stages[i]:
            cs_nm = stages[i]['Csnm']
        if "CompD" in stages[i]:
            comp_d = stages[i]['CompD']

        events = stages[i]['Events']

        matches: list[LivescoreMatch] = []


        for y in range(len(events)):
            event = events[y]
            t1_news_tag = None
            t1_img = None
            t2_news_tag = None
            t2_img = None
            tr1 = None
            tr2 = None
            trp1 = None
            trp2 = None
            if "NewsTag" in event['T1'][0]:
                t1_news_tag = event['T1'][0]['NewsTag']
            if "Img" in event['T1'][0]:
                t1_img = 'https://lsm-static-prod.livescore.com/medium/' + event['T1'][0]['Img']
            if "NewsTag" in event['T2'][0]:
                t2_news_tag =  event['T2'][0]['NewsTag']
            if "Img" in event['T2'][0]:
                t2_img = 'https://lsm-static-prod.livescore.com/medium/' + event['T2'][0]['Img']
            if "Tr1" in event:
                tr1 = event['Tr1']
            if "Tr2" in event:
                tr2 = event['Tr2']
            if "Trp1" in event:
                trp1 = event['Trp1']
            if "Trp2" in event:
                trp2 = event['Trp2']


            matches.append(
                LivescoreMatch(
                    home_team=LivescoreTeam(name=event['T1'][0]['Nm'], img=t1_img, abr=event['T1'][0]['Abr'], news_tag=t1_news_tag),
                    away_team=LivescoreTeam(name=event['T2'][0]['Nm'], img=t2_img, abr=event['T2'][0]['Abr'], news_tag=t2_news_tag),
                    home_score=tr1,
                    home_pen_score=trp1,
                    away_score=tr2,
                    away_pen_score=trp2,
                    status=event['Eps']
                )
            )
        leagues.append(LivescoreLeagueGroup(league_name=cs_nm, group_name=stages[i]['Snm'], badge_url=badge_url, abr=comp_d, matches=matches))



    return  leagues

