def orth_triangle(
        *,
        cathetus1: float = 0,
        cathetus2: float = 0,
        hypotenuse: float = 0
) -> float | None:
    """Функция вычисляет третью сторону прямоугольного треугольника по двум переданным."""

    if (
           cathetus1 and cathetus2 and hypotenuse
        or cathetus1 > hypotenuse and hypotenuse
        or cathetus2 > hypotenuse and hypotenuse
    ):
        return None
    else:
        if not cathetus1:
            return (hypotenuse**2 - cathetus2**2) ** 0.5
        if not cathetus2:
            return (hypotenuse**2 - cathetus1**2) ** 0.5
        if not hypotenuse:
            return (cathetus1**2 + cathetus2**2) ** 0.5


# >>> orth_triangle(cathetus2=3, hypotenuse=5)
# 4.0

# >>> orth_triangle(cathetus2=15, cathetus1=8)
# 17.0

# >>> print(orth_triangle(cathetus1=9, hypotenuse=3))
# None

# >>> orth_triangle(cathetus1=10, hypotenuse=25)
# 22.9128784747792

