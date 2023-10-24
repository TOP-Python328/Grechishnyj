from numbers import Number
from collections.abc import Iterable
from typing import Self, Callable
from operator import add, sub, neg, mul
from itertools import chain

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
    def transpose(self: Self) -> Self:
        """Метод возвращает транспонированную матрицу"""
        self.__rows = [[self.__rows[j][i] for j in range(self.n)] for i in range(self.m)]
        self.n, self.m = self.m, self.n
        return self


    def __getitem__(self: Self, index: int) -> RawRow:
        """Доступ на чтение строки (элемента) матрицы по индексу"""
        return self.__rows[index]

    
    def __element_wise_operation(self, operation: Callable, other: Self | Number) -> Self:
        """Выполняет переданную операцию со своим и переданным объектом"""
        new_matrix = Matrix([[0 for _ in range(self.m)] for _ in range(self.n)])
        if isinstance(other, Number): 
            for i in range(self.n):
                for j in range(self.m):
                    new_matrix[i][j] = operation(self[i][j], other)
        elif isinstance(other, Matrix):
            if operation.__name__ == 'mul':
                raise NotImplementedError('умножение матриц будет реализованно в будущем')
            if self.n == other.n or self.m == other.m:
                for i in range(self.n):
                    for j in range(self.m):
                        new_matrix[i][j] = operation(self[i][j], other[i][j])
            else:
                raise ValueError('сложение и вычитание возможно только для матриц одной размерности')
        return new_matrix
        
    
    def __add__(self, other) -> Self:
        """docstring"""
        return self.__element_wise_operation(add, other)

        
    def __radd__(self, other) -> Self:
        """docstring"""
        return self.__element_wise_operation(add, other)

      
    def __sub__(self, other) -> Self:
        """docstring"""
        return self.__element_wise_operation(sub, other)  


    def __rsub__(self, other) -> Self:
        """docstring"""
        return self.__element_wise_operation(sub, other) 

    
    def __mul__(self, other) -> Self:
        """docstring"""
        return self.__element_wise_operation(mul, other)  


    def __rmul__(self, other) -> Self:
        """docstring"""
        return self.__element_wise_operation(mul, other)  


    def __neg__(self) -> Self:
        """docstring"""
        return self.__element_wise_operation(mul, -1)       


    # не выводит дробную часть
    # def __repr__(self):
        # format_item = f'%{len(str(max(abs(i) for i in chain(*self.__rows))))}d'
        # representation = ''
        # for i in range(self.n):
            # representation += f'{" ".join(format_item %(self.__rows[i][j]) for j in range(self.m))} \n'
        # return representation

    def __repr__(self):
        representation = ''
        for i in range(self.n):
            representation += " ".join(f"{round(self[i][j], 1):>2}" for j in range(self.m)) + '\n'
        return representation
        
  
# >>> a = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
# >>> m1 = Matrix(a)
# >>> m1
 # 1  2  3  4  5
 # 6  7  8  9 10
# 11 12 13 14 15

# >>> m2 = m1 * 3
# >>> m3 = m2 * 0.5 - m1
# >>> m4 = m1 + m2 + m3
# >>> m1
 # 1  2  3  4  5
 # 6  7  8  9 10
# 11 12 13 14 15

# >>> m2
 # 3  6  9 12 15
# 18 21 24 27 30
# 33 36 39 42 45

# >>> m3
# 0.5 1.0 1.5 2.0 2.5
# 3.0 3.5 4.0 4.5 5.0
# 5.5 6.0 6.5 7.0 7.5

# >>> m4
# 4.5 9.0 13.5 18.0 22.5
# 27.0 31.5 36.0 40.5 45.0
# 49.5 54.0 58.5 63.0 67.5

# >>> m1[0][0] = 0
# >>> m2[0][0] = 0
# >>> m3[0][0] = 0
# >>> m4[0][0] = 0
# >>>
# >>> m1.transpose
 # 0  6 11
 # 2  7 12
 # 3  8 13
 # 4  9 14
 # 5 10 15

# >>> m2.transpose
 # 0 18 33
 # 6 21 36
 # 9 24 39
# 12 27 42
# 15 30 45

# >>> m3.transpose
 # 0 3.0 5.5
# 1.0 3.5 6.0
# 1.5 4.0 6.5
# 2.0 4.5 7.0
# 2.5 5.0 7.5

# >>> m4.transpose
 # 0 27.0 49.5
# 9.0 31.5 54.0
# 13.5 36.0 58.5
# 18.0 40.5 63.0
# 22.5 45.0 67.5


