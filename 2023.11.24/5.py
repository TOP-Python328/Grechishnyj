from random import randrange as rr, sample
from string import ascii_lowercase as letters
from contextlib import redirect_stdout
from typing import Self, Callable
from pathlib import Path
from sys import path
from io import StringIO
import inspect


class TestCase:
    """
    Адресат.
    """
    def __init__(self):
        self.messages = [
            ''.join(sample(letters, k=rr(3, 7)))
            for _ in range(1000)
        ]
        self.numbers = [
            (rr(10, 100) for _ in range(rr(4, 6))) 
            for _ in range(1000)
        ]
    
    def print_msg(self):
        msg = self.messages.pop()
        print(msg)
    
    def print_nums(self):
        nums = self.numbers.pop()
        print(*nums)


class Listener:
    """Слушатель функций"""
    @staticmethod
    def code():
        current_frame = inspect.currentframe()
        caller_frame = current_frame.f_back
        code_obj = caller_frame.f_code
        code_obj_name = code_obj.co_name
        code_obj_vars = code_obj.co_varnames
        # print(caller_frame.__dir__())
        # print(caller_frame.f_locals)
        return f"Операция: {code_obj_name}"
 

class Logger(dict):
    """
    История операций
    """
    def __init__(self):
        super().__init__()
        self['completed']: list[str] = []
        self['cancelled']: list[str] = []

    def add_log(self, log: str):
        self['completed'].append(log)

    def del_log(self):
        last_log = self['completed'].pop()
        self['cancelled'].append(last_log)
    
    
class TCCommand:
    """
    Команда
    """
    def __init__(self, testcase: TestCase):
        self.testcase = testcase
        self.logger = Logger()

    def save(self, operation: Callable) -> None:
        """Сохранение операции"""
        listener = Listener.code()
        log = StringIO()
        with redirect_stdout(log):
            operation()
        self.logger.add_log(f"{listener} результат: {log.getvalue()}")

    def cancel(self, count: int = 1) -> None:
        """Отмена последних операций"""
        for i in range(count):
            self.logger.del_log()

 
testcase = TestCase()
command = TCCommand(testcase)
command.save(testcase.print_nums)


# >>> command.logger
# {'completed': ['Операция: save результат: 90 25 76 96 40\n'], 'cancelled': []}
# >>> command.save(testcase.print_nums)
# >>> command.save(testcase.print_nums)
# >>> command.save(testcase.print_nums)
# >>> command.save(testcase.print_nums)
# >>> command.logger
# {'completed': ['Операция: save результат: 90 25 76 96 40\n', 'Операция: save результат: 78 62 34 31\n', 'Операция: save результат: 86 79 86 60 88\n', 'Операция: save результат: 99 41 87 44\n', 'Операция: save результат: 11 36 66 12\n'], 'cancelled': []}
# >>> command.cancel(1)
# >>> command.logger
# {'completed': ['Операция: save результат: 90 25 76 96 40\n', 'Операция: save результат: 78 62 34 31\n', 'Операция: save результат: 86 79 86 60 88\n', 'Операция: save результат: 99 41 87 44\n'], 'cancelled': ['Операция: save результат: 11 36 66 12\n']}
# >>> command.cancel(3)
# >>> command.logger
# {'completed': ['Операция: save результат: 90 25 76 96 40\n'], 'cancelled': ['Операция: save результат: 11 36 66 12\n', 'Операция: save результат: 99 41 87 44\n', 'Операция: save результат: 86 79 86 60 88\n', 'Операция: save результат: 78 62 34 31\n']}