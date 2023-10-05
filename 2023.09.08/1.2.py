from random import choice
from time import sleep


def exception_delay_repeat(func_obj):
    """Функция-декоратор которая повторяет вызов декорируемой функции в случае возникновения исключения"""
    
    def wrapper(*args, **kwargs):
        """Функция-обертка"""
        while True: 
            try:
                return func_obj(*args, **kwargs)
            except:
                print('перехват нужного исключения')
                sleep(0.5)
    return wrapper
    
 
def test_func(num, divs):
    """doc"""
    choice_div = choice(divs)
    print(f'choice_div = {choice_div}')
    return f'end = {num / choice_div}'

test_func = exception_delay_repeat(test_func)
test_func(5, [0, 0, 0, 0, 0, 0, 0, 0, 5])

# 20:19:56 > python -i 2023.09.08\1.2.py
# choice_div = 0
# перехват нужного исключения
# choice_div = 0
# перехват нужного исключения
# choice_div = 0
# перехват нужного исключения
# choice_div = 0
# перехват нужного исключения
# choice_div = 0
# перехват нужного исключения
# choice_div = 0
# перехват нужного исключения
# choice_div = 0
# перехват нужного исключения
# choice_div = 0
# перехват нужного исключения
# choice_div = 5