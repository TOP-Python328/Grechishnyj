class Army(dict):
    """армия"""
    def __init__(self):
        super().__init__()
        
    def add(self, soldier):
        if not soldier.__class__.__name__ in self:
            self[soldier.__class__.__name__] = [soldier]
        else:
            self[soldier.__class__.__name__] += [soldier]

    
    @property
    def size(self):
        """Численность армии"""
        return sum(len(soldiers) for soldiers in self.values())
    
    
    @property
    def attack(self):
        """Сила атаки армии"""
        return sum(sum(soldier.power_attack for soldier in soldiers) for soldiers in self.values())

    
    @property
    def shield(self):
        """Уровень защиты армии"""
        return sum(sum(soldier.power_shield for soldier in soldiers) for soldiers in self.values())


    @property
    def power(self):
        """Общая мощь армии"""
        return self.attack + self.shield
        
        
    def __repr__(self):
        string = ''
        for key, values in self.items():
            string += f'{key}:\n'
            for unit in values:
                string += f'\t{unit}\n'
        return string