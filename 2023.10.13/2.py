from numbers import Number
from collections.abc import Iterable
from typing import Self, Callable
from functools import cache
from operator import add, sub, neg, mul

class Matrix:
    """Класс моделирует неизменяемую матрицу"""
    
    def __init__(self, *args: Number, n: int, m: int):
        """Конструктор экземпляра класса.
        
        :param *args: элементы матрицы
        :param n: количество строк
        :param m: количество столбцов
        """

        if self.is_valid(*args, row=n, col=m):
            self.__flat: tuple[Number, ...] = args
            self.n = n
            self.m = m
            self.__transpose: Iterable[Number] = []
            for i in range(m):
                self.__transpose += list(args[i::m])
    
    
    @staticmethod
    def is_valid(*args: Number, row: int, col: int) -> bool:
        """Метод проверяет, является ли аргумент подходящим объектом для конструирования матрицы"""
        # ДОБАВИТЬ: перехват исключения ValueError: невозможно сконструировать матрицу
        if len(args) != row * col:
            return False
        for num in args:
            if not isinstance(num, Number):
                return False
        return True
     
    
    @property
    @cache
    def transpose(self: Self) -> Self: 
        """Метод возвращает транспонированную матрицу"""
        return self.__transpose
        
        
    def __element_wise_operation(self, operation: Callable, other: Self | Number) -> Self:
        """Выполняет переданную операцию со своим и переданным объектом"""
        if isinstance(other, Number):
            return self.__class__(*(operation(num, other) for num in self.__flat), n=self.n, m=self.m)
        elif isinstance(other, self.__class__):
            if self.n == other.n and self.m == other.m:
                return self.__class__(*(operation(self.__flat[i], other.__flat[i]) for i in range(len(self.__flat))), n=self.n, m=self.m)
            else:
                raise ValueError('сложение и вычитание возможно только для матриц одной размерности')
        else:
            raise ValueError('алгебраические операции возможны только с матрицами и часлами')
    
    
    def __add__(self, other) -> Self:
        return self.__element_wise_operation(add, other)


    def __radd__(self, other) -> Self:
        return self.__add__(other)


    def __sub__(self, other) -> Self:
        return self.__element_wise_operation(sub, other)

        
    def __rsub__(self, other) -> Self:
        return -self.__sub__(other)
        
        
    def __mul__(self, other) -> Self:
        if isinstance(other, Number):
            return self.__class__(*(i * other for i in self.__flat), n=self.n, m=self.m)
        elif isinstance(other, self.__class__):
            raise NotImplementedError('умножение матриц будет реализованно в будущем')

    
    def __rmul__(self, other) -> Self:
        return self.__mul__(other)


    def __neg__(self) -> Self:
        return self.__mul__(-1)









      
    def __repr__(self):
        # ИСПРАВИТЬ: используйте генераторное выражение в ещё одном join() — и не будет ни лишних пробелов, ни лишних eol
        #" ".join(f"{round(self[i][j], 1):>2}" for j in range(self.m)) + '\n'
        
        print(self.__flat, self.n, self.m, self.__transpose)
        return f'{self.__flat}'
        # representation = ''
        # for i in range(self.n):
            # representation += " ".join(f"{round(self[i][j], 1):>2}" for j in range(self.m)) + '\n'
        # return representation
        
    # def __repr__(self):
        # # ИСПРАВИТЬ: используйте генераторное выражение в ещё одном join() — и не будет ни лишних пробелов, ни лишних eol
        # representation = ''
        # for i in range(self.n):
            # representation += " ".join(f"{round(self[i][j], 1):>2}" for j in range(self.m)) + '\n'
        # return representation
