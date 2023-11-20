from random import sample, choice, randint
from datetime import date as dt
from data import HUMANS, KGPU
from university import Contact, Person, Employee, Teacher, Administrator, Student, Gratebook
from university import OrganizationLevel, Group, Auditorium, Faculty, Department, University



def rand_contact() -> Contact:  
    """Функция генерирует экземпляр класса Contact - случайная генерация"""
    
    digits = '0123456789'
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    
    mobile = f"+79{''.join(choice(digits) for _ in range(9))}"
    office = f"NotImplemented"
    email = f"{''.join(choice(letters) for _ in range(randint(5, 10)))}@{choice(['mail.ru', 'ya.ru', 'gmail.com'])}"
    web = f"www.{''.join(choice(letters) for _ in range(randint(5, 8)))}.{choice(['ru', 'com', 'by'])}"
    telegram = f"@{''.join(choice(letters) for _ in range(randint(3, 8)))}"
    
    return Contact(mobile, office, email, web, telegram)
    

# >>> contact = rand_contact()
# >>> contact
# Contact(mobile='+79376746870', office='NotImplemented', email='dhempm@ya.ru', web='www.gaxszzr.ru', telegram='@haygn')
# >>> contact.__dict__
# {'mobile': '+79376746870', 'office': 'NotImplemented', 'email': 'dhempm@ya.ru', 'web': 'www.gaxszzr.ru', 'telegram': '@haygn'}


def rand_person() -> Person:
    """Функция генерирует экземпляр класса Person"""
    
    full_name = choice(HUMANS).split(' ')
    birthdate = dt(randint(1975, 2005), randint(1, 12), randint(1, 28))
    return Person(*full_name, birthdate)


# >>> person = rand_person()
# >>> person.__dict__
# {'last_name': 'Гущин', 'first_name': 'Георгий', 'patr_name': 'Никитович', 'birthdate': datetime.date(1988, 8, 26), 'contact': <class 'university.Contact'>}
# >>> print(person.contact.mobile)
# None
# >>> person.contact = rand_contact()
# >>> person.contact.mobile
# '+79850531732'
# >>> person.contact.__dict__
# {'mobile': '+79850531732', 'office': 'NotImplemented', 'email': 'malnx@ya.ru', 'web': 'www.ftpbm.com', 'telegram': '@tgkgqmw'}


def rand_student() -> Student:
    """Функция генерирует экземпляр класса Student"""
    
    full_name = choice(HUMANS).split(' ')
    birthdate = dt(randint(2000, 2005), randint(1, 12), randint(1, 28))
    return Student(*full_name, birthdate)


# >>> student = rand_student()
# >>> student.contact = rand_contact()
# >>> student.contact.__dict__
# {'mobile': '+79456917674', 'office': 'NotImplemented', 'email': 'yvhtmwe@ya.ru', 'web': 'www.cwstdzd.ru', 'telegram': '@gbdfztt'}
# >>> print(*list(attr for attr in student.__dict__.items()), sep='\n')
# ('last_name', 'Силин')
# ('first_name', 'Георгий')
# ('patr_name', 'Викторович')
# ('birthdate', datetime.date(1980, 7, 9))
# ('contact', Contact(mobile='+79456917674', office='NotImplemented', email='yvhtmwe@ya.ru', web='www.cwstdzd.ru', telegram='@gbdfztt'))
# ('id_', '2670958637840')
# ('form', очная)
# ('contract', бюджетный)
# ('semester', 1)
# ('gradebook', {})
# ('_stipendia', 1)


def rand_teacher() -> Teacher:
    """Функция генерирует экземпляр класса Teacher"""
    
    full_name = choice(HUMANS).split(' ')
    birthdate = dt(randint(1975, 1995), randint(1, 12), randint(1, 28))
    return Teacher(*full_name, birthdate)
    
    
# >>> teacher = rand_teacher()
# >>> print(*list(attr for attr in teacher.__dict__.items()), sep='\n')
# ('last_name', 'Колесникова')
# ('first_name', 'София')
# ('patr_name', 'Олеговна')
# ('birthdate', datetime.date(1991, 9, 5))
# ('contact', <class 'university.Contact'>)
# ('position', None)
# ('income', 1)
# ('courses', [])
# ('degree', кандидат)
# ('professor', False)
# >>> teacher.contact = rand_contact()
# >>> teacher.courses.append('Python')
# >>> teacher.courses.append('SQL')
# >>> teacher.courses
# ['Python', 'SQL']
# >>> teacher.position = 'Преподаватель'
# >>> teacher.position
# 'Преподаватель'
# >>> teacher.contact.telegram
# '@qkeonjzu'


def rand_administrator() -> Administrator:
    """Функция генерирует экземпляр класса Administrator"""
    
    full_name = choice(HUMANS).split(' ')
    birthdate = dt(randint(1975, 1995), randint(1, 12), randint(1, 28))
    return Administrator(*full_name, birthdate)


