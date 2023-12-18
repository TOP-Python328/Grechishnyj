from chess import Piece, Square, Chessboard
from typing import Self, Callable
from datetime import datetime


class Memento:
    """Описывает момент хода (шаблон снимок) шахматной фигуры."""
    id_ = 1
    def __init__(
            self, piece: Piece, *,
            before: Square = None, 
            after: Square = None
        ):
        self.id = self.__class__.id_
        self._piece = piece
        self._square_before = before
        self.square_after = after
        self._time = datetime.now()
        self.__class__.id_ += 1
 
    @property
    def state(self) -> dict[str, Piece | Square]:
        """Возвращает состояние объекта."""
        return {
            'piece': self._piece, 
            'before': self._square_before,
            'after': self.square_after
            
        }

    def __repr__(self):
        return f'<{self._piece} : {self._square_before} -> {self.square_after}>'




class Turn(list):
    """История (шаблон опекун) сделанных ходов."""
    def __init__(self):
        self = super().__init__() 

    
    def save(self, memento: Memento) -> None:
        """Сохраняет снимок хода фигуры."""
        self.append(memento)

    def cancel(self) -> Memento:
        """Отменяет последний сделанный ход"""
        return self.pop()



class Game:
    """Описывает процесс игры"""
    id_ = 1
    
    def __init__(self):
        self.chess_board = Chessboard()
        self.id = self.__class__.id_
        self.turn = Turn()
        self.__class__.id_ += 1
        print(self.chess_board)
    
    def make_move(self, piece: Piece, square_after: str) -> None:
        """Сделать ход в игре."""
        square_start = piece.square
        square_end = self.chess_board.__getitem__(square_after)
        piece.move(square_end)
        memento = Memento(piece, before=square_start, after=square_end)
        self.turn.save(memento)
        # print(self.turn)

    def re_move(self) -> None:
        """Отменить последний сделанный ход."""
        if self.turn:
            memento = self.turn.cancel()
        else:
            return
        memento.state['piece'].move(memento.state['before'])

    def back_to_move(self, number_move) -> None:
        """Возврат игры к номеру хода"""
        if 0 < number_move < len(self.turn):
            for _ in range(number_move):
                self.re_move()
        
        
 # 14:11:01 > python -i 2023.12.01\1.py
# >>> game = Game()
# {'a': {1: <a1: White Rook>, 2: <a2: White Pawn>, 3: <a3: None>, 4: <a4: None>, 5: <a5: None>, 6: <a6: None>, 7: <a7: Black Pawn>, 8: <a8: Black Rook>}, 'b': {1: <b1: White Knight>, 2: <b2: White Pawn>, 3: <b3: None>, 4: <b4: None>, 5: <b5: None>, 6: <b6: None>, 7: <b7: Black Pawn>, 8: <b8: Black Knight>}, 'c': {1: <c1: White Bishop>, 2: <c2: White Pawn>, 3: <c3: None>, 4: <c4: None>, 5: <c5: None>, 6: <c6: None>, 7: <c7: Black Pawn>, 8: <c8: Black Bishop>}, 'd': {1: <d1: White Queen>, 2: <d2: White Pawn>, 3: <d3: None>, 4: <d4: None>, 5: <d5: None>, 6: <d6: None>, 7: <d7: Black Pawn>, 8: <d8: Black Queen>}, 'e': {1: <e1: White King>, 2: <e2: White Pawn>, 3: <e3: None>, 4: <e4: None>, 5: <e5: None>, 6: <e6: None>, 7: <e7: Black Pawn>, 8: <e8: Black King>}, 'f': {1: <f1: White Bishop>, 2: <f2: White Pawn>, 3: <f3: None>, 4: <f4: None>, 5: <f5: None>, 6: <f6: None>, 7: <f7: Black Pawn>, 8: <f8: Black Bishop>}, 'g': {1: <g1: White Knight>, 2: <g2: White Pawn>, 3: <g3: None>, 4: <g4: None>, 5: <g5: None>, 6: <g6: None>, 7: <g7: Black Pawn>, 8: <g8: Black Knight>}, 'h': {1: <h1: White Rook>, 2: <h2: White Pawn>, 3: <h3: None>, 4: <h4: None>, 5: <h5: None>, 6: <h6: None>, 7: <h7: Black Pawn>, 8: <h8: Black Rook>}}
# >>> wr = game.chess_board['a'][1].piece
# >>> game.chess_board.__getitem__('a1')
# <a1: White Rook>
# >>> game.make_move(wr, 'a3')
# [<WR : a1 -> a3>]
# >>> game.make_move(wr, 'a1')
# [<WR : a1 -> a3>, <WR : a3 -> a1>]
# >>> game.make_move(wr, 'a3')
# [<WR : a1 -> a3>, <WR : a3 -> a1>, <WR : a1 -> a3>]
# >>> game.make_move(wr, 'a1')
# [<WR : a1 -> a3>, <WR : a3 -> a1>, <WR : a1 -> a3>, <WR : a3 -> a1>]
# >>> game.re_move()
# >>> game.make_move(wr, 'a1')
# [<WR : a1 -> a3>, <WR : a3 -> a1>, <WR : a1 -> a3>, <WR : a3 -> a1>]
# >>> game.re_move()
# >>> game.make_move(wr, 'a1')
# [<WR : a1 -> a3>, <WR : a3 -> a1>, <WR : a1 -> a3>, <WR : a3 -> a1>]
# >>> game.re_move()
# >>> game.make_move(wr, 'a1')
# [<WR : a1 -> a3>, <WR : a3 -> a1>, <WR : a1 -> a3>, <WR : a3 -> a1>]
# >>> game.re_move()
# >>> game.re_move()
# >>> game.re_move()
# >>> game.make_move(wr, 'a1')
# [<WR : a1 -> a3>, <WR : a3 -> a1>]
# >>> game.re_move()
# >>> game.re_move()
# >>> game.make_move(wr, 'a3')
# [<WR : a1 -> a3>]
# >>>