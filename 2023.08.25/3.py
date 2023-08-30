def math_function_resolver(
        math_func: 'function', 
        /, 
        x_main: int | float, 
        *x_args: int | float,
        *,
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