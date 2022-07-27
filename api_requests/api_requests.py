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
        player_url = f"https://soccer.sportmonks.com/api/v2.0/players/{id}?api_token={self._api_token}"
        response = requests.request("GET", url=player_url)
        
        return response.text
        

    def request_player_by_name(self, name):
        name_player_url = f"https://soccer.sportmonks.com/api/v2.0/players/search/:{name}?api_token={self._api_token}"
        response = requests.request("GET", url=name_player_url)

        return response.text




# '''
# todas as ligas
# f"https://soccer.sportmonks.com/api/v2.0/leagues?api_token={api_token}"
# {"data":[{"id":271,"active":true,"type":"domestic","legacy_id":43,"country_id":320,"logo_path":"https:\/\/cdn.sportmonks.com\/images\/soccer\/leagues\/271.png","name":"Superliga","is_cup":false,"is_friendly":false,"current_season_id":19686,"current_round_id":273989,"current_stage_id":77457696,"live_standings":true,"coverage":{"predictions":true,"topscorer_goals":true,"topscorer_assists":true,"topscorer_cards":true}},{"id":501,"active":true,"type":"domestic","legacy_id":66,"country_id":1161,"logo_path":"https:\/\/cdn.sportmonks.com\/images\/soccer\/leagues\/501.png","name":"Premiership","is_cup":false,"is_friendly":false,"current_season_id":19735,"current_round_id":null,"current_stage_id":null,"live_standings":true,"coverage":{"predictions":true,"topscorer_goals":true,"topscorer_assists":true,"topscorer_cards":true}},{"id":513,"active":true,"type":"domestic","legacy_id":null,"country_id":1161,"logo_path":"https:\/\/cdn.sportmonks.com\/images\/soccer\/leagues\/1\/513.png","name":"Premiership Play-Offs","is_cup":false,"is_friendly":false,"current_season_id":19611,"current_round_id":null,"current_stage_id":null,"live_standings":false,"coverage":{"predictions":true,"topscorer_goals":true,"topscorer_assists":true,"topscorer_cards":true}},{"id":1659,"active":true,"type":"domestic","legacy_id":null,"country_id":320,"logo_path":"https:\/\/cdn.sportmonks.com\/images\/\/soccer\/leagues\/27\/1659.png","name":"Superliga Play-offs","is_cup":false,"is_friendly":false,"current_season_id":18101,"current_round_id":null,"current_stage_id":null,"live_standings":false,"coverage":{"predictions":true,"topscorer_goals":true,"topscorer_assists":true,"topscorer_cards":true}}],"meta":{"plans":[{"name":"Football Free Plan","features":"Standard","request_limit":"180,60","sport":"Soccer"}],"sports":[{"id":1,"name":"Soccer","current":true}],"pagination":{"total":4,"count":4,"per_page":100,"current_page":1,"total_pages":1,"links":{}}}}
# '''


'''
estatisticas do time

id_do_time = 3468
name_player_url = f"https://soccer.sportmonks.com/api/v2.0/teams/{id_do_time}?api_token={api_token}&include=stats"
'''