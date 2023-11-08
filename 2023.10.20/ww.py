"""
Классы солдаты и крестьяне (warrior & worker)
"""
from unit import Unit
from time import sleep

# Абстрактный класс для любого солдата с нулевыми значениями атаки и защиты
# Дочерние классы от него (например): Лучник, Пехотинец, Всадник
# Класс Hero так же наследуется от Warrior, чтобы Hero имел возможность сражаться

class Warrior(Unit):
    """Класс солдат"""
     
    def __init__(self):
        """Инициализация экземпляра

        :params power_attack: сила атаки (уменьшение здоровья противника)
        :params power_shield: уровень защиты (реализовано как добавление атаки)
        :params speed_attack: интервал частоты наносимых ударов (тайминг sleep)
        """
        super().__init__()
        self.name = self.__class__.__name__
        self.power_attack = 0
        self.power_shield = 0
        self.speed_attack = 10 - 0 # максимально 10
     

    # Атака противника, эксперементально...
    def attacked(self, other: 'Unit') -> None:
        """Атаковать противника"""
        if not self.is_friend(other):
            while other.health > 0:
                sleep(self.speed_attack)
                other.health -= self.power_attack + self.power_shield*0.1
                if self.health <= 0:
                    print(f'{self} погиб!')
                    # Unit die
                    break
                if other.health <= 0:
                    print(f'{other} погиб!')
                    # Unit die
                    break
                    


# Крестьяне приносят сырье:
# Лесорубы - деревоб, Шахтёры - железо и камень
# Класс Hero так же наследуется от Worker, чтобы Hero имел возможность приносить ресурсы
class Worker(Unit):
    """Класс крестьянин"""
    ...
    
    