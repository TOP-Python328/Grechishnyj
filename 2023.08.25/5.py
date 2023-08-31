def logger(func_obj: 'function') -> 'function':
    """Функция - декоратор, ведет журнал вызовов декорируемой функции"""

    main_string = ''
    
    def wrapper(*args, **kwargs):
        """Функция-обертка, вызывает декорируемую функцию"""
        
        result = func_obj(*args, **kwargs)
        
        kwargs_default = dict(zip(reversed(func_obj.__code__.co_varnames),reversed(func_obj.__defaults__)))
        kwargs_update = kwargs_default | dict(reversed(tuple(kwargs.items())))

        args_position = tuple(map(lambda item: str(item), args))
        args_keywords = tuple(map(lambda item: f'{item[0]}={item[1]}', reversed(kwargs_update.items())))
        
        str_params = ', '.join((*args_position, *args_keywords))    
        log_string = f'{func_obj.__name__}({str_params}) -> {result}'
        print(log_string)
        return result
           
    return wrapper
    
    
# def test_func(n1: int, s2: int, n3: int, key: bool=False, key2: bool=False):
#     return round(n1 / s2, 3)
    
# print(test_func(55, 33, 44))

# test_func = logger(test_func)
# print(test_func(55, 21, 44))
# print(test_func(55, 21, 44, key=2))
# print(test_func(55, 21, 44, key=2, key2=2))
# print(test_func(55, 21, n3=44, key=2, key2=2))
# print(test_func(55, s2=21, n3=44, key=2, key2=2))
# print(test_func(n1=55, s2=21, n3=44, key=2, key2=2))

# >>> test_func(55, 21, 44)
# 2.619

# test_func = logger(test_func)

# >>> test_func(55, 21, 44)
# test_func(55, 21, 44, key=False, key2=False) -> 2.619
# 2.619
# >>> test_func(55, 21, 44, key=2)
# test_func(55, 21, 44, key=2, key2=False) -> 2.619
# 2.619
# >>> test_func(55, 21, 44, key=2, key2=2)
# test_func(55, 21, 44, key=2, key2=2) -> 2.619
# 2.619
# >>> test_func(55, 21, n3=44, key=2, key2=2)
# test_func(55, 21, n3=44, key=2, key2=2) -> 2.619
# 2.619
# >>> test_func(55, s2=21, n3=44, key=2, key2=2)
# test_func(55, s2=21, n3=44, key=2, key2=2) -> 2.619
# 2.619
# >>> test_func(n1=55, s2=21, n3=44, key=2, key2=2)
# test_func(n1=55, s2=21, n3=44, key=2, key2=2) -> 2.619
# 2.619
