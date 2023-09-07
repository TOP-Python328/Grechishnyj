def strong_password(password: str) -> bool:
    """Функция возвращает результат проверки пароля."""
    if len(password) < 8:
        return False
    else:
        checkers = {
            'lat_lower': 0,
            'lat_upper': 0,
            'punctuation': 0,
            'digits': 0
        }
    for char in password:
        symbol = ord(char)
        # ИСПОЛЬЗОВАТЬ: представьте числовую ось, поместите на неё метки 65 и 90, теперь нанесите на ось отметку symbol для истинного условия — в каком порядке у вас окажутся подписи меток, в таком же порядке записывайте неравенства — так станет куда проще воспринимать условие целиком
        if 65 <= symbol and symbol <= 90:
            checkers['lat_upper'] += 1
        # ИСПОЛЬЗОВАТЬ: также в Python возможно конструировать цепочки сравнительных операторов, таким образом and оказывается не нужен
        if 97 <= symbol <= 122:
            checkers['lat_lower'] += 1
        if char in ' ,./<>?;\':\"-_=+()[]*&^%$#@':
            checkers['punctuation'] += 1
        if char.isdigit():
            checkers['digits'] += 1

    if checkers['digits'] < 2:
        return False

    for value in checkers.values():
        if not value:
            return False
    else:
        return True


# >>> strong_password('aP3:kD_l3')
# True

# >>> strong_password('password')
# False

# >>> strong_password('Йц3:шЩ_д3')
# False

# >>> strong_password('aP3:kD_')
# False

# >>> strong_password('Aa55+')
# False

# >>> strong_password('Aa55+...')
# True

# >>> strong_password()
# TypeError: strong_password() missing 1 required positional argument: 'password'

