from numbers import Number

class Matrix:
    """Класс моделирует неизменяемую матрицу"""
    
    def __init__(self, *args: Number, n: int, m: int):
        """Конструктор экземпляра класса.
        
        :param *args: элементы матрицы
        :param n: количество строк
        :param m: количество столбцов
        """
        # УТОЧНИТЬ: стрктуру данных
        if self.is_valid(*args, row=n, col=m):
            print(args, n, m)
            flat: tuple[Number, ...] = ([args[i][j] for i in range(n)] for j in range(m)) 
        
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