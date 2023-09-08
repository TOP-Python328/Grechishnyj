def logger(func_obj: 'function') -> 'function':
    """Функция - декоратор, ведет журнал вызовов декорируемой функции."""
    
    def wrapper(*args, **kwargs):
        """Функция-обёртка, вызывает декорируемую функцию."""

        # УДАЛЕНО: вычисление переменной kwargs_default
        # kwargs_default = dict(zip(
            # reversed(func_obj.__code__.co_varnames),
            # ИСПРАВИТЬ: у объекта функции есть два атрибута __defaults__ и __kwdefaults__ — если мы объявляем строго ключевые параметры, то их значения по умолчанию попадают только в __kwdefaults__; а если при этом в строго позиционных и позиционно-ключевых параметрах значений пол умолчанию нет, то в атрибуте __defaults__ будет записан объект None
            #reversed(func_obj.__kwdefaults__)
        # ))
        
        # ИСПОЛЬЗОВАТЬ: объект dict_items может быть передан в встроенную функцию reversed() без преобразования
        kwargs_update = func_obj.__kwdefaults__ | dict(kwargs.items())

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
# >>> div_round(7, 6, digits=5)
# div_round(7, 6, digits=5, key=False) -> 1.16667
# 1.16667
# >>> div_round(7, 6, digits=1, key=True)
# div_round(7, 6, digits=1, key=True) -> 1.2
# 1.2
# >>> div_round(7, 6)
# div_round(7, 6, digits=0, key=False) -> 1.0
# 1.0
# >>> div_round(7, 0)
# div_round(7, 0, digits=0, key=False) .. ZeroDivisionError: division by zero
# >>> div_round(7)
# div_round(7, digits=0, key=False) .. TypeError: div_round() missing 1 required positional argument: 'num2'
# >>>