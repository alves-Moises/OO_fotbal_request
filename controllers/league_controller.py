from api_requests import *

import json
from api_requests.api_requests import ApiRequests
import classes.league

api_requests = ApiRequests()


def request_league():
    league_list = list()

    league_data = json.loads(api_requests.request_league())
    league = league_data['data'] 

    for item in league:
        league_list.append(classes.league.League(item['id'], item['name'], item['active'], item['type'], item['country_id']))

    return league_list

def request_league_by_name(name):
    league_list = request_league()

    new_list = list()
    
    for league in league_list:
        if name in league.get_name(): new_list.append(league)

    return new_list
