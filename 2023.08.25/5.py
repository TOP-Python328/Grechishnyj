def logger(func_obj: 'function') -> 'function':
    """Функция - декоратор, ведет журнал вызовов декорируемой функции."""
    
    def wrapper(*args, **kwargs):
        """Функция-обёртка, вызывает декорируемую функцию."""

        # ИСПРАВИТЬ: у объекта функции есть два атрибута __defaults__ и __kwdefaults__ — если мы объявляем строго ключевые параметры, то их значения по умолчанию попадают только в __kwdefaults__; а если при этом в строго позиционных и позиционно-ключевых параметрах значений пол умолчанию нет, то в атрибуте __defaults__ будет записан объект None
        
        kwargs_default = dict()
        if func_obj.__kwdefaults__:
            kwargs_default = dict(func_obj.__kwdefaults__) | dict(kwargs.items())
            
        if func_obj.__defaults__:
            kwargs_default = dict(zip(
                reversed(func_obj.__code__.co_varnames),
                reversed(func_obj.__defaults__)
            ))
        
        # ИСПОЛЬЗОВАТЬ: объект dict_items может быть передан в встроенную функцию reversed() без преобразования
        kwargs_update = kwargs_default | dict(kwargs.items())

        # ИСПОЛЬЗОВАТЬ: lambda функция избыточна
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
            # ИСПРАВИТЬ: журнал ведётся в stdout — отправьте сообщение туда
            print(f'{string_logger} .. {exception.__class__.__name__}: {exception}')
            # ИСПРАВИТЬ: при ошибке возвращайте None вместо result
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