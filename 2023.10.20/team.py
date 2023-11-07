from unit import Unit

class Team(dict):
    def __init__(self, name_team):
        super().__init__
        self.name: str = name_team
        self.heroes = []
        self['name'] = self.name
        self['heroes'] = self.heroes
    
    @property    
    def get_heroes(self) -> list['Hero']:
        return self.heroes
        
    @get_heroes.setter
    def set_heroes(self, hero) -> None:
        self.heroes.append(hero)
        
       

    
    def info(self):
        return f'{self.__class__.__name__} {self.name}'
        
        
