class Point:
    """Класс описывает точку с координатами x, y"""
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
    """Класс описывает отрезок с координатами (x, y) для начальной и конечной точек"""
    def __init__(self, start: Point, end: Point):
        self.__start = start
        self.__end = end


    @staticmethod
    def __length_calc(point1: Point, point2: Point) -> float:
        """Возвращает длину отрезка"""
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


class Polygon(list):
    """Класс описывает многоугольник на координатной плоскости"""
    def __init__(self, side1: Line, side2: Line, side3: Line, *sides: tuple[Line, ...]):
        super().__init__((side1, side2, side3, *sides))
        # self.__perimetr = 0


    def _is_closed(self) -> bool:
        """Проверяет, формируют ли отрезки замкнутый многоугольник""" 
        if self[0].start != self[len(self) - 1].end:
            return False
        for i in range(len(self) - 1):
            if self[i].end != self[i+1].start:
                return False
        else:
            return True


    @property
    def perimeter(self):
        """Вычисляет и возвращает периметр многоугольника"""
        if self._is_closed():
            return sum(line.length for line in self)
        else:
            raise ValueError("line items doesn't from a closed plygon") 


    @perimeter.setter
    def perimeter(self, new_perimeter):
        """Возвращает исключение при попытке изменения свойства perimeter"""
        raise AttributeError(f"property 'perimeter' of '{self.__class__.__name__}' object has no setter") 


# >>> p1 = Point(0, 3)
# >>> p2 = Point(4, 0)
# >>> p3 = Point(8, 3)
# >>> p4 = Point(5, 5)
# 
# >>> p1, p2, p3, p4
# ((0, 3), (4, 0), (8, 3), (5, 5))
# 
# >>> p1.x, p1.y, p2.x, p2.y, p3.x, p3.y, p4.x, p4.y
# (0, 3, 4, 0, 8, 3, 5, 5)
# 
# >>> p1.x, p4.y = 4, 10
# ...
# TypeError: Point object does not support coordinate assignment
# 
# >>> p0 = Point(0, 3)
# >>> p1 == p0, p0 == p1, p1 != p0, p0 != p1
# (True, True, False, False)
# 
# >>> l1 = Line(p1, p2)
# >>> l2 = Line(p2, p3)
# >>> l3 = Line(p3, p1)
# >>> l4 = Line(p4, p2)
# 
# >>> l1
# (0, 3)---(4, 0)
# >>> l2
# (4, 0)---(8, 3)
# >>> l3
# (8, 3)---(0, 3)
# >>> l4
# (5, 5)---(4, 0)
# 
# >>> l1.length, l2.length, l3.length, l4.length
# (5.0, 5.0, 8.0, 5.0990195135927845)
# >>> l1.start, l1.end, l2.start, l2.end, l3.start, l3.end
# ((0, 3), (4, 0), (4, 0), (8, 3), (8, 3), (0, 3))
# 
# >>> l1.start = 15
# ...
# TypeError: 'start' attribute of 'Line'object supports only 'Point'object assignment
# 
# >>> polygon1 = Polygon(l1, l2, l3)
# >>> polygon2 = Polygon(l1, l2, l3, l4)
# >>> polygon1._is_closed()
# True
# >>> polygon2._is_closed()
# False
#
# >>> polygon1.perimeter
# 18.0
# >>> polygon2.perimeter
# ...
# ValueError: line items doesn't from a closed plygon
# >>> polygon1.perimeter = 20
# ...
# AttributeError: property 'perimeter' of 'Polygon' object has no setter