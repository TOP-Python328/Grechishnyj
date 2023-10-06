from random import choice, randrange
from time import sleep


def exception_delay_repeat(func_obj: 'function') -> 'function':
    """Функция-декоратор которая повторяет вызов декорируемой функции в случае возникновения исключения"""
    def wrapper(*args, **kwargs) -> 'function':
        """Функция-обёртка"""
        counter = 0
        while True: 
            try:
                return func_obj(*args, **kwargs)
            except Exception as exception:
                counter += 1
                if counter > 1:
                    print(f'{exception!r}')
                    return None
                sleep(0.5)
    return wrapper

#  тестирование декоратора exception_delay_repeat

def test_func(num, divs):
    """doc"""
    choice_div = int(choice(divs))
    return f'end = {num / choice_div}'
    

def test_func_2():
    """doc"""
    if randrange(2):
        raise ConnectionError('failure')
    else:
        return 'succes'
        
test_func = exception_delay_repeat(test_func)
print('вызовы тестовой функции -> test_func()\n')
for i in range(10):
    result = test_func(5, [0, '0', 'a', 0, '0', 'a', 5])
    print(f'{i+1} вызов: {result=}')

       
test_func_2 = exception_delay_repeat(test_func_2)
print('\nвызовы тестовой функции -> test_func_2()\n') 
for i in range(10):
    result = test_func_2()
    print(f'{i+1} вызов: {result=}')      


# вызовы тестовой функции -> test_func()

# ZeroDivisionError('division by zero')
# 1 вызов: result=None
# 2 вызов: result='end = 1.0'
# ZeroDivisionError('division by zero')
# 3 вызов: result=None
# ZeroDivisionError('division by zero')
# 4 вызов: result=None
# ValueError("invalid literal for int() with base 10: 'a'")
# 5 вызов: result=None
# ZeroDivisionError('division by zero')
# 6 вызов: result=None
# 7 вызов: result='end = 1.0'
# ZeroDivisionError('division by zero')
# 8 вызов: result=None
# 9 вызов: result='end = 1.0'
# ZeroDivisionError('division by zero')
# 10 вызов: result=None

# вызовы тестовой функции -> test_func_2()

# 1 вызов: result='succes'
# 2 вызов: result='succes'
# ConnectionError('failure')
# 3 вызов: result=None
# 4 вызов: result='succes'
# 5 вызов: result='succes'
# 6 вызов: result='succes'
# 7 вызов: result='succes'
# 8 вызов: result='succes'
# ConnectionError('failure')
# 9 вызов: result=None
# 10 вызов: result='succes'