def repeat(num) -> 'function':
    """Функция выполняет заданную функцию n-ное число раз"""
    def decorator(func_obj: 'function') -> 'function':
        """Функция-декоратор"""
        def wrapper(*args, **kwargs):
            for n in range(num):
                func_obj(*args, **kwargs)
        return wrapper
    return decorator
    
    
# 17:22:10 > python -i 2023.08.25/4.py

# >>> @repeat(5)
# ... def print_hi(s):
# ...     print(s)
# ...
# >>> print_hi('Hi World!')
# Hi World!
# Hi World!
# Hi World!
# Hi World!
# Hi World!
# >>>
# >>> @repeat(8)
# ... def print_hi(s):
# ...     print(s)
# ...
# >>> print_hi('Python decorators!')
# Python decorators!
# Python decorators!
# Python decorators!
# Python decorators!
# Python decorators!
# Python decorators!
# Python decorators!
# Python decorators!