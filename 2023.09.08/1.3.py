from pathlib import Path
from sys import path
from random import choice, uniform
from typing import Literal
from datetime import date



# print(typing.Literal['мужской', 'женский'])


# Файлы хранения данных
ROOT_DIR = Path(path[0])
FIRST_NAMES = ROOT_DIR / 'first_names.txt'
LAST_NAMES = ROOT_DIR / 'last_names.txt'

# Перменные для аннотаций
Names = dict[str, list[str]]
Name = str
Patronymic = str
Surname = str
Gender = Literal['мужской', 'женский']
Birth = date
Mobile = str
Person = dict[Name, Patronymic, Surname, Gender, Birth, Mobile]

# Глобальное пространство имён
names: Names = {}


def load_data() -> None:
    """Функция создания словаря имен из файлов данных"""
    
    first_names = FIRST_NAMES.read_text(encoding='utf-8')
    last_names = LAST_NAMES.read_text(encoding='utf-8')
    
    first_names = first_names.strip().split('\n')
    last_names = last_names.strip().split('!')
    
    names['мужской'] = first_names[1].split('!')
    names['женский'] = first_names[0].split('!')
    names['фамилия'] = last_names
    return None
    


    
    
def generate_person() -> Person:
    """Вспомогательная функция генерирует анкету человека со случаными данными"""
    person: Person = {}
    pointer = choice(('мужской', 'женский'))
    person['имя']: Name = choice(names[pointer])
    
    def get_patronymic(pointer) -> Patronymic:
        """Функция преобразует мужское имя в отчество"""
        patronymic = choice(names['мужской'])
        start = patronymic[:-2]
        end = patronymic[-2:]
        if pointer == 'женский':
            if end == 'ей':
                end = 'евна'
            elif end == 'ий':
                end = 'ьевна'
            elif end == 'ел':
                end = 'ловна'
            else:
                end = 'овна'
                return f'{patronymic}{end}'
            return f'{start}{end}'
        else:
            if end == 'ей':
                end = 'евич'
            elif end == 'ий':
                end = 'ьевич'
            elif end == 'ел':
                end = 'лович'
            else:
                end = 'ович'
                return f'{patronymic}{end}'
            return f'{start}{end}'
            
    def get_surname(pointer) -> Surname:
        """Вспомогательная функция возвращает женскую фамилию"""
        last_name = choice(names['фамилия'])
        start = last_name[:-2]
        end = last_name[-2:]
        if pointer == 'женский':
            if end in ('ий', 'ый'):
                end = 'ая'
                return f'{start}{end}'
            else:
                end = 'а'
                return f'{last_name}{end}'
            return f'{start}{end}'
        else:
            return last_name
    
    
    def get_rand_date() -> Birth:
        """Вспомогательная функция генерации даты"""
        lg_month = [1, 3, 5, 7, 8, 10, 12]
        sm_montn = [4, 6, 9, 11]
        year = int(uniform(1925, 2025))
        month = int(uniform(1, 13))
        if month == 2:
            day = uniform(1, 30) if year // 4 == 0 else int(uniform(1, 29))
        elif month in lg_month:
            day = uniform(1, 32)
        elif month in sm_montn:
            day = uniform(1, 31)
        day = int(day)    
        return date(year, month, day)
        
    def get_mobile() -> Mobile:
        """Вспомогательная функция генерации номера телефона"""
        mobile = '+79'
        for _ in range(9):
            mobile += str(int(uniform(0, 10)))
        return mobile
        
    person['отчество']: Patronymic = get_patronymic(pointer)
    person['фамилия']: Surname = get_surname(pointer)
    person['пол']: Gender = pointer
    person['дата рождения']: Birth = get_rand_date()
    person['мобильный']: Mobile = get_mobile()
    
    return person
    

# if __name__ == '__main__':
    # load_data()
    # generate_person()
    
    

 # 17:29:11 > python -i 2023.09.08\1.3.py
# >>> from pprint import pprint
# >>>
# >>> load_data()
# >>>
# >>> person = generate_person()
# >>> pprint(person)
# {'дата рождения': datetime.date(1946, 5, 23),
 # 'имя': 'Ростислав',
 # 'мобильный': '+79287029220',
 # 'отчество': 'Ахмедович',
 # 'пол': 'мужской',
 # 'фамилия': 'Калугин'}
# >>>
# >>> person = generate_person()
# >>> pprint(person)
# {'дата рождения': datetime.date(1961, 2, 19),
 # 'имя': 'Феодосия',
 # 'мобильный': '+79164256676',
 # 'отчество': 'Филипповна',
 # 'пол': 'женский',
 # 'фамилия': 'Судакова'}
# >>>
# >>> person = generate_person()
# >>> pprint(person)
# {'дата рождения': datetime.date(2014, 8, 23),
 # 'имя': 'Панкрат',
 # 'мобильный': '+79210926755',
 # 'отчество': 'Романович',
 # 'пол': 'мужской',
 # 'фамилия': 'Федосов'}
# >>>
# >>> person = generate_person()
# >>> pprint(person)
# {'дата рождения': datetime.date(1971, 10, 8),
 # 'имя': 'Татьяна',
 # 'мобильный': '+79260236994',
 # 'отчество': 'Касьяновна',
 # 'пол': 'женский',
 # 'фамилия': 'Булгакова'}
# >>>
# >>> person = generate_person()
# >>> pprint(person)
# {'дата рождения': datetime.date(2001, 1, 4),
 # 'имя': 'Аарон',
 # 'мобильный': '+79237577279',
 # 'отчество': 'Азатович',
 # 'пол': 'мужской',
 # 'фамилия': 'Серов'}
# >>>
# >>> person = generate_person()
# >>> pprint(person)
# {'дата рождения': datetime.date(1972, 6, 23),
 # 'имя': 'Лилия',
 # 'мобильный': '+79130475955',
 # 'отчество': 'Августовна',
 # 'пол': 'женский',
 # 'фамилия': 'Леонова'}
# >>>
# >>> person = generate_person()
# >>> pprint(person)
# {'дата рождения': datetime.date(1951, 2, 9),
 # 'имя': 'Ливия',
 # 'мобильный': '+79775885447',
 # 'отчество': 'Ипполитовна',
 # 'пол': 'женский',
 # 'фамилия': 'Злобина'}
# >>>    
    
    
    
    


    

