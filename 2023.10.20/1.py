from typing import Self

class AttributeChangeError(Exception):
    """Исключение при попытке изменить значение защищенного атрибута"""
    def __init__(self, attr_name):
        super().__init__(f'access to the attribute change {attr_name!r} is closed')



class Unit:
    """Класс описывает одну игровую единицу"""
    def __init__(self, team: str = 'nobody'):
        self.__id = id(self) 
        self.__team = team

    @property
    def id(self):
        return self.__id
        
    @id.setter
    def id(self, new_id):
        raise AttributeChangeError('id')
        
    @property
    def team(self):
        return self.__team
        
    @team.setter
    def team(self, new_team):
        self.__team = new_team
        return self

    
class Hero(Unit):
    """docstring"""
    def __init__(self):
        super().__init__()
        self.soldiers = list()
        self.level = len(self.soldiers)
        
    def upgrade_level(self):
        """docstring"""
        self.level += 5
        return self
        
    def follow_the_team(self, team):
        """docstring"""
        self.team = team.name

        
class Soldier(Unit):
    """docstring"""
    def __init__(self):
        super().__init__()
        
        
    def follow_the_hero(self, hero: Hero) -> None:
        """docstring"""
        hero.soldiers.append(self)
        
        
class Team(dict):
    def __init__(self, name, hero):
        super().__init__
        self.name = name
        self.hero = hero
        hero.team = self.name
        self.soldiers = self.hero.soldiers
        
        
        
        
        
        
# >>> unit = Unit()
# >>> unit_2 = Unit()
# >>> unit.__dict__
# {'id': 2520190317968}
# >>> unit_2.__dict__
# {'id': 2520190318480}

# >>> hero_1 = Hero()
# >>> hero_2 = Hero()
# >>> hero_1.__dict__
# {'id': 2520190318544}
# >>> hero_2.__dict__
# {'id': 2520190318928}

# >>> soldier_1 = Soldier()
# >>> soldier_2 = Soldier()
# >>> soldier_1.__dict__
# {'id': 2520190319312}
# >>> soldier_2.__dict__
# {'id': 2520190319440}

# >>> hero = Hero()
# >>> hero.id
# 1654938104976
# >>> hero.id = 0
# ...
# AttributeChangeError: access to the attribute change 'id' is closed
