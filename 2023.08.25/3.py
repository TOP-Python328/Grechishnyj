def math_function_resolver(
        math_func: 'function', 
        /, 
        x_main: int | float, 
        *x_args: int | float, 
        # *, - получаем ошибку SyntaxError: * argument may appear only once
        strings: bool=False
    ) -> list[float | str]:
    """
        Функция вычисляет округленные значения для различных математических функций
        Принимает аргументы:
            math_func - обязательный, функция, которая производит математические вычисления
            x_main - обязательный, аргумент для функции math_func
            x_args - не обязательный, аргумент для функции math_func
            strings - не обязательный, устанавливает тип элементов в возвращаемом списке
        Возвращает:
            объект типа list - список значений, результатов вычислений math_func
    """
    results = []
    
    x_args = x_main, *x_args
    
    for x in x_args:
        res = round(math_func(x), 2)
        results.append(str(res) if strings else res)
    
    return results 

# >>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
# [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5]

# >>> math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10))
# [1.5, 1.0, 0.5, 0.0, -0.5, -1.0, -1.5, -2.0, -2.5]

# >>> math_function_resolver(lambda x: 2.72**x, *range(1, 10), strings=True)
# ['2.72', '7.4', '20.12', '54.74', '148.88', '404.96', '1101.49', '2996.07', '8149.3']    