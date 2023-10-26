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
            # ИСПРАВИТЬ: согласно условию передать можно любой итерируемый объект, а для соблюдения требования изменяемости в атрибуте должен быть список списков чисел
            self.__rows = raw_matrix
            self.n = len(raw_matrix)
            self.m = len(raw_matrix[0])

    @staticmethod
    def is_valid(raw_matrix: RawMatrix) -> bool:
        """Метод проверяет, является ли аргумент подходящим объектом для конструирования матрицы"""
        # УДАЛИТЬ: в задании нет требования о том, чтобы переданный в конструктор аргумент был именно списком — да и аннотация как бы намекает
        if not isinstance(raw_matrix, list):
            # КОММЕНТАРИЙ: да и в тесте у меня нет таких сообщений
            raise ValueError('невозможно сконструировать матрицу: матрица должна быть списком')
        for row in raw_matrix:
            if not isinstance(row, list):
                raise ValueError('невозможно сконструировать матрицу: ряды матрицы должны быть списками')
                # ИСПРАВИТЬ: код после выброса исключения никогда не будет выполнен
                for num in row:
                    if not isinstance(num, Number):
                        raise ValueError('невозможно сконструировать матрицу: элементами рядов матрицы должны быть числа')
        # ДОБАВИТЬ: обработчик исключений (try)
        if len(set(map(len, raw_matrix))) != 1:
            raise ValueError('невозможно сконструировать матрицу: матрица должна содержать ряды с одинаковой длинной')
        return True

    @property
    def transpose(self: Self) -> Self:
        """Метод возвращает транспонированную матрицу"""
        return self.__class__([[self.__rows[j][i] for j in range(self.n)] for i in range(self.m)])

    def __getitem__(self: Self, index: int) -> RawRow:
        """Доступ на чтение строки (элемента) матрицы по индексу"""
        return self.__rows[index]

    def __element_wise_operation(self, operation: Callable, other: Self | Number) -> Self:
        """Выполняет переданную операцию со своим и переданным объектом"""
        if isinstance(other, Number):
            return self.__class__([[operation(self[i][j], other) for j in range(self.m)] for i in range(self.n)])
        elif isinstance(other, self.__class__):
            if operation is mul:
                raise NotImplementedError('умножение матриц будет реализованно в будущем')
            if self.n == other.n and self.m == other.m:
                return self.__class__([[operation(self[i][j],  other[i][j]) for j in range(self.m)] for i in range(self.n)])
            else:
                raise ValueError('сложение и вычитание возможно только для матриц одной размерности')

    def __add__(self, other) -> Self:
        return self.__element_wise_operation(add, other)

    def __radd__(self, other) -> Self:
        return self.__element_wise_operation(add, other)

    def __sub__(self, other) -> Self:
        return self.__element_wise_operation(sub, other)

    def __rsub__(self, other) -> Self:
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


# КОММЕНТАРИЙ: должна быть возможность создать матрицу из такого объекта
# >>> m1 = Matrix(((1, 2), (3, 4)))
# КОММЕНТАРИЙ: и должна быть возможность дальше работать с ним как с матрицей
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


# Тесты после изменений
# >>> m1 = Matrix(1)
# ...
# ValueError: невозможно сконструировать матрицу: матрица должна быть списком
# >>> m1 = Matrix(((1, 2), (3, 4)))
# ...
# ValueError: невозможно сконструировать матрицу: матрица должна быть списком
# >>> m1 = Matrix([(1, 2), (3, 4)])
# ...
# ValueError: невозможно сконструировать матрицу: ряды матрицы должны быть списками
# >>> m1 = Matrix([1,2,3])
# ...
# ValueError: невозможно сконструировать матрицу: ряды матрицы должны быть списками
# >>> m1 = Matrix(([1,2,3], [1,2,3], [1,2,3]))
# ...
# ValueError: невозможно сконструировать матрицу: матрица должна быть списком

# >>> m1 = Matrix([[1,2,3], [1,2,3], [1,2,3], []])
# ...
# ValueError: невозможно сконструировать матрицу: матрица должна содержать ряды с одинаковой длинной

# >>> m1 = Matrix([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
# >>> m1
 # 1  1  1  1  1
 # 1  1  1  1  1
 # 1  1  1  1  1

# >>> m1.transpose
 # 1  1  1
 # 1  1  1
 # 1  1  1
 # 1  1  1
 # 1  1  1

# >>> m1 + 1
 # 2  2  2  2  2
 # 2  2  2  2  2
 # 2  2  2  2  2

# >>> 1 + m1
 # 2  2  2  2  2
 # 2  2  2  2  2
 # 2  2  2  2  2

# >>> m1 - 1
 # 0  0  0  0  0
 # 0  0  0  0  0
 # 0  0  0  0  0

# >>> 1 - m1
 # 0  0  0  0  0
 # 0  0  0  0  0
 # 0  0  0  0  0

# >>> m1 * 2
 # 2  2  2  2  2
 # 2  2  2  2  2
 # 2  2  2  2  2

# >>> m2 = m1 * 4
# >>> m2
 # 4  4  4  4  4
 # 4  4  4  4  4
 # 4  4  4  4  4

# >>> m1 + m2
 # 5  5  5  5  5
 # 5  5  5  5  5
 # 5  5  5  5  5

# >>> m2 + m1
 # 5  5  5  5  5
 # 5  5  5  5  5
 # 5  5  5  5  5

# >>> m1 - m2
# -3 -3 -3 -3 -3
# -3 -3 -3 -3 -3
# -3 -3 -3 -3 -3

# >>> m2 - m1
 # 3  3  3  3  3
 # 3  3  3  3  3
 # 3  3  3  3  3

# >>> m1 * m2
# ...
# NotImplementedError: умножение матриц будет реализованно в будущем


# ИТОГ: хорошо — 8/10


# СДЕЛАТЬ: изучите пример решения
