def logger(func_obj: 'function') -> 'function':
    """Функция - декоратор, ведет журнал вызовов декорируемой функции"""
    
    def wrapper(*args, **kwargs):
        """Функция-обертка, вызывает декорируемую функцию"""
        
        kwargs_default = dict(zip(
            reversed(func_obj.__code__.co_varnames),
            # ИСПРАВИТЬ: у объекта функции есть два атрибута __defaults__ и __kwdefaults__ — если мы объявляем строго ключевые параметры, то их значения по умолчанию попадают только в __kwdefaults__; а если при этом в строго позиционных и позиционно-ключевых параметрах значений пол умолчанию нет, то в атрибуте __defaults__ будет записан объект None
            reversed(func_obj.__defaults__)
        ))
        # ИСПОЛЬЗОВАТЬ: объект dict_items может быть передан в встроенную функцию reversed() без преобразования
        kwargs_update = kwargs_default | dict(reversed(kwargs.items()))

        # ИСПОЛЬЗОВАТЬ: lambda функция избыточна
        args_position = tuple(map(str, args))
        args_keywords = tuple(map(
            lambda item: f'{item[0]}={item[1]}',
            reversed(kwargs_update.items())
        ))

        string_params = ', '.join((*args_position, *args_keywords))
        string_logger = f'{func_obj.__name__}({string_params})'
        
        try:
            result = func_obj(*args, **kwargs)
            print(f'{string_logger} -> {result}')
            return result
        except Exception as exception:
            # ИСПРАВИТЬ: журнал ведётся в stdout — отправьте сообщение туда
            # ИСПРАВИТЬ: при ошибке возвращайте None вместо result
            return f'{string_logger} .. {exception.__class__.__name__}: {exception}'

    return wrapper


# >>> def div_round(num1, num2, digits=0):
# ...     return round(num1 / num2, digits)
# ...

# >>> div_round(1, 3, digits=2)
# 0.33

# >>> div_round(7, 2)
# 4.0

# >>> div_round = logger(div_round)

# >>> div_round(7, 2)
# div_round(7, 2, digits=0) -> 4.0
# 4.0

# >>> div_round(7, 0)
# 'div_round(7, 0, digits=0) .. ZeroDivisionError: division by zero'

