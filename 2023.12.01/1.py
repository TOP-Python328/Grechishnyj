from chess import Piece, Square, Chessboard
from typing import Self, Callable
from datetime import datetime
from os import get_terminal_size


class Memento:
    """Описывает момент хода (шаблон снимок) шахматной фигуры."""
    def __init__(
            self, piece: Piece,
            before: Square = None, 
            after: Square = None
        ):
        self._piece = piece
        self._square_before = before
        self.square_after = after
        self._time = datetime.now()
 
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
    """История-очередь (шаблон опекун) сделанных ходов."""
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
        # print(self.chess_board)
    
    def make_move(self, piece: Piece, square_after: str) -> None:
        """Сделать ход в игре."""
        square_start = piece.square
        square_end = self.chess_board.__getitem__(square_after)
        piece.move(square_end)
        memento = Memento(piece, square_start, square_end)
        self.turn.save(memento)

    def re_move(self) -> None:
        """Отменить последний сделанный ход."""
        if self.turn:
            memento = self.turn.cancel()
        else:
            return
        memento.state['piece'].move(memento.state['before'])

    def back_to_move(self, number_move) -> None:
        """Возврат игры к началу заданного хода."""
        length = len(self.turn)
        if 0 < number_move < length:
            target_move = length - number_move + 1
            for _ in range(target_move):
                self.re_move()
    
    @property
    def report(self):
        """Вывод всех сделанных ходов"""
        line = '-' * get_terminal_size().columns
        protocol = line + f'\tREPORT GAME: {self.id}\n' + line
        number = 1
        
        for memento in self.turn:
            protocol += f'\t{number}. {memento._piece} | {memento._square_before} | {memento.square_after} | {memento._time.ctime()}\n'
            number += 1
        protocol += line + '\tEND REPORT\n' + line
        return(protocol)

if __name__ == '__main__':

    game = Game()
    wr = game.chess_board['a'][1].piece
    game.make_move(wr, 'a3')
    game.make_move(wr, 'a1')
    game.make_move(wr, 'a3')
    game.make_move(wr, 'a1')
    game.make_move(wr, 'a3')
    game.make_move(wr, 'a1')
    game.make_move(wr, 'a3')
    game.make_move(wr, 'a1')
    game.make_move(wr, 'a3')
    game.make_move(wr, 'a1')
    game.make_move(wr, 'a3')
    game.make_move(wr, 'a1')
    game.make_move(wr, 'a3')
    game.make_move(wr, 'a1')

    game.back_to_move(5)
    print(game.report)
    
    game = Game()
    wr = game.chess_board['a'][1].piece
    game.make_move(wr, 'a3')
    game.make_move(wr, 'a1')
    game.make_move(wr, 'a3')
    game.make_move(wr, 'a1')
    game.make_move(wr, 'a3')
    game.make_move(wr, 'a1')
    game.make_move(wr, 'a3')
    game.make_move(wr, 'a1')
    game.make_move(wr, 'a3')
    game.make_move(wr, 'a1')
    game.make_move(wr, 'a3')
    game.make_move(wr, 'a1')
    game.make_move(wr, 'a3')
    game.make_move(wr, 'a1')

    game.back_to_move(10)
    print(game.report)


# -------------------------------------------------------------------------------------------
#     REPORT GAME: 1
# -------------------------------------------------------------------------------------------
#     1. WR | a1 | a3 | Mon Dec 18 15:54:10 2023
#     2. WR | a3 | a1 | Mon Dec 18 15:54:10 2023
#     3. WR | a1 | a3 | Mon Dec 18 15:54:10 2023
#     4. WR | a3 | a1 | Mon Dec 18 15:54:10 2023
# -------------------------------------------------------------------------------------------
#     END REPORT
# -------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------
#     REPORT GAME: 2
# -------------------------------------------------------------------------------------------
#     1. WR | a1 | a3 | Mon Dec 18 15:54:10 2023
#     2. WR | a3 | a1 | Mon Dec 18 15:54:10 2023
#     3. WR | a1 | a3 | Mon Dec 18 15:54:10 2023
#     4. WR | a3 | a1 | Mon Dec 18 15:54:10 2023
# -------------------------------------------------------------------------------------------
#     END REPORT
# -------------------------------------------------------------------------------------------