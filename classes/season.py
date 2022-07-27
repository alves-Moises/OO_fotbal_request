class Season():
    def __init__(self, season_id,  name, league_id, is_corrent_season, current_round_id, current_stage):
        self.id = season_id
        self.name = name
        self.league_id = league_id
        self.is_current_season = is_corrent_season
        self.current_round_id = current_round_id
        self.current_stage = current_stage

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
    
    def get_league_id(self):
        return self.league_id

    def is_current_season(self):
        if self.is_current_season: return "sim"
        
        return "não"

    def get_current_round_id(self):
        if not self.current_round_id: return ''
        return self.current_round_id

    def get_current_stage(self):
        if not self.get_current_stage: return ''
        return self.current_stage

    


