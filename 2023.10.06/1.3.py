

class ChessKing:
    """Шахматная фигура короля
    
    :attr files: соответствие между буквой, обозначающей вертикаль шахматной доски и числом:
    :attr ranks: соответствие между строковым представлением числа (горизонталь) и числом:
    """
    files: dict[str, int] = {'abcdefgh'[i]: i+1 for i in range(8)}
    ranks: dict[str, int] = {'12345678'[i]: i+1 for i in range(8)}
    
    
    
    def __init__(self, color: str = 'white', square: str = None):
        """
        :attr color: цвет фигуры
        :attr square: поле шахматной доски, где в данный момент находится фигура
        """
        self.color = color
        self.square = {'white': 'e2', 'black': 'e8'}[color] if not square else square


wk = ChessKing()
bk = ChessKing('black')