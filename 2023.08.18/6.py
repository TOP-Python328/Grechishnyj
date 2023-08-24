def orth_triangle(
        *, 
        cathetus1: float = 0,
        cathetus2: float = 0,
        hipotenuse: float = 0
    ) -> float | None:
    """Функция вычисяет третью сторону прямоугольного треугольника по двум переданным"""
    
    if (cathetus1 and cathetus2 and hipotenuse
        or cathetus1 > hipotenuse and hipotenuse
        or cathetus2 > hipotenuse and hipotenuse):
        return None 
    else: 
        if not cathetus1:
            return (hipotenuse ** 2 - cathetus2 ** 2) ** 0.5
        if not cathetus2:
            return (hipotenuse ** 2 - cathetus1 ** 2) ** 0.5
        if not hipotenuse:
            return (cathetus1 ** 2 + cathetus2 ** 2) ** 0.5

# >>> orth_triangle(cathetus2=3, hipotenuse=5)
# 4.0

# >>> orth_triangle(cathetus2=15, cathetus1=8)
# 17.0

# >>> print(orth_triangle(cathetus1=9, hipotenuse=3))
# None

# >>> orth_triangle(cathetus1=10, hipotenuse=25)
# 22.9128784747792