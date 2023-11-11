from typing import Self

class AttributeChangeError(Exception):
    """Исключение при попытке изменить значение защищенного атрибута"""
    def __init__(self, attr_name: str):
        super().__init__(f'access to the attribute change {attr_name!r} is closed')


# Абстрактный класс для создания условной игровой единицы
# от которого наследуются дочерние классы делящиеся по функционалу
# Солдаты(абстрактный) и Крестьяне(абстрактный)
class Unit:
    """Игровая единица"""

    
    def __init__(self):
        """Инициализация экземпляра

        :params __id: идентификатор экземпляра игровой единицы
        :params team: принадлежность к команде (по умолчанию None)
        :params health: начальный уровень здоровья
        """
        self.__id: int = id(self) 
        self.__team: 'Team' = None
        self.health: int = 100

    # Геттер - для доступа к защищенному атрибуту __id
    @property
    def id(self) -> int:
        """Возвращает id игровой единицы"""
        return self.__id
    
    # Сеттер - выброс собственного исключения при попутке изменить __id
    @id.setter
    def id(self, new_id: int) -> None:
        """Исключение при попытке изменить id""" 
        raise AttributeChangeError('id')

    # Геттер - для доступа к защищенному атрибуту __team
    @property
    def team(self):
        return self.__team

    # Сеттер - для изменения атрибута __team
    @team.setter
    def team(self, new_team) -> None:
        self.__team = new_team 

    # Проверка на дружбу с юнитом
    def is_friend(self, other: Self) -> bool:
        """Проверка - является ли второй юнит другом(врагом) или нет"""
        return self.team is other.team
   
    # Выбытие смерть юнита при значении атрибута health=0 
    # Не реализовано...
    def die(self) -> None:
        """Выбытие юнита из игры"""
   
    def __repr__(self):
        return f'{self.name} id={self.id}'