# >>> admin = rand_administrator()
# >>> admin.contact = rand_contact()
# >>> admin.position = 'администратор'
# >>> admin.income = 2
# >>> admin.subordinates = [rand_person() for _ in range(5)]
# >>> print(*list(attr for attr in admin.__dict__.items()), sep='\n')
# ('last_name', 'Хохлова')
# ('first_name', 'Елизавета')
# ('patr_name', 'Валерьевна')
# ('birthdate', datetime.date(1981, 7, 12))
# ('contact', Contact(mobile='+79656508775', office='NotImplemented', email='wgymn@ya.ru', web='www.bjlojfr.ru', telegram='@dcid'))
# ('position', 'администратор')
# ('income', 2)
# ('head', None)
# ('subordinates', [Person Воронова А. id=2302297603728, Person Меркушева А. id=2302297601872, Person Лаврентьева В. id=2302297601424, Person Горбунов Р. id=2302297600080, Person Новикова М. id=2302297601680])


def rand_group() -> Group[Student]:
    """Функция создает группу 15-ти студентов"""
    group = Group()
    group += (rand_student() for _ in range(15))
    group.chief = choice(group)
    return group
    
    
# >>> group = rand_group()
# >>> print(*list(attr for attr in group.__dict__.items()), sep='\n')
# ('id_', '1970635401376')
# ('chief', Student Панфилова Ж. id=1970635109008)
# ('curator', None)
# >>> group.curator = rand_teacher()
# >>> print(*list(attr for attr in group.__dict__.items()), sep='\n')
# ('id_', '1970635401376')
# ('chief', Student Панфилова Ж. id=1970635109008)
# ('curator', Teacher Кулагин Г. id=1970632032400)
# >>> group
# [Student Панфилова Ж. id=1970635109008, Student Ширяева Я. id=1970635108816, Student Иванов А. id=1970638159120, Student Анисимов Н. id=1970638159376, Student Марков Ф. id=1970638159760, Student Козлов С. id=1970638159568, Student Баранова А. id=1970638242768, Student Сидоров К. id=1970638243280, Student Сергеева Ю. id=1970638243472, Student Панфилова Ж. id=1970635108688, Student Некрасов М. id=1970638243792, Student Суворов В. id=1970638243984, Student Сысоев Ф. id=1970638244176, Student Новикова М. id=1970638244368, Student Цветкова М. id=1970638244560]  
    
  
def create_auditoriums() -> list[Auditorium]:
    """Функция возвращает список аудиторий"""
    auditoriums = []
    
    for number in range(101, 201):
        number = str(number)
        seats =  choice([30, 50, 100, 200])
        building = choice([1, 2, 3])
        auditoriums.append(Auditorium(number, seats, building))

    return auditoriums

    
# >>> auditoriums = create_auditoriums()
# >>> print(*(auditorium for auditorium in auditoriums), sep='\n')
# Auditorium(number='101', seats=200, building=3)
# Auditorium(number='102', seats=30, building=1)
# Auditorium(number='103', seats=100, building=3)
# ...
# Auditorium(number='198', seats=30, building=3)
# Auditorium(number='199', seats=100, building=3)
# Auditorium(number='200', seats=200, building=1)


def create_university() -> University[Faculty[Department]]:
    """Функция возвращает экземпляр класса University"""
    # Из заранее подготовленого словаря создаются факультеты и кафедры
    
    university = University('КГПУ им. К.Э. Циолковкого')
    
    for key, values in KGPU.items():
        faculty = Faculty(key)
        for department in KGPU[faculty.title]:
            faculty.append(Department(department))
        university.append(faculty)

    return university
    
# >>> university_kgpu = create_university()
# >>> university_kgpu
# [[[], [], [], []], [[], [], [], []], [[], []], [[], []], [[], [], [], [], []], [[], [], [], []], [[], [], []], [[], [], []], [[], [], [], []]]
# >>>
# >>>
# >>>
# >>> for faculty in university_kgpu:
# ...     print(faculty.title)
# ...     for department in faculty:
# ...             print(f'\t{department.title}')
# ...
# Инженерно-технологический факультет
        # Кафедра Инженерных и технологических дисциплин
        # Кафедра Информатики и информационных технологий
        # Кафедра Физики и математики
        # Кафедра Экономики и управления
# Факультет естествознания
        # Ботанический сад
        # Кафедра Биологии и экологии
        # Кафедра Географии и безопасности жизнедеятельности
        # Кафедра Химии
# Факультет педагогики
        # Кафедра Педагогики
        # Кафедра Теории и методики дошкольного, начального и специального образования
# Факультет психологии
        # Кафедра Общей и социальной психологии
        # Кафедра Психологии развития и образования
# Факультет искусств и социокультурного проектирования
        # Кафедра Искусств и социально-культурной деятельности
        # Кафедра Социальной адаптации и организации работы с молодежью
        # Кафедра Теории и методики физического воспитания
        # Кафедра Физического воспитания
        # Кафедра Философии, культурологии и социологии
# Факультет лингвистики и мировых языков
        # Кафедра Английского языка
        # Кафедра Лингвистики и иностранных языков
        # Кафедра Теории языкознания и немецкого языка
        # Кафедра Французского языка
# Факультет филологии и массмедиа
        # Кафедра Литературы
        # Кафедра Русского языка
        # Кафедра Русского языка как иностранного
# Факультет истории и права
        # Кафедра Истории
        # Кафедра Таможенного дела и логистики
        # Кафедра Юриспруденции
# Медицинский факультет
        # Кафедра Внутренних болезней
        # Кафедра Медико-биологических дисциплин
        # Кафедра Постдипломного образования - Eдиный аккредитационно-симуляционный центр подготовки медицинских работников
        # Кафедра Хирургии  
