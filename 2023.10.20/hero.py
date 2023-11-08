from unit import Unit
from team import Team
from army import Army
from ww import Warrior, Worker

class Hero(Warrior, Worker):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.level = 0
        self.army = Army()
        self.power_attack = 50
        self.power_shield = 50
        self.speed_attack = 8
        
    # Герой создает свою команду и вступает в неё с армией
    def create_team(self, name_team) -> Team:
        """Возможность Героя создать свою команду"""
        self.quit_team()
        new_team = Team(name_team)
        self.join_team(new_team)
        
        return new_team
    
    # Герой присоединяется к существующей команде
    def join_team(self, team: Team) -> None:
        """Возможность Героя вступить в команду вместе с армией"""
        self.quit_team()
        self.team = team
        for units in self.army.values():
            for unit in units:
                unit.team = self.team
        team.heroes.append(self)
     
    # Герой покидает команду в которой он находится     
    def quit_team(self) -> None:
        """Выход из команды"""
        if self.team:
            team = self.team
            self.team = None
            team.heroes.remove(self)
            for units in self.army.values():
                for unit in units:
                    unit.team = self.team
                    
    # Повышение уровня Героя
    def update_level(self, add_num: int) -> None:
        self.level += add_num
        

 
