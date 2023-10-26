from collections.abc import Iterable
from numbers import Number
from operator import add, sub, mul
from typing import Self, Callable


RawRow = Iterable[Number]
RawMatrix = Iterable[RawRow]
ProcessedRow = list[Number]
ProcessedMatrix = list[ProcessedRow]


class Matrix:
    def __init__(self, raw_matrix: RawMatrix):
        if not self.is_valid(raw_matrix):
            raise ValueError('невозможно сконструировать матрицу')
        self.__rows: ProcessedMatrix = [list(row) for row in raw_matrix]
        self.n: int = len(self.__rows)
        self.m: int = len(self.__rows[0])
    
    @staticmethod
    def is_valid(raw_matrix: RawMatrix) -> bool:
        try:
            rls = set(len(row) for row in raw_matrix)
        except TypeError:
            return False
        else:
            return rls != {0} and len(rls) == 1
    
    @property
    def transpose(self) -> Self:
        return self.__class__([
            [
                self.__rows[i][j] 
                for i in range(self.n)
            ] 
            for j in range(self.m)
        ])
    
    def __getitem__(self, index: int) -> ProcessedRow:
        return self.__rows[index]
    
    def __element_wise_operation(self, other, operation: Callable) -> Self:
        if isinstance(other, self.__class__):
            if operation in (add, sub):
                if (self.n, self.m) == (other.n, other.m):
                    return self.__class__([
                        [
                            operation(self.__rows[i][j], other.__rows[i][j])
                            for j in range(self.m)
                        ]
                        for i in range(self.n)
                    ])
                else:
                    raise ValueError('сложение и вычитание возможно только для матриц одной размерности')
            else:
                raise NotImplementedError('умножение матриц будет реализовано в будущем')
        # elif isinstance(other, Iterable):
        #     if operation in (add, sub):
        #         return operation(self, self.__class__(other))
        #     else:
        #         raise NotImplementedError('умножение матриц будет реализовано в будущем')
        elif isinstance(other, Number):
            return self.__class__([
                [
                    operation(self.__rows[i][j], other)
                    for j in range(self.m)
                ]
                for i in range(self.n)
            ])
        else:
            raise TypeError('алгебраические операции возможны только с матрицами и числами')
    
    def __add__(self, other) -> Self:
        return self.__element_wise_operation(other, add)
    
    def __radd__(self, other) -> Self:
        return self.__element_wise_operation(other, add)
    
    def __neg__(self) -> Self:
        return self.__element_wise_operation(-1, mul)
    
    def __sub__(self, other) -> Self:
        return self.__element_wise_operation(other, sub)
    
    def __rsub__(self, other) -> Self:
        return (-self).__element_wise_operation(other, add)
    
    def __mul__(self, other) -> Self:
        return self.__element_wise_operation(other, mul)
    
    def __rmul__(self, other) -> Self:
        return self.__element_wise_operation(other, mul)
    
    def __repr__(self):
        width = max(len(str(elem)) for row in self.__rows for elem in row)
        return '\n'.join(
            ' '.join(f'{elem:>{width}}' for elem in row)
            for row in self.__rows
        )


m1 = Matrix([[1, 1, 1], [1, 1, 1]])
m2 = Matrix([[3, 3, 3], [3, 3, 3]])

m3 = Matrix([[1, 2], [3, 4]])
