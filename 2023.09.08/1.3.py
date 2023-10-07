from pathlib import Path
from sys import path
from random import choice, randrange
from typing import Literal
from datetime import date


# Файлы хранения данных
ROOT_DIR = Path(path[0])
NAMES = ROOT_DIR / 'names.txt'
PATRONYMICS = ROOT_DIR / 'patronymics.txt'
SURNAMES = ROOT_DIR / 'surnames.txt'

# Перменные для аннотаций
DictGenders = dict[str, [list[str]]]
Names = dict[DictGenders]
Name = str
Patronymic = str
Surname = str
Gender = Literal['мужской', 'женский']
Birth = date
Mobile = str
Person = dict[Name, Patronymic, Surname, Gender, Birth, Mobile]

# Глобальное пространство имён
names_db: Names = {}
TOKENS = ('мужской', 'женский')

# Структура файлов
# мужской:Иван!Перт!Алексей...\nженский:Ольга!Наталья!...!Яна


def generate_gender(data_file_text: str) -> DictGenders:
    """Вспомогательная функция генерирует словарь с ключами мужской или женский"""
    data_file_text = data_file_text.strip().split('\n')
    dict_gender: DictGenders = {}
    for text_line in data_file_text:
        text_line = text_line.split(':')
        dict_gender[text_line[0]] = text_line[1].split('!')
    return dict_gender

    
def get_rand_date() -> Birth:
    """Вспомогательная функция генерации даты"""
    large_month: list[int] = [1, 3, 5, 7, 8, 10, 12]
    small_montn: list[int] = [4, 6, 9, 11]
    year: int = randrange(1920, 2020)
    month: int = randrange(1, 13)
    day: int = None
    if month == 2:
        day = randrange(1, 30) if year // 4 == 0 else randrange(1, 29)
    elif month in large_month:
        day = randrange(1, 32)
    elif month in small_montn:
        day = randrange(1, 31)
    return date(year, month, day)

    
def get_mobile() -> Mobile:
    """Вспомогательная функция генерации номера телефона"""
    mobile: Mobile = '+79'
    for _ in range(9):
        mobile += str(randrange(0, 10))
    return mobile


def load_data() -> None:
    """Функция создания словаря из файлов данных"""
    names: DictGenders = NAMES.read_text(encoding='utf-8')
    patronymics: DictGenders = PATRONYMICS.read_text(encoding='utf-8')
    surnames: DictGenders = SURNAMES.read_text(encoding='utf-8')  
    names_db['имена'] = generate_gender(names)
    names_db['отчества'] = generate_gender(patronymics)
    names_db['фамилии'] = generate_gender(surnames)
 
    
def generate_person() -> Person:
    """Функция генерирует анкету человека со случаными данными"""
    person: Person = {}
    pointer: str = choice(TOKENS)
    person['имя']: Name = choice(names_db['имена'][pointer])
    person['отчество']: Patronymic = choice(names_db['отчества'][pointer])
    person['фамилия']: Surname = choice(names_db['фамилии'][pointer])
    person['пол']: Gender = pointer
    person['дата рождения']: Birth = get_rand_date()
    person['мобильный']: Mobile = get_mobile()
    return person


# 12:00:24 > python -i 2023.09.08\1.3.py
# >>> from pprint import pprint
# >>> load_data()
# >>> for _ in range(7):
# ...     pprint(generate_person(), sort_dicts=False)
# ...
# {'имя': 'Клавдия',
 # 'отчество': 'Леонидовна',
 # 'фамилия': 'Швецова',
 # 'пол': 'женский',
 # 'дата рождения': datetime.date(2006, 11, 2),
 # 'мобильный': '+79837320367'}
# {'имя': 'Самуил',
 # 'отчество': 'Аксёнович',
 # 'фамилия': 'Корольков',
 # 'пол': 'мужской',
 # 'дата рождения': datetime.date(1952, 8, 18),
 # 'мобильный': '+79294197577'}
# {'имя': 'Алина',
 # 'отчество': 'Павловна',
 # 'фамилия': 'Гончарова',
 # 'пол': 'женский',
 # 'дата рождения': datetime.date(1948, 5, 18),
 # 'мобильный': '+79378551140'}
# {'имя': 'Леон',
 # 'отчество': 'Каллистратович',
 # 'фамилия': 'Гончаров',
 # 'пол': 'мужской',
 # 'дата рождения': datetime.date(1932, 12, 2),
 # 'мобильный': '+79203899507'}
# {'имя': 'Иоанна',
 # 'отчество': 'Никодимовна',
 # 'фамилия': 'Яковлева',
 # 'пол': 'женский',
 # 'дата рождения': datetime.date(1995, 5, 21),
 # 'мобильный': '+79623107685'}
# {'имя': 'Динара',
 # 'отчество': 'Яковлевна',
 # 'фамилия': 'Новодворская',
 # 'пол': 'женский',
 # 'дата рождения': datetime.date(2019, 12, 14),
 # 'мобильный': '+79192665326'}
# {'имя': 'Алиса',
 # 'отчество': 'Ильгизовна',
 # 'фамилия': 'Макеева',
 # 'пол': 'женский',
 # 'дата рождения': datetime.date(1973, 1, 4),
 # 'мобильный': '+79111737099'}