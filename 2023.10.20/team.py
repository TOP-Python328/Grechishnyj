"""
Класс команда - Team"""

class Team(dict):
    def __init__(self, name_team):
        super().__init__
        self.name: str = name_team
        self.heroes = []
        self['name'] = self.name
        self['heroes'] = self.heroes


    def add(self, hero: 'Hero') -> None:
        """Добавить в список Героя"""
        self.heroes.append(hero)

    
    def info(self) -> str:
        """Возвращает информацию о команде"""
        return f'{self.__class__.__name__} {self.name}'
 
