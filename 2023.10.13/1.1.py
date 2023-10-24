from numbers import Number
from collections.abc import Iterable
from typing import Self, Callable
from operator import add, sub, neg, mul

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
        return self.__rows


    def __getitem__(self: Self, index: int) -> RawRow:
        """Доступ на чтение строки (элемента) матрицы по индексу"""
        return self.__rows[index]
    
    # В работе...
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



    # В работе...
    def __repr__(self):
        representation = ''
        for i in range(self.n):
            for j in range(self.m):
                representation += f' {self.__rows[i][j]}'
            representation += '\n'
        return representation
        
        
   
# a = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
# b = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]


# >>> m1 = Matrix(a)
# >>> -m1
 # -1 -1 -1 -1 -1
 # -1 -1 -1 -1 -1
 # -1 -1 -1 -1 -1

# >>> m1 = Matrix(a)
# >>> m2 = m1 * 5
# >>> m3 = 4 * m1
# >>> m4 = m1 - 6
# >>> m5 = 9 - m4
# >>> m6 = m1 + m2
# >>> m1
 # 1 1 1 1 1
 # 1 1 1 1 1
 # 1 1 1 1 1

# >>> m2
 # 5 5 5 5 5
 # 5 5 5 5 5
 # 5 5 5 5 5

# >>> m3
 # 4 4 4 4 4
 # 4 4 4 4 4
 # 4 4 4 4 4

# >>> m4
 # -5 -5 -5 -5 -5
 # -5 -5 -5 -5 -5
 # -5 -5 -5 -5 -5

# >>> m5
 # -14 -14 -14 -14 -14
 # -14 -14 -14 -14 -14
 # -14 -14 -14 -14 -14

# >>> m6
 # 6 6 6 6 6
 # 6 6 6 6 6
 # 6 6 6 6 6

# >>> m1 + m2 + m3
 # 10 10 10 10 10
 # 10 10 10 10 10
 # 10 10 10 10 10

# >>> m7 = m1 + m2 + m3 + m4 + m5 + m6
# >>> m7
 # -3 -3 -3 -3 -3
 # -3 -3 -3 -3 -3
 # -3 -3 -3 -3 -3

# >>> m7.transpose
# [[-3, -3, -3], [-3, -3, -3], [-3, -3, -3], [-3, -3, -3], [-3, -3, -3]]
# >>> m7
 # -3 -3 -3
 # -3 -3 -3
 # -3 -3 -3
 # -3 -3 -3
 # -3 -3 -3

# >>> -m7
 # 3 3 3
 # 3 3 3
 # 3 3 3
 # 3 3 3
 # 3 3 3
