# Класс Армия список всех солдат Героя 

class Army(dict):
    """Армия"""
    def __init__(self):
        super().__init__()
        
    # Дабавляет в словарь солдата (ключ - тип Воина, здачение экземпляр класс Воин)
    def add_soldier(self, soldier: [str, 'Warrior']) -> None:
        """Добавить солдата"""
        if not soldier.__class__.__name__ in self:
            self[soldier.__class__.__name__] = [soldier]
        else:
            self[soldier.__class__.__name__] += [soldier]

    # Численность армии - количество всех солдат в армии
    @property
    def size(self) -> int:
        """Численность армии"""
        return sum(len(soldiers) for soldiers in self.values())
    
    
    @property
    def attack(self) -> float:
        """Сила атаки армии"""
        return sum(sum(soldier.power_attack for soldier in soldiers) for soldiers in self.values())

    
    @property
    def shield(self) -> float:
        """Уровень защиты армии"""
        return sum(sum(soldier.power_shield for soldier in soldiers) for soldiers in self.values())


    @property
    def power(self) -> float:
        """Общая мощь армии"""
        return self.attack + self.shield
        
        
