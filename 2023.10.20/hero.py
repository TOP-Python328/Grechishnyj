from unit import Unit
from team import Team
from army import Army
from ww import Warrior, Worker

class Hero(Warrior, Worker):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.army = Army()
        self.power_attack = 50
        self.power_shield = 50
        self.speed_attack = 8
        # self.battle_distance = 1
        # self.travel_speed = 1
        
    
    def create_team(self, name_team) -> Team:
        """Возможность Героя создать свою команду"""
        new_team = Team(name_team)
        self.join_team(new_team)
        
        return new_team
        
    def join_team(self, team: Team) -> None:
        """Возможность Героя вступить в команду вместе с армией"""
        self.team = team
        for units in self.army.values():
            for unit in units:
                unit.team = self.team
        team.heroes.append(self)
        
    def __repr__(self):
        return f'{self.name!r}'
        
        
        
        
        
# >>> h1 = Hero('Илья Муромец')
# >>> h2 = Hero('Змей Горыныч')
# >>> t1 = Team('Богатыри')
# >>> t2 = Team('Нечисть')
# >>> h1.join_team(t1)
# >>> h2.join_team(t2)
# >>> h1.is_friend(h2)
# False

# >>> h1 = Hero('Илья Муромец')
# >>> w = Warrior()
# >>> h1.__dict__
# {'_Unit__id': 2048577944336, 'team': None, 'health': 100, 'attack': 5, 'shield': 5, 'name': 'Илья Муромец', 'army': {}}
# >>> w.__dict__
# {'_Unit__id': 2048577944208, 'team': None, 'health': 100, 'attack': 5, 'shield': 5}

# >>> t1 = Team('t1')
# >>> w.join_hero(h1)
# >>> w.__dict__
# {'_Unit__id': 2048577944208, 'team': None, 'health': 100, 'attack': 5, 'shield': 5}
# >>> h1.join_team(t1)
# >>> h1.team
# {'name': 't1', 'heroes': [Илья Муромец - class Hero]}
# >>> w.__dict__
# {'_Unit__id': 2048577944208, 'team': {'name': 't1', 'heroes': [Илья Муромец - class Hero]}, 'health': 100, 'attack': 5, 'shield': 5}

# >>> h1.army
# {'Warrior': [<ww.Warrior object at 0x000001DCF8C2BA90>]}

