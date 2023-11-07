from typing import Self
from exc import AttributeChangeError


class Unit:
    """Игровая единица"""
    def __init__(self):
        self.__id: int = id(self) 
        self.team = None
        self.health: int = 100

    @property
    def id(self) -> int:
        """Возвращает id игровой единицы"""
        return self.__id
        
    @id.setter
    def id(self, new_id) -> None:
        """Исключение при попытке изменить id""" 
        raise AttributeChangeError('id')


    def is_friend(self, other: Self) -> bool:
        """Проверка - является ли второй юнит другом или нет"""
        if self.team is other.team:
            return True
        return False
        
        
    def die(self) -> None:
        """Выбытие юнита из игры"""
        
        
        
        
        
        
# >>> u1 = Unit()
# >>> u2 = Unit()
# >>> u3 = Unit()
# >>> u1.team, u2.team, u3.team
# ('nobody', 'nobody', 'nobody')

# >>> t1 = 1
# >>> t2 = 2
# >>> t3 = '3'

# >>> u1.team = t1
# >>> u2.team = t2
# >>> u3.team = t3

# >>> u1.is_enemy(u2)
# False
# >>> u1.is_enemy(u3)
# False

# >>> u2.team = 1
# >>> u1.is_enemy(u2)
# True

# >>> u1 = Unit()
# >>> u1.id
# 1409973357008
# >>> u1.id = 1
# ...
# AttributeChangeError: access to the attribute change 'id' is closed
