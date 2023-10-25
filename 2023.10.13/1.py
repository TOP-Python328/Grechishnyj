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
        
        :param raw_matrix: строки матрицы
        """
        if self.is_valid(raw_matrix):
            # ИСПРАВИТЬ: здесь должен быть уже не любой итерируемый объект, а именно список списков чисел (см. тест ниже)
            self.__rows = raw_matrix
            self.n = len(raw_matrix)
            self.m = len(raw_matrix[0])
        else:
            raise ValueError('невозможно сконструировать матрицу')


    @staticmethod
    def is_valid(raw_matrix: RawMatrix) -> bool:
        """Метод проверяет, является ли аргумент подходящим объектом для конструирования матрицы"""
        # ДОБАВИТЬ: обработчики исключений (см. тест ниже)
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
        # ИСПРАВИТЬ: операция транспонирования должна возвращать новый объект, а не изменённый текущий экземпляр
        # ИПРАВЛЕНО
        return Matrix([[self.__rows[j][i] for j in range(self.n)] for i in range(self.m)])

    def __getitem__(self: Self, index: int) -> RawRow:
        """Доступ на чтение строки (элемента) матрицы по индексу"""
        return self.__rows[index]

    def __element_wise_operation(self, operation: Callable, other: Self | Number) -> Self:
        """Выполняет переданную операцию со своим и переданным объектом"""
        # ИСПРАВИТЬ: предварительное создание нулевой матрицы избыточно, это лишние итерации — создавайте генераторными выражениями объект с вычисленными значениями и сразу передавайте этот объект в конструктор
        # ИСПРАВЛЕНО
        if isinstance(other, Number):
            return Matrix([[operation(self[i][j], other) for j in range(self.m)] for i in range(self.n)])
        elif isinstance(other, Matrix):
            # ИСПРАВИТЬ: лучше сравнить напрямую идентичность с объектом функции
            # ИСПРАВЛЕНО
            if operation is mul:
                raise NotImplementedError('умножение матриц будет реализованно в будущем')
            # ИСПРАВИТЬ: складываются матрицы только строго одной размерности, а не только по одному из измерений (см. тест ниже)
            # ИСПРАВЛЕНО
            if self.n == other.n and self.m == other.m:
                return Matrix([[operation(self[i][j],  other[i][j]) for j in range(self.m)] for i in range(self.n)])
            else:
                raise ValueError('сложение и вычитание возможно только для матриц одной размерности')


    def __add__(self, other) -> Self:
        return self.__element_wise_operation(add, other)

    def __radd__(self, other) -> Self:
        return self.__element_wise_operation(add, other)

    def __sub__(self, other) -> Self:
        return self.__element_wise_operation(sub, other)

    def __rsub__(self, other) -> Self:
        # ИСПРАВИТЬ: переставлять объекты в вычитании надо с сохранением знаков (см. тест ниже)
        # КОММЕНТАРИЙ: я зачем вам унарное отрицание подкинул, мм?..)
        # ИСПРАВЛЕНО
        sub_matrix = -self
        return sub_matrix.__element_wise_operation(add, other)

    def __mul__(self, other) -> Self:
        return self.__element_wise_operation(mul, other)

    def __rmul__(self, other) -> Self:
        return self.__element_wise_operation(mul, other)

    def __neg__(self) -> Self:
        return self.__element_wise_operation(mul, -1)

    
    # def __repr__(self):
        # КОММЕНТАРИЙ: не выводит дробную часть, потому что %d — это код для целого числа, для вещественного — %f
        # format_item = f'%{len(str(max(abs(i) for i in chain(*self.__rows))))}d'
        # representation = ''
        # for i in range(self.n):
            # representation += f'{" ".join(format_item %(self.__rows[i][j]) for j in range(self.m))} \n'
        # return representation

    def __repr__(self):
        # ИСПРАВИТЬ: используйте генераторное выражение в ещё одном join() — и не будет ни лишних пробелов, ни лишних eol
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

# ДОБАВИТЬ: тесты правосторонних методов перегрузки операторов (число плюс/минус матрица)

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

# >>> m1 = Matrix(((1, 2), (3, 4)))
# >>> m1[0][0] = -1
# ...
# TypeError: 'tuple' object does not support item assignment

# >>> m1 = Matrix([1,2,3])
# ...
# TypeError: object of type 'int' has no len()

# >>> m1 = Matrix([(1, 2), (3, 4)])
# >>> m2 = Matrix([(1, 2, 3, 4), (5, 6, 7, 8)])
# >>> m2 + m1
# ...
# IndexError: tuple index out of range

# >>> m1 = Matrix([(1, 1), (1, 1)])
# >>> 5 - m1
# -4 -4
# -4 -4
# КОММЕНТАРИЙ: а должны быть положительными


# ИТОГ: хорошо — 7/10
