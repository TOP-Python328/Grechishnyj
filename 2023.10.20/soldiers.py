from ww import Warrior 

class Soldier(Warrior):
    """"""
    def __init__(self):
        super().__init__()
    
    # Воин вступает в армию к Hero и получает Team от Hero
    def join_hero(self, hero: 'Hero') -> None:
        """Присоединиться к Герою, вступить в его армию"""
        try:
            self.team = hero.team
            hero.army.add_soldier(self)
        except:
            print('Солдат не смог присоединиться к Герою')
            
            
# Примеры различных солдат 

class Infantry(Soldier):
    """Солдат пехотинец"""
    def __init__(self):
        super().__init__()
        self.power_attack = 15
        self.power_shield = 15
        self.speed_attack = 5
        
    
class Archer(Soldier):
    """Солдат лучник"""
    def __init__(self):
        super().__init__()
        self.power_attack = 5
        self.power_shield = 5
        self.speed_attack = 6


class Cavalry(Soldier):
    """Всадник-кавалерист"""
    def __init__(self):
        super().__init__()
        self.power_attack = 25
        self.power_shield = 25
        self.speed_attack = 7