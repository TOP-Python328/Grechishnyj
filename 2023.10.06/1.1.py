class Tetrahedron:
    """Правильный тетраэдр"""
    
    def __init__(self, edge: float):
        self.edge = edge
        
    def surface(self) -> float:
        """Метод вычисляет и возвращает площадь поверхности"""
        return self.edge ** 2 * 3 ** 0.5
    
    def volume(self) -> float:
        """Метод вычисляет и возвращает объём тела"""
        return self.edge ** 3 / 12 * 2 ** 0.5
        
# >>> t1 = Tetrahedron(5)
# >>> t1.edge
# 5
# >>> t1.surface()
# 43.30127018922193
# >>> t1.volume()
# 14.73139127471974
# >>> t1.edge = 6
# >>> t1.surface()
# 62.35382907247958
# >>> t1.volume()
# 25.455844122715714