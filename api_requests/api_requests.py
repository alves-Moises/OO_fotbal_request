import requests

class ApiRequests():
    def __init__(self):
        
        self._api_token = "YwB4DudVPcTCwkdhblPTSh0ZrKipxrUFDruNbbN7dwua4Wv6kgWDRJZYsolY"

    def request_league(self):
        url = f"https://soccer.sportmonks.com/api/v2.0/leagues?api_token={self._api_token}"
        result = requests.request("GET", url = url)
        return result.text


    def request_season(self):
        url = f"https://soccer.sportmonks.com/api/v2.0/seasons?api_token={self._api_token}"
        result = requests.request("GET", url = url)

        return result.text


    def request_player_by_id(self, id):
        player_url = f"https://soccer.sportmonks.com/api/v2.0/players/{id}?api_token={self._api_token}"
        response = requests.request("GET", url=player_url)
        
        return response.text
        

    def request_player_by_name(self, name):
        name_player_url = f"https://soccer.sportmonks.com/api/v2.0/players/search/:{name}?api_token={self._api_token}"
        response = requests.request("GET", url=name_player_url)

        return response.text



