class Player():
    def __init__(self, player_id, name, nationality, birthdate, image_path):
        self.id = player_id
        self.name = name
        self.nationality = nationality
        self.birthdate = birthdate
        self.image_path = image_path
        
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_nationality(self):
        return self.nacionality

    def get_birthdate(self):
        return self.birthdate
    
    def get_image(self):
        return self.image_path
    
    def get_age(self):
        return 2022 - self.birthdate

        