class Point:
    """Класс описывает точку с координатами по осям x, y"""
    
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y
        
    @property
    def x(self) -> float:
        return self.__x
        
    @x.setter
    def x(self, new_x) -> None:
        raise TypeError(f'{self.__class__.__name__} object does not support coordinate assignment')
        
    @property
    def y(self) -> float:
        return self.__y
        
    @y.setter
    def y(self, new_y) -> None:
        raise TypeError(f'{self.__class__.__name__} object does not support coordinate assignment')
        
    def __repr__(self):
        return f'{(self.x, self.y)}'
        
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            class_name = self.__class__.__name__
            raise ValueError(f'{class_name} the comparison can only be made with {class_name}')
        if self.x == other.x and self.y == other.y:
            return True
        return False

# >>> p = Point(1, 2)
# >>> p
# (1, 2)
# >>> print(p)
# (1, 2)
# >>> repr(p) == str(p)
# True
# >>> p.x, p.y
# (1, 2)
# >>> p.x, p.y = 1, 2
# Traceback (most recent call last):
# ...
# TypeError: Point object does not support coordinate assignment
#
# >>> p1 = Point(1, 2)
# >>> p2 = Point(1, 2)
# >>> p1 == p2
# True
# >>> p2 == p1
# True
# >>> p3 = Point(0, 0)
# >>> p2 == p3
# False
# >>> p1 != p3
# True
# >>> p1 != p2
# False


