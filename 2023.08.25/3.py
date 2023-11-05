def math_function_resolver(
        math_func: 'function',
        /,
        # ИСПОЛЬЗОВАТЬ: для аннотации и целых, и вещественных чисел достаточно float
        x_main: float,
        *x_args: float,
        strings: bool = False
) -> list[float | str]:
    # ИСПОЛЬЗОВАТЬ: разметку reStructuredText в строках документации
    """Функция вычисляет округленные значения для различных математических функций

    :param math_func: функция, которая производит математические вычисления
    :param x_main: аргумент для функции math_func
    :param x_args: аргументы для функции math_func
    :param strings: устанавливает тип элементов в возвращаемом списке
    :return: список значений, результатов вычислений math_func
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


# ИТОГ: хорошо, но можно лучше — 2/3
