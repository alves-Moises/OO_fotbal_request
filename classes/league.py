from unicodedata import name


class League():
    def __init__(self, id, name, active, _type, country_id):
        self.id = id
        self.name = name
        self.active = active
        self.type = _type
        self.country_id = country_id


    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def is_active(self):
        if self.active: return 'sim'
        return 'não'

    def get_type(self):
        return self.type

    def country_id(self):
        return self.country_id
   