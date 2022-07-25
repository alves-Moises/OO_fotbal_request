from pkgutil import get_data
from api_requests.api_requests import *
import json
import classes.player
api_requests = ApiRequests()

def search_player(name):

    player_list = list() #list of player's objects

    #getting json requested from api
    player_data = json.loads(api_requests.request_player_by_name(name))
    player_data = player_data['data']

    #players objects
    for player in player_data:
        player_list.append(classes.player.Player(player['player_id'], player['common_name'], player['nationality'], player['birthdate'], player['image_path']))

    return player_list
    # print(get_data(player_data))
   