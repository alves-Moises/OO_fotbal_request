import requests

class ApiRequests():
    def __init__(self):
        
        self._api_token = "YwB4DudVPcTCwkdhblPTSh0ZrKipxrUFDruNbbN7dwua4Wv6kgWDRJZYsolY"

    def request_league(self, league):
        pass

    def request_country(self, country):
        pass

    def request_team_by_country(self, country):   
        pass

    def request_player_by_id(self, id):
        pass

    def request_player_by_name(self, name):
        nome_do_jogador = name
        name_player_url = f"https://soccer.sportmonks.com/api/v2.0/players/search/:{nome_do_jogador}?api_token={self._api_token}"
        response = requests.request("GET", url=name_player_url)  # , headers=headers)

        # print("x" * 30 , response.text , "x" * 30)
        return response.text
