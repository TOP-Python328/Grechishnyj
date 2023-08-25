def generate_system_dict() -> dict[str, int]:
    """
        Функция возвращает словарь соответсвия между числами в десятичной 
        системе счисления и цифрами в системах счисления большей разрядности
    """
    system_dict = {}
    for value in range(36):
        key = str(value if value < 10 else chr(value + 87))
        system_dict[key] = value
    return system_dict

system_dict = generate_system_dict()

def find_key(name_dict: dict, inp_value: int) -> int | None:
    """
        Функция осуществляет поиск и возвращает ключ элемента 
        по значению элемента
    """
    for key, value in name_dict.items():
        if value == inp_value:
            return key
    else:
        return None
  
def int_decimal(str_num: str, base: int) -> int | None:
    """
        Функция преобразовывает число из произвольной системы счисления
        в десятичную систему счисления 
    """
    reverse_num = str_num[::-1]
    decimal_num = 0
    power_num = 0
    for digit in reverse_num:
        decimal_num += system_dict[digit] * (base ** power_num)
        power_num += 1   
    return decimal_num

def int_instaled(num: int, base: int) -> str:
    """
        Функция преобразовывает число из десятичной системы счисления
        в произвольную систему счисления 
    """ 
    digit = '' 
    while num:
        digit += find_key(system_dict, num % base)
        num //= base
    return digit[::-1]

def int_base(number: str, start_base: int, end_base: int) -> str | None:
    """
        Функция преобразовывает число из произвольной системы счисления в произвольную
        Использует:
        def int_decimal - для преобразования произвольного числа в десятичную систему счисления
        def int_instaled - для преобразования десятичного числа в произвольную систему счисления
    """
    if start_base < 2 or start_base > 36 or end_base < 2 or end_base > 36:
        return None
    
    for char in number:
        if system_dict[char] > start_base:
            return None
    else:
        return int_instaled(int_decimal(number, start_base), end_base) 



# >>> int_base('ff00', 16, 2)
# '1111111100000000'

# >>> int_base('1101010', 2, 30)
# '3g'

# >>> int_base('110120120', 3, 10)
# '9168'

# >>> int_base('11012330120', 4, 10)
# '1339160'

# >>> int_base('1339160', 10, 4)
# '11012330120'

# >>> int_base('12af07d', 16, 10)
# '19591293'

# >>> int_base('19591293', 10, 16)
# '12af07d'

# >>> int_base('abcdef', 16, 16)
# 'abcdef'

# >>> print(int_base('0123456789ABCDEF', 1, 40))
# None

# >>> print(int_base('aaaaaa', 9, 10))
# None