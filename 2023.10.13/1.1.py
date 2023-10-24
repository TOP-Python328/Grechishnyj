from numbers import Number
from collections.abc import Iterable
from typing import Self, Callable
from operator import add, sub, mul

RawRow = Iterable[Number]
RawMatrix = Iterable[RawRow]

class Matrix:
    """Класс моделирует изменяемую матрицу"""
    

    def __init__(self, raw_matrix: RawMatrix):
        """Конструктор экземпляра класса.
        
        :attr raw_matrix: строки матрицы
        :attr n: количество строк
        :attr m: количество столбцов
        """
        if self.is_valid(raw_matrix):
            self.__rows = raw_matrix
            self.n = len(raw_matrix)
            self.m = len(raw_matrix[0])
        else:
            raise ValueError('невозможно сконструировать матрицу')
    

    @property
    def transpose(self: Self) -> Self:
        """Метод возвращает транспонированную матрицу"""
        self.__rows = [[self.__rows[j][i] for j in range(self.n)] for i in range(self.m)]
        self.n, self.m = self.m, self.n
        return self.__rows


    @staticmethod
    def is_valid(raw_matrix: RawMatrix) -> bool:
        """Метод проверяет, является ли аргумент подходящим объектом для конструирования матрицы"""
        if len(set(map(len, raw_matrix))) != 1:
            return False   
        for row in raw_matrix:
            if not iter(row):
                return False
            for num in row:
                if not isinstance(num, Number):
                    return False            
        return True

    
    @property
    def __getitem__(self: Self, index: int) -> RawRow:
        """Доступ на чтение строки матрицы по индексу"""
        return self.__rows[index]

    

    def __element_wise_operation(self: Self, operation: Callable, other: RawMatrix | Number) -> Self:
        """Выполняет переданную операцию матрицы с переданным объектом"""
        print(operation.__name__)
        new_object = Matrix(self.__rows)
        if type(other) is Matrix:
            for i in range(self.n):
                for j in range(self.m):
                    new_object[i][j] = self[i][j] + other[i][j]
        else:
            for i in range(self.n):
                for j in range(self.m):
                    new_object[i][j] = self[i][j] + other
        return new_object

  
    def __add__(self, other) -> Self:
        return self.element_wise_operation(add, other)  


    # def __neg__(self, other) -> Self:
        # new_object = Matrix(self.rows)
        # for i in range(len(self.rows)):
            # for j in range(len(self.rows)):
                # self.rows[i][j] -= other.rows[i][j]         
    
    
    # def __sub__(self, other) -> Self:
        # new_object = Matrix(self.rows)
        # for i in range(len(self.rows)):
            # for j in range(len(self.rows)):
                # new_object[i][j] = self.rows[i][j] - other.rows[i][j] 
        # return new_object 
    
    
    # def __mul__(self, other) -> Self:
        # pass
      
    
    
    def __repr__(self):
        representation = ''
        for i in range(self.n):
            for j in range(self.m):
                representation += f' {self.rows[i][j]}'
            representation += '\n'
        return representation