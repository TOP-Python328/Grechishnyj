def logger(func_obj: 'function') -> 'function':
    """Функция - декоратор, ведет журнал вызовов декорируемой функции."""
    
    def wrapper(*args, **kwargs):
        """Функция-обёртка, вызывает декорируемую функцию."""
        kwargs_default = dict()
        if func_obj.__kwdefaults__:
            kwargs_default = dict(func_obj.__kwdefaults__) | dict(kwargs.items())
        # ИСПРАВИТЬ: разве не может быть значений по умолчанию одновременно у позиционных и ключевых параметров?
        if func_obj.__defaults__:
            kwargs_default = dict(zip(
                reversed(func_obj.__code__.co_varnames),
                reversed(func_obj.__defaults__)
            ))
        kwargs_update = kwargs_default | dict(kwargs.items())
        args_position = tuple(map(str, args))
        args_keywords = tuple(map(
            lambda item: f'{item[0]}={item[1]}',
            kwargs_update.items()
        ))
        string_params = ', '.join((*args_position, *args_keywords))
        string_logger = f'{func_obj.__name__}({string_params})'
        
        try:
            result = func_obj(*args, **kwargs)
            print(f'{string_logger} -> {result}')
            return result
        except Exception as exception:
            print(f'{string_logger} .. {exception.__class__.__name__}: {exception}')
            return None

    return wrapper


# >>> def div_round(num1, num2, *, digits=0, key=False):
# ...     return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>> div_round(7, 6, digits=3)
# div_round(7, 6, digits=3, key=False) -> 1.167
# 1.167
# >>> div_round(7, 6)
# div_round(7, 6, digits=0, key=False) -> 1.0
# 1.0

# >>> def div_round(num1, num2, digits=0, key=False):
# ...     return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>> div_round(7, 6, digits=3)
# div_round(7, 6, key=False, digits=3) -> 1.167
# 1.167
# >>> div_round(7, 0)
# div_round(7, 0, key=False, digits=0) .. ZeroDivisionError: division by zero
# >>> div_round(7)
# div_round(7, key=False, digits=0) .. TypeError: div_round() missing 1 required positional argument: 'num2'

# >>> def div_round(num1, num2):
# ...     return round(num1 / num2)
# ...
# >>> div_round = logger(div_round)
# >>> div_round(7, 6)
# div_round(7, 6) -> 1
# 1
# >>> div_round(7, 's')
# div_round(7, s) .. TypeError: unsupported operand type(s) for /: 'int' and 'str'

# КОММЕНТАРИЙ: мало сценариев объявления и вызова декорируемой функции рассмотрено

# СДЕЛАТЬ: изучите пример, запустите тестовые функции со своей реализацией декоратора, найдите ошибки


# ИТОГ: неплохо, но можно лучше — 4/7
