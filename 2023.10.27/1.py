class Point:
    """Класс описывает точку с координатами по осям x, y"""
    
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y
    
    
    @property
    def x(self) -> float:
        """Возвращает защищенный атрибут x"""
        return self.__x


    @x.setter
    def x(self, new_x) -> None:
        """Возвращает исключение при попытке изменения значения защищенного атрибута x"""
        raise TypeError(f'{self.__class__.__name__} object does not support coordinate assignment')


    @property
    def y(self) -> float:
        """Возвращает защищенный атрибут y"""
        return self.__y


    @y.setter
    def y(self, new_y) -> None:
        """Возвращает исключение при попытке изменения значения защищенного атрибута y"""
        raise TypeError(f'{self.__class__.__name__} object does not support coordinate assignment')


    def __repr__(self):
        return f'{(self.x, self.y)}'


    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.x == other.x and self.y == other.y


class Line:
    """Класс описывает линию с координатами (x, y) для начальной и конечной точек"""
    
    def __init__(self, start: Point, end: Point):
        self.__start = start
        self.__end = end


    @staticmethod
    def __length_calc(point1: Point, point2: Point) -> float:
        """Возвращает расстояние между двумя точками линиии"""
        return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5

    
    @property
    def start(self) -> Point:
        """Возвращает защищенный атрибут start"""
        return (self.__start.x, self.__start.y)


    @start.setter
    def start(self, new_start: Point) -> None:
        """Устанавливает новое значение защищенного атрибута start"""
        if not isinstance(new_start, Point):
            raise TypeError(
                f"'start' attribute of '{self.__class__.__name__}'"
                f"object supports only '{self.__start.__class__.__name__}'"
                f"object assignment"
            )
        self.__start = new_start


    @property
    def end(self) -> Point:
        """Возвращает защищенный атрибут end"""
        return (self.__end.x, self.__end.y)


    @end.setter
    def end(self, new_end: Point) -> None:
        """Устанавливает новое значение защищенного атрибута end"""
        if not isinstance(new_end, Point):
            raise TypeError(
                f"'end' attribute of '{self.__class__.__name__}'"
                f"object supports only '{self.__start.__class__.__name__}'"
                f"object assignment"
            )
        self.__end = new_end

    
    @property
    def length(self) -> float:
        """Вычисляет и возвращает значение защищенного атрибута length"""
        return self.__length_calc(self.start, self.end) 


    @length.setter
    def length(self, new_length) -> None:
        """Возвращает исключение при попытке изменения значения защищенного атрибута length"""
        raise TypeError(f'{self.__class__.__name__} object does not support length assignment')


    def __repr__(self):
        return(f'{self.start}---{self.end}')


class Polygon:
    pass
    

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
# >>> p1 == (1, 2)
# False

# >>> p1 = Point(1,1)
# >>> p2 = Point(2,2)
# >>> l1 = Line(p1, p2)
# >>> l1.start
# (1, 1)
# >>> l1.end
# (2, 2)
# >>> l1.length
# 1.4142135623730951
# >>> l1.start = Point(3,3)
# >>> l1.end = Point(10,10)
# >>> l1.length
# 9.899494936611665
# >>> l1
# (3, 3)---(10, 10)
# >>> l1.length = 100
# ...
# TypeError: Line object does not support length assignment
# >>> l1.start = 12
# ...
# TypeError: 'start' attribute of 'Line' object supports only 'Point' object assignment
# >>> l1.end = 12
# ...
# TypeError: 'end' attribute of 'Line' object supports only 'Point' object assignment
# >>> repr(l1) == str(l1)
# True


