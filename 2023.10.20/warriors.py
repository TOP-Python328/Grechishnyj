from ww import Warrior

class Infantry(Warrior):
    """Солдат пехотинец"""
    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__
        self.power_attack = 15
        self.power_shield = 15
        # self.battle_distance = 5
        # self.travel_speed = 10
    
    
    
class Archer(Warrior):
    """Солдат лучник"""
    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__
        self.power_attack = 5
        self.power_shield = 5
        self.speed_attack = 6
        # self.battle_distance = 20
        # self.travel_speed = 15
        

        
class Cavalry(Warrior):
    """Всадник-кавалерист"""
    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__
        self.power_attack = 25
        self.power_shield = 25
        self.speed_attack = 7
        # self.battle_distance = 10
        # self.travel_speed = 25