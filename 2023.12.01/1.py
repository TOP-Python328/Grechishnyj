from chess import Piece, Square, Chessboard
from typing import Self, Callable
from datetime import datetime


class Memento:
    """Хранитель - шаблон снимок."""
    id_ = 1
    def __init__(
            self, piece: Piece, 
            square_before: Square = None, 
            square_about: Square = None
        ):
        self.id = self.__class__.id_
        self._piece = piece
        self._square_about = square_about
        self._square_before = square_before
        self._time = datetime.now()
        self.__class__.id_ += 1
 
    @property
    def state(self) -> dict[str, Piece | Square]:
        """Возвращает состояние объекта."""
        return {
            'piece': self._piece, 
            'about': self._square_about, 
            'before': self._square_before
        }

    def __repr__(self):
        return f'<{self._piece} : {self._square_before} -> {self._square_about}>'




class Turn(list):
    """История (хронолическая очередь) сделанных ходов."""
    def __init__(self):
        self = super().__init__() 

    
    def save(self, memento: Memento):
        """Сохраняет снимок хода фигуры."""
        self.append(memento)

    def cancel(self):
        """Отменяет последний сделанный ход"""
        last_memento = self.pop()
        print(last_memento)



class Game:
    """Описывает процесс игры"""
    id_ = 1
    
    def __init__(self):
        self.chess_board = Chessboard()
        self.number = self.__class__.id_
        self.turn = Turn()
        self.__class__.id_ += 1
        print(self.chess_board)
    
    
# >>> game = Game()
# {'a': {1: <a1: White Rook>, 2: <a2: White Pawn>, 3: <a3: None>, 4: <a4: None>, 5: <a5: None>, 6: <a6: None>, 7: <a7: Black Pawn>, 8: <a8: Black Rook>}, 'b': {1: <b1: White Knight>, 2: <b2: White Pawn>, 3: <b3: None>, 4: <b4: None>, 5: <b5: None>, 6: <b6: None>, 7: <b7: Black Pawn>, 8: <b8: Black Knight>}, 'c': {1: <c1: White Bishop>, 2: <c2: White Pawn>, 3: <c3: None>, 4: <c4: None>, 5: <c5: None>, 6: <c6: None>, 7: <c7: Black Pawn>, 8: <c8: Black Bishop>}, 'd': {1: <d1: White Queen>, 2: <d2: White Pawn>, 3: <d3: None>, 4: <d4: None>, 5: <d5: None>, 6: <d6: None>, 7: <d7: Black Pawn>, 8: <d8: Black Queen>}, 'e': {1: <e1: White King>, 2: <e2: White Pawn>, 3: <e3: None>, 4: <e4: None>, 5: <e5: None>, 6: <e6: None>, 7: <e7: Black Pawn>, 8: <e8: Black King>}, 'f': {1: <f1: White Bishop>, 2: <f2: White Pawn>, 3: <f3: None>, 4: <f4: None>, 5: <f5: None>, 6: <f6: None>, 7: <f7: Black Pawn>, 8: <f8: Black Bishop>}, 'g': {1: <g1: White Knight>, 2: <g2: White Pawn>, 3: <g3: None>, 4: <g4: None>, 5: <g5: None>, 6: <g6: None>, 7: <g7: Black Pawn>, 8: <g8: Black Knight>}, 'h': {1: <h1: White Rook>, 2: <h2: White Pawn>, 3: <h3: None>, 4: <h4: None>, 5: <h5: None>, 6: <h6: None>, 7: <h7: Black Pawn>, 8: <h8: Black Rook>}}
# >>>
# >>> game.number
# 1
# >>> game.turn
# []
# >>>
# >>> memento = Memento('Piece', 'Start', 'End')
# >>> memento
# <Piece : Start -> End>
# >>>
# >>> game.turn.save(memento)
# >>> game.turn
# [<Piece : Start -> End>]
# >>> game.turn.cancel()
# <Piece : Start -> End>
# >>> game.turn
# []
# >>>

