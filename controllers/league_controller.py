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
