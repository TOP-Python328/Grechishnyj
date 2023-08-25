def strong_password(password: str) -> bool:
    """Функция возвращает результат проверки пароля"""
    if len(password) < 8:
        return False
    else:
        cheker = {
            'lat_lower': 0,
            'lat_upper': 0,
            'punctuation': 0,
            'digits': 0
        }
    
    for char in password:
        symbol = ord(char)
        if symbol >= 65 and symbol <= 90:
            cheker['lat_upper'] += 1
        if symbol >= 97 and symbol <= 122:
            cheker['lat_lower'] += 1
        if char in ' ,./<>?;\':\"-_=+()[]*&^%$#@':
            cheker['punctuation'] +=1
        if char.isdigit():
            cheker['digits'] +=1
    
    if cheker['digits'] < 2:
        return False
        
    for value in cheker.values():
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