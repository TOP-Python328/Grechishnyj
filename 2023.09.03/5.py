from pathlib import Path
from sys import path
from datetime import datetime as dt

def logger(func_obj: 'function') -> 'function':
    """
        Функция - декоратор, ведет журнал вызовов декорируемой функции
        Вызовы функции записываются в файл - журнал вызовов (data/function_calls.log)
    """
    
    def wrapper(*args, **kwargs):
        """Функция-обертка, вызывает декорируемую функцию"""
        
        kwargs_default = dict(zip(reversed(func_obj.__code__.co_varnames),reversed(func_obj.__defaults__)))
        kwargs_update = kwargs_default | dict(reversed(tuple(kwargs.items())))

        args_position = tuple(map(lambda item: str(item), args))
        args_keywords = tuple(map(lambda item: f'{item[0]}={item[1]}', reversed(kwargs_update.items())))
            
        string_params = ', '.join((*args_position, *args_keywords))
        string_logger = f'{func_obj.__name__}({string_params})'
        
        try: 
            result = func_obj(*args, **kwargs)
            logstring = (f'{dt.now().strftime("%Y.%m.%d %H:%M:%S")} -> {string_logger} -> {result}')
            
        except Exception as exception:
            result = None
            logstring = f'{dt.now().strftime("%Y.%m.%d %H:%M:%S")} -> {string_logger} .. {exception.__class__.__name__}: {exception}'
            
        file = Path(path[0]) / 'data/function_calls.log'
        with open(file, 'a', encoding='utf-8') as file_content:
            print(logstring, file=file_content)
        
        return result
        
    return wrapper

# Декоратор logger работает формирует строку параметров не верно!!!

# Результаты вызова  
# >>> def div_round(num1, num2, digits=0):
# ...     return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>> div_round(5, 2)
# 2.0
# >>> div_round(5, 2, 1)
# 2.5
# >>> div_round(5, 0)
# >>> div_round(5)

# Записи журнала function_calls.log
# 2023.09.07 11:18:20 -> div_round(5, 2, digits=0) -> 2.0
# 2023.09.07 11:18:33 -> div_round(5, 2, 1, digits=0) -> 2.5
# 2023.09.07 11:20:23 -> div_round(5, 0, digits=0) .. ZeroDivisionError: division by zero
# 2023.09.07 11:20:29 -> div_round(5, digits=0) .. TypeError: div_round() missing 1 required positional argument: 'num2'