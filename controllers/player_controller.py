from api_requests.api_requests import *

import json
import classes.player

api_requests = ApiRequests()

def search_player_by_name(name):

    player_list = list() #list of player's objects

    #getting json requested from api
    player_data = json.loads(api_requests.request_player_by_name(name))
    player_data = player_data['data']

    #players objects
    for player in player_data:
        if name in player['fullname']:
            player_list.append(classes.player.Player(player['player_id'], player['fullname'], player['nationality'], player['birthdate'], player['image_path']))

    
    if player_list == []: return False
    return player_list
   

def search_player_by_id(id):

    player_data = json.loads(api_requests.request_player_by_id(id))
    try:
        new_data = player_data['data']
        
        player = classes.player.Player(new_data['player_id'], new_data['fullname'], new_data['nationality'], new_data['birthdate'], new_data['image_path'])
        
    except:
        return False

    return player
    # print(new_data)
    # print("Deu certo.")