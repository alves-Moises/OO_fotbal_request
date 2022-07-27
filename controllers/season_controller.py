from api_requests import *
import json

import classes.season
from api_requests.api_requests import ApiRequests

api_requests = ApiRequests()

def search_season():
    season_list = list()
    season = json.loads(api_requests.request_season())    
    data = season['data']
    
    for season in data:
        season_list.append(classes.season.Season(season['id'],  season['name'], season['league_id'], season['is_current_season'], season['current_round_id'], season['current_stage_id']))
        
    return season_list