from collections.abc import Iterable
from functools import cache, cached_property
from itertools import chain, repeat
from numbers import Number
from operator import add, sub
from typing import Self, Callable


RawRow = Iterable[Number]
ProcessedRow = tuple[Number, ...]


class Matrix:
    def __init__(self, *numbers: Number, n: int, m: int):
        if not self.is_valid(numbers, n=n, m=m):
            raise ValueError('невозможно сконструировать матрицу')
        self.__flat: ProcessedRow = numbers
        self.n = n
        self.m = m
        self.__transpose: RawRow = chain.from_iterable([
            numbers[i::m]
            for i in range(self.m)
        ])
    
    @staticmethod
    def is_valid(numbers: ProcessedRow, n: int, m: int) -> bool:
        return (
                len(numbers) == n * m 
            and all(map(lambda x: isinstance(x, Number), numbers))
        )
    
    @cached_property
    def transpose(self) -> Self:
        return self.__class__(*self.__transpose, n=self.m, m=self.n)
    
    def __element_wise_operation(self, other, operation: Callable) -> Self:
        if isinstance(other, self.__class__):
            if (self.n, self.m) == (other.n, other.m):
                return self.__class__(
                    *(
                        operation(*xy)
                        for xy in zip(self.__flat, other.__flat)
                    ),
                    n=self.n,
                    m=self.m
                )
            else:
                raise ValueError('сложение и вычитание возможно только для матриц одной размерности')
        # elif isinstance(other, Iterable):
        #     return operation(
        #         self,
        #         self.__class__(*other, n=self.n, m=self.m)
        #     )
        elif isinstance(other, Number):
            return self.__class__(
                *(operation(x, other) for x in self.__flat), 
                n=self.n, 
                m=self.m
            )
        else:
            raise TypeError('алгебраические операции возможны только с матрицами и числами')
    
    def __add__(self, other) -> Self:
        return self.__element_wise_operation(other, add)
    
    def __radd__(self, other) -> Self:
        return self + other
        
    def __neg__(self) -> Self:
        return -1 * self

    def __sub__(self, other) -> Self:
        return self.__element_wise_operation(other, sub)
    
    def __rsub__(self, other) -> Self:
        return -self + other
    
    def __mul__(self, other) -> Self:
        if isinstance(other, Number):
            return self.__class__(
                *(x*other for x in self.__flat), 
                n=self.n, 
                m=self.m
            )
        elif isinstance(other, self.__class__):
            raise NotImplementedError('умножение матриц будет реализовано в будущем')
        else:
            raise TypeError('алгебраические операции возможны только с матрицами и числами')
    
    def __rmul__(self, other) -> Self:
        return self * other
    
    @cache
    def __repr__(self):
        width = max(len(str(n)) for n in self.__flat)
        return '\n'.join(
            ' '.join(f'{elem:>{width}}' for elem in self.__flat[i:i+self.m])
            for i in range(0, self.n*self.m, self.m)
        )


m1 = Matrix(*repeat(1, 15), n=3, m=5)
m2 = Matrix(*range(1, 16), n=3, m=5)

m3 = Matrix(*range(1, 5), n=2, m=2)
