"""
Классы солдаты и работники (warrior & worker)
"""
from unit import Unit
from time import sleep

class Warrior(Unit):
    """Класс солдаты"""
     
    def __init__(
            self, 
            default_power_attack: int = 5, 
            default_power_shield: int = 5,
            default_speed_attack: int = 5
        ):
        super().__init__()
        self.power_attack = default_power_attack
        self.power_shield = default_power_shield
        self.speed_attack = default_power_shield
     
    def join_hero(self, hero) -> None:
        """Присоединиться к Герою, вступить в его армию"""
        # try:
        self.team = hero.team
        hero.army.add(self)
    
    # Экспериментально...
    def attacked(self, other: Unit) -> None:
        """Атаковать противника"""
        if not self.is_friend(other):
            while other.health > 0:
                sleep(10 - default_speed_attack)
                other.health -= self.attack
                if self.health <= 0:
                    print(f'{self} погиб!')
                    # удалить Unit
                    break
                if other.health <= 0:
                    print(f'{other} погиб!')
                    # удалить Unit
                    break
                    
    def __repr__(self):
        return f'{self.name}: id={self.id}'
                    
                    
class Worker(Unit):
    """Класс работники"""
    ...
    
    def __repr__(self):
        return f'{self.name!r}'
   