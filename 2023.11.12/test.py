from random import sample, choice, randint
from datetime import date as dt
from data import HUMANS, KGPU
from university import Contact, Person, Employee, Teacher, Administrator, Student, Gratebook
from university import OrganizationLevel, Group, Auditorium, Faculty, Department, University, HR



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
    
    for key, value in KGPU.items():
        faculty = Faculty(key)
        faculty.head = rand_administrator()
        faculty.staff.append(faculty.head)
        faculty.contact = rand_contact()
        faculty.departments = list(Department(dep) for dep in KGPU[key])
        for dep in faculty.departments:
            dep.head = rand_administrator()
            dep.contact = rand_contact()
            dep.teachers = list(rand_teacher() for _ in range(10))
            for teacher in dep.teachers:
                teacher.contact = rand_contact()
            dep.auditoria = choice(create_auditoriums())
        university.facultets.append(faculty)


    return university
    
# >>> kgpu = create_university()
# >>>
# >>> kgpu.facultets
# [Инженерно-технологический факультет, Факультет естествознания, Факультет педагогики, Факультет психологии, Факультет искусств и социокультурного проектирования, Факультет лингвистики и мировых языков, Факультет филологии и массмедиа, Факультет истории и права, Медицинский факультет]
# >>>
# >>> kgpu.facultets[0].departments
# [Кафедра Инженерных и технологических дисциплин, Кафедра Информатики и информационных технологий, Кафедра Физики и математики, Кафедра Экономики и управления]
# >>>
# >>> kgpu.facultets[0].departments[0].teachers
# [Teacher Никифоров Н. id=1532026384720, Teacher Крюков Б. id=1532026387088, Teacher Гордеев А. id=1532026387792, Teacher Гордеев А. id=1532026387856, Teacher Ширяева В. id=1532026387920, Teacher Кабанов И. id=1532026387984, Teacher Артемьева Я. id=1532026388048, Teacher Меркушева А. id=1532026388112, Teacher Дорофеева Л. id=1532026388176, Teacher Степанова К. id=1532026384464]
# >>>
# >>> kgpu.facultets[0].departments[0].teachers[0].contact
# Contact(mobile='+79428076919', office='NotImplemented', email='jwegplf@mail.ru', web='www.nahojtgo.ru', telegram='@xfcw')
# >>>
# >>> kgpu.facultets[0].departments[0].auditoria
# Auditorium(number='129', seats=100, building=3)
# >>>
# >>> kgpu.facultets[0].departments[0].head
# Administrator Ширяева Я. id=1532023407632


# >>> for F in kgpu.facultets:
# ...     print(F.title)
# ...     print(F.contact)
# ...     print(F.head)
# ...     print(F.departments)
# ...     for D in F.departments:
# ...             print('\t', D.title)
# ...             print('\t', D.contact)
# ...             print('\t', D.head)
# ...             print('\t', D.auditoria)
# ...             print('\t', D.teachers)
# ...
# Инженерно-технологический факультет
# Contact(mobile='+79286686312', office='NotImplemented', email='dbntudpi@mail.ru', web='www.lrlgrivq.by', telegram='@geea')
# Administrator Назаров И. id=1532023305040
# [Кафедра Инженерных и технологических дисциплин, Кафедра Информатики и информационных технологий, Кафедра Физики и математики, Кафедра Экономики и управления]
         # Кафедра Инженерных и технологических дисциплин
         # Contact(mobile='+79333827691', office='NotImplemented', email='egkyamguvp@ya.ru', web='www.xyhdjih.by', telegram='@obfzx')
         # Administrator Ширяева Я. id=1532023407632
         # Auditorium(number='129', seats=100, building=3)
         # [Teacher Никифоров Н. id=1532026384720, Teacher Крюков Б. id=1532026387088, Teacher Гордеев А. id=1532026387792, Teacher Гордеев А. id=1532026387856, Teacher Ширяева В. id=1532026387920, Teacher Кабанов И. id=1532026387984, Teacher Артемьева Я. id=1532026388048, Teacher Меркушева А. id=1532026388112, Teacher Дорофеева Л. id=1532026388176, Teacher Степанова К. id=1532026384464]
         # Кафедра Информатики и информационных технологий
         # Contact(mobile='+79857158263', office='NotImplemented', email='rcekn@ya.ru', web='www.abyeiwns.ru', telegram='@hzxywg')
         # Administrator Третьякова Н. id=1532026440464
         # Auditorium(number='200', seats=30, building=3)
         # [Teacher Терентьев Р. id=1532026440976, Teacher Кузнецова А. id=1532026440912, Teacher Никифоров Н. id=1532026441168, Teacher Горбунов Р. id=1532026441104, Teacher Фролов Е. id=1532026441296, Teacher Зуева А. id=1532026441232, Teacher Кабанов И. id=1532026441424, Teacher Дорофеева П. id=1532026441360, Teacher Козлова Д. id=1532026441552, Teacher Силин Г. id=1532026440784]
         # Кафедра Физики и математики
         # Contact(mobile='+79064668782', office='NotImplemented', email='senps@ya.ru', web='www.vgmubf.ru', telegram='@idebp')
         # Administrator Михеева Г. id=1532026444560
         # Auditorium(number='111', seats=200, building=2)
         # [Teacher Сысоев Ф. id=1532026445136, Teacher Кулагин Г. id=1532026445392, Teacher Попов Ю. id=1532026445200, Teacher Смирнова К. id=1532026445520, Teacher Блинов В. id=1532026445328, Teacher Денисова М. id=1532026445648, Teacher Моисеев А. id=1532026445456, Teacher Гордеев А. id=1532026445776, Teacher Дьячков А. id=1532026445584, Teacher Захарова Ю. id=1532026445072]
         # Кафедра Экономики и управления
         # Contact(mobile='+79866744894', office='NotImplemented', email='uhdegoy@ya.ru', web='www.orppsmi.ru', telegram='@xptl')
         # Administrator Попов Ю. id=1532026448976
         # Auditorium(number='185', seats=100, building=3)
         # [Teacher Федорова М. id=1532026449424, Teacher Кудряшова А. id=1532026449680, Teacher Козлова П. id=1532026449616, Teacher Гущин В. id=1532026449808, Teacher Андреев А. id=1532026449744, Teacher Титова Л. id=1532026449936, Teacher Коновалова Ж. id=1532026449872, Teacher Захарова Ю. id=1532026450064, Teacher Авдеев С. id=1532026450000, Teacher Авдеев С. id=1532026449488]
# Факультет естествознания
# Contact(mobile='+79588105511', office='NotImplemented', email='patfyspkg@ya.ru', web='www.difogah.com', telegram='@bqreq')
# Administrator Харитонов М. id=1532026453456
# [Ботанический сад, Кафедра Биологии и экологии, Кафедра Географии и безопасности жизнедеятельности, Кафедра Химии]
         # Ботанический сад
         # Contact(mobile='+79669366310', office='NotImplemented', email='ooloiqhi@gmail.com', web='www.vfxdblrh.by', telegram='@ngowcuya')
         # Administrator Шестаков И. id=1532026454096
         # Auditorium(number='197', seats=200, building=1)
         # [Teacher Меркушев А. id=1532026454608, Teacher Марков Ф. id=1532026454736, Teacher Давыдова К. id=1532026454160, Teacher Захарова Ю. id=1532026454864, Teacher Козлов С. id=1532026454800, Teacher Козлов С. id=1532026454992, Teacher Марков Ф. id=1532026454928, Teacher Кулагин Г. id=1532026455120, Teacher Зуева А. id=1532026455056, Teacher Попов Ю. id=1532026454672]
         # Кафедра Биологии и экологии
         # Contact(mobile='+79589845302', office='NotImplemented', email='vmneexxlb@gmail.com', web='www.dzbvcl.com', telegram='@eidled')
         # Administrator Назаров И. id=1532026459024
         # Auditorium(number='129', seats=50, building=3)
         # [Teacher Михеева Г. id=1532026459536, Teacher Ширяева Я. id=1532026459216, Teacher Сысоев Ф. id=1532026459472, Teacher Данилов К. id=1532026459664, Teacher Шашков С. id=1532026459600, Teacher Блинов В. id=1532026459792, Teacher Молчанова Л. id=1532026459728, Teacher Федорова М. id=1532026459920, Teacher Молчанова Л. id=1532026459856, Teacher Архипов Р. id=1532026459088]
         # Кафедра Географии и безопасности жизнедеятельности
         # Contact(mobile='+79451262400', office='NotImplemented', email='szbvy@ya.ru', web='www.shpxytx.ru', telegram='@cpplmvau')
         # Administrator Шестаков И. id=1532026463248
         # Auditorium(number='114', seats=50, building=3)
         # [Teacher Шашкова Г. id=1532026463952, Teacher Рыбаков И. id=1532026464208, Teacher Цветкова А. id=1532026463888, Teacher Кулагин Г. id=1532026464336, Teacher Суворов В. id=1532026464016, Teacher Сысоев Ф. id=1532026464592, Teacher Дроздова В. id=1532026464144, Teacher Гущин В. id=1532026464720, Teacher Кудряшова А. id=1532026464272, Teacher Авдеев С. id=1532026463760]
         # Кафедра Химии
         # Contact(mobile='+79221677764', office='NotImplemented', email='ktqztocq@gmail.com', web='www.trpxjbq.by', telegram='@mab')
         # Administrator Никифоров Н. id=1532026468240
         # Auditorium(number='124', seats=100, building=2)
         # [Teacher Блинов В. id=1532026468752, Teacher Моисеев А. id=1532026468688, Teacher Кабанов И. id=1532026468944, Teacher Попов Ю. id=1532026468880, Teacher Рыбаков И. id=1532026469072, Teacher Сидоров К. id=1532026469008, Teacher Блинов В. id=1532026469200, Teacher Третьякова Н. id=1532026469136, Teacher Артемьева Я. id=1532026469328, Teacher Силин Г. id=1532026468560]
# Факультет педагогики
# Contact(mobile='+79637847609', office='NotImplemented', email='ujqasdwfm@mail.ru', web='www.kdkvv.com', telegram='@omsdicq')
# Administrator Анисимов Н. id=1532026489552
# [Кафедра Педагогики, Кафедра Теории и методики дошкольного, начального и специального образования]
         # Кафедра Педагогики
         # Contact(mobile='+79321094826', office='NotImplemented', email='rgwyiltq@gmail.com', web='www.btrcuret.com', telegram='@zuqnwwyc')
         # Administrator Колесникова С. id=1532026490128
         # Auditorium(number='134', seats=50, building=3)
         # [Teacher Федорова Л. id=1532026490512, Teacher Иванов А. id=1532026490704, Teacher Зуева А. id=1532026490640, Teacher Дорофеева П. id=1532026490768, Teacher Фролов Е. id=1532026490192, Teacher Дроздова В. id=1532026490896, Teacher Данилов К. id=1532026490832, Teacher Марков Ф. id=1532026491024, Teacher Соловьев Н. id=1532026490960, Teacher Крюков Б. id=1532026490576]
         # Кафедра Теории и методики дошкольного, начального и специального образования
         # Contact(mobile='+79280763421', office='NotImplemented', email='pfufpzo@gmail.com', web='www.npreq.com', telegram='@hfcax')
         # Administrator Алексеева С. id=1532026494672
         # Auditorium(number='173', seats=200, building=3)
         # [Teacher Блохина О. id=1532026495184, Teacher Крылов К. id=1532026494864, Teacher Куликов К. id=1532026495120, Teacher Коновалова Ж. id=1532026495312, Teacher Петухова А. id=1532026495248, Teacher Гущин Г. id=1532026495440, Teacher Шашков С. id=1532026495376, Teacher Денисова М. id=1532026495568, Teacher Никитин И. id=1532026495504, Teacher Сафонова М. id=1532026494736]
# Факультет психологии
# Contact(mobile='+79913776895', office='NotImplemented', email='bfqvapwjv@gmail.com', web='www.qikzu.ru', telegram='@cgqc')
# Administrator Степанова К. id=1532026499024
# [Кафедра Общей и социальной психологии, Кафедра Психологии развития и образования]
         # Кафедра Общей и социальной психологии
         # Contact(mobile='+79789920956', office='NotImplemented', email='kgsdxxvgy@gmail.com', web='www.zpakasp.com', telegram='@uzffjy')
         # Administrator Шестаков И. id=1532026499856
         # Auditorium(number='190', seats=50, building=3)
         # [Teacher Кузнецова А. id=1532026500176, Teacher Блохина О. id=1532026500368, Teacher Соколов И. id=1532026500496, Teacher Шашкова Г. id=1532026499664, Teacher Хохлова Е. id=1532026500624, Teacher Архипов Р. id=1532026500304, Teacher Кулагина А. id=1532026500752, Teacher Хохлова Е. id=1532026500432, Teacher Давыдова К. id=1532026500880, Teacher Хохлова Е. id=1532026500240]
         # Кафедра Психологии развития и образования
         # Contact(mobile='+79485576707', office='NotImplemented', email='qngmajp@ya.ru', web='www.brnyud.by', telegram='@hajx')
         # Administrator Меркушев А. id=1532026521040
         # Auditorium(number='176', seats=200, building=3)
         # [Teacher Соколов И. id=1532026521360, Teacher Захарова Ю. id=1532026521616, Teacher Колесникова С. id=1532026521680, Teacher Ширяева В. id=1532026521744, Teacher Ширяева Я. id=1532026521808, Teacher Денисова М. id=1532026521872, Teacher Некрасов М. id=1532026521936, Teacher Шашкова Г. id=1532026522000, Teacher Козлова Д. id=1532026522064, Teacher Ковалева Л. id=1532026521552]
# Факультет искусств и социокультурного проектирования
# Contact(mobile='+79844619905', office='NotImplemented', email='uytwudb@ya.ru', web='www.ehbhjnk.ru', telegram='@jst')
# Administrator Брагин А. id=1532026525712
# [Кафедра Искусств и социально-культурной деятельности, Кафедра Социальной адаптации и организации работы с молодежью, Кафедра Теории и методики физического воспитания, Кафедра Физического воспитания, Кафедра Философии, культурологии и социологии]
         # Кафедра Искусств и социально-культурной деятельности
         # Contact(mobile='+79606807642', office='NotImplemented', email='lnounrevi@gmail.com', web='www.gnvfaeuk.ru', telegram='@tawp')
         # Administrator Сысоев Ф. id=1532026526672
         # Auditorium(number='113', seats=50, building=1)
         # [Teacher Федорова Л. id=1532026527440, Teacher Щукин О. id=1532026527120, Teacher Артемьева Я. id=1532026527568, Teacher Анисимова В. id=1532026527248, Teacher Кузнецова А. id=1532026527696, Teacher Марков Ф. id=1532026527376, Teacher Крюков Б. id=1532026527824, Teacher Дорофеева П. id=1532026527504, Teacher Козлова П. id=1532026527952, Teacher Блинов В. id=1532026526992]
         # Кафедра Социальной адаптации и организации работы с молодежью
         # Contact(mobile='+79159467903', office='NotImplemented', email='nudajjdtmz@ya.ru', web='www.xzfucfua.ru', telegram='@bqt')
         # Administrator Дорофеева П. id=1532026531344
         # Auditorium(number='109', seats=30, building=2)
         # [Teacher Меркушева А. id=1532026531856, Teacher Сергеева Ю. id=1532026531536, Teacher Цветкова А. id=1532026531792, Teacher Соловьев Н. id=1532026531984, Teacher Шашков С. id=1532026531920, Teacher Лаврентьева В. id=1532026532112, Teacher Сорокина Г. id=1532026532048, Teacher Кошелев А. id=1532026532240, Teacher Марков Ф. id=1532026532176, Teacher Соловьев Н. id=1532026531408]
         # Кафедра Теории и методики физического воспитания
         # Contact(mobile='+79050255172', office='NotImplemented', email='jzmvm@mail.ru', web='www.ifxbykd.com', telegram='@nxo')
         # Administrator Давыдова К. id=1532026536144
         # Auditorium(number='195', seats=30, building=1)
         # [Teacher Куликов К. id=1532026536848, Teacher Данилов К. id=1532026537104, Teacher Дроздова В. id=1532026536784, Teacher Новикова М. id=1532026537232, Teacher Суворов В. id=1532026536912, Teacher Никитин И. id=1532026537360, Teacher Мясникова Л. id=1532026537040, Teacher Коновалова Ж. id=1532026537296, Teacher Анисимов Н. id=1532026536976, Teacher Щукин О. id=1532026536656]
         # Кафедра Физического воспитания
         # Contact(mobile='+79017789519', office='NotImplemented', email='gffmlk@gmail.com', web='www.hjzljqfc.by', telegram='@qyfvcyi')
         # Administrator Смирнова К. id=1532026540944
         # Auditorium(number='170', seats=100, building=2)
         # [Teacher Новикова М. id=1532026541456, Teacher Никифоров Н. id=1532026541392, Teacher Анисимов Н. id=1532026541648, Teacher Кошелев А. id=1532026541584, Teacher Козлова П. id=1532026541776, Teacher Лаврентьева В. id=1532026541712, Teacher Брагин А. id=1532026541904, Teacher Кулагин Г. id=1532026541840, Teacher Назаров И. id=1532026542032, Teacher Цветкова А. id=1532026541264]
         # Кафедра Философии, культурологии и социологии
         # Contact(mobile='+79356584660', office='NotImplemented', email='alqaj@mail.ru', web='www.hefkl.by', telegram='@zfyonc')
         # Administrator Шашкова Г. id=1532026545296
         # Auditorium(number='151', seats=30, building=3)
         # [Teacher Лаврентьева В. id=1532026546000, Teacher Дроздов М. id=1532026546256, Teacher Меркушев А. id=1532026545936, Teacher Шестаков И. id=1532026546384, Teacher Колесникова С. id=1532026546064, Teacher Дорофеева Л. id=1532026546512, Teacher Третьякова Н. id=1532026546192, Teacher Меркушева А. id=1532026546640, Teacher Меркушев А. id=1532026546320, Teacher Мясникова Л. id=1532026545808]
# Факультет лингвистики и мировых языков
# Contact(mobile='+79462792279', office='NotImplemented', email='xdmbl@mail.ru', web='www.mtwioalc.com', telegram='@bdfql')
# Administrator Меркушев А. id=1532026549968
# [Кафедра Английского языка, Кафедра Лингвистики и иностранных языков, Кафедра Теории языкознания и немецкого языка, Кафедра Французского языка]
         # Кафедра Английского языка
         # Contact(mobile='+79884054280', office='NotImplemented', email='qsklyhpoge@gmail.com', web='www.ogcydbzn.ru', telegram='@cvu')
         # Administrator Молчанова Л. id=1532026550736
         # Auditorium(number='176', seats=200, building=1)
         # [Teacher Третьякова В. id=1532026551440, Teacher Сергеева Ю. id=1532026551376, Teacher Коновалова Ж. id=1532026551568, Teacher Новикова М. id=1532026551504, Teacher Никифоров Н. id=1532026551696, Teacher Шашкова Г. id=1532026551632, Teacher Федорова М. id=1532026551824, Teacher Петухова А. id=1532026551760, Teacher Панфилова Ж. id=1532026551952, Teacher Титова Л. id=1532026551248]
         # Кафедра Лингвистики и иностранных языков
         # Contact(mobile='+79657284012', office='NotImplemented', email='varkugs@ya.ru', web='www.zbywf.com', telegram='@xbxa')
         # Administrator Щукин О. id=1532026571984
         # Auditorium(number='134', seats=200, building=1)
         # [Teacher Гордеев Д. id=1532026572432, Teacher Меркушев А. id=1532026572688, Teacher Ковалева Л. id=1532026572624, Teacher Федорова М. id=1532026572816, Teacher Кузнецов М. id=1532026572752, Teacher Козлова Д. id=1532026572944, Teacher Козлов С. id=1532026572880, Teacher Блинов В. id=1532026573200, Teacher Козлова Д. id=1532026573008, Teacher Анисимов Н. id=1532026572496]
         # Кафедра Теории языкознания и немецкого языка
         # Contact(mobile='+79071760399', office='NotImplemented', email='bhfcvh@mail.ru', web='www.qcopbj.com', telegram='@acxaojma')
         # Administrator Зуева А. id=1532026576720
         # Auditorium(number='109', seats=50, building=3)
         # [Teacher Анисимова В. id=1532026577168, Teacher Шашков С. id=1532026577424, Teacher Ширяева Я. id=1532026577360, Teacher Марков В. id=1532026577552, Teacher Моисеев А. id=1532026577488, Teacher Степанова К. id=1532026577680, Teacher Третьякова В. id=1532026577616, Teacher Иванов А. id=1532026577808, Teacher Горбунов Р. id=1532026577744, Teacher Козлова П. id=1532026577232]
         # Кафедра Французского языка
         # Contact(mobile='+79204454145', office='NotImplemented', email='bhuao@mail.ru', web='www.aodscf.ru', telegram='@ydqzg')
         # Administrator Назаров И. id=1532026581456
         # Auditorium(number='117', seats=100, building=3)
         # [Teacher Петухова А. id=1532026582032, Teacher Дроздова В. id=1532026582288, Teacher Попов Ю. id=1532026582224, Teacher Крылов К. id=1532026582416, Teacher Захарова Ю. id=1532026582352, Teacher Гордеев А. id=1532026582544, Teacher Суворов В. id=1532026582480, Teacher Михеева Г. id=1532026582736, Teacher Щукин О. id=1532026582160, Teacher Кулагина А. id=1532026582096]
# Факультет филологии и массмедиа
# Contact(mobile='+79520426659', office='NotImplemented', email='czxpugkwu@gmail.com', web='www.hkvlptg.by', telegram='@olr')
# Administrator Блохина О. id=1532026635472
# [Кафедра Литературы, Кафедра Русского языка, Кафедра Русского языка как иностранного]
         # Кафедра Литературы
         # Contact(mobile='+79625322514', office='NotImplemented', email='wgifbvg@ya.ru', web='www.okwdekx.by', telegram='@pal')
         # Administrator Суворов В. id=1532026635920
         # Auditorium(number='125', seats=100, building=1)
         # [Teacher Зуева А. id=1532026636688, Teacher Марков В. id=1532026636880, Teacher Кузнецова А. id=1532026636816, Teacher Цветкова А. id=1532026637008, Teacher Баранова А. id=1532026636944, Teacher Суворов В. id=1532026637136, Teacher Ширяева Я. id=1532026637072, Teacher Суворов В. id=1532026637264, Teacher Попов Ю. id=1532026637200, Teacher Авдеев С. id=1532026636752]
         # Кафедра Русского языка
         # Contact(mobile='+79258685214', office='NotImplemented', email='uzqgpfnks@mail.ru', web='www.lahdyta.by', telegram='@tor')
         # Administrator Некрасов М. id=1532026641104
         # Auditorium(number='116', seats=200, building=2)
         # [Teacher Третьякова Н. id=1532026641616, Teacher Назаров И. id=1532026641424, Teacher Крылов К. id=1532026641680, Teacher Третьякова Н. id=1532026641744, Teacher Сысоев Ф. id=1532026641808, Teacher Блохина О. id=1532026641872, Teacher Кабанов И. id=1532026641936, Teacher Новиков А. id=1532026642000, Teacher Ширяева Я. id=1532026642064, Teacher Дроздова В. id=1532026641296]
         # Кафедра Русского языка как иностранного
         # Contact(mobile='+79929844659', office='NotImplemented', email='iexsvepr@ya.ru', web='www.aqvrkdg.ru', telegram='@dluksgm')
         # Administrator Андреев А. id=1532026645840
         # Auditorium(number='189', seats=30, building=2)
         # [Teacher Козлова П. id=1532026646032, Teacher Кузнецова А. id=1532026646288, Teacher Шашков С. id=1532026646480, Teacher Козлова П. id=1532026646416, Teacher Федорова Л. id=1532026646608, Teacher Козлова П. id=1532026646544, Teacher Никифоров Н. id=1532026646736, Teacher Новикова М. id=1532026646672, Teacher Крылов К. id=1532026646864, Teacher Блинов В. id=1532026646352]
# Факультет истории и права
# Contact(mobile='+79756317283', office='NotImplemented', email='qrkfjwih@ya.ru', web='www.ghvpgs.com', telegram='@fskr')
# Administrator Меркушев А. id=1532026650512
# [Кафедра Истории, Кафедра Таможенного дела и логистики, Кафедра Юриспруденции]
         # Кафедра Истории
         # Contact(mobile='+79406787742', office='NotImplemented', email='uwifo@mail.ru', web='www.ctijruk.com', telegram='@mzyeo')
         # Administrator Некрасов М. id=1532026667408
         # Auditorium(number='172', seats=50, building=3)
         # [Teacher Некрасов М. id=1532026668368, Teacher Горбунов Р. id=1532026668048, Teacher Анисимов Н. id=1532026668496, Teacher Сафонова М. id=1532026668176, Teacher Кузнецова А. id=1532026668624, Teacher Цветкова А. id=1532026668304, Teacher Кузнецова А. id=1532026668752, Teacher Попов Ю. id=1532026668432, Teacher Третьякова Н. id=1532026668880, Teacher Дорофеева П. id=1532026667920]
         # Кафедра Таможенного дела и логистики
         # Contact(mobile='+79516791647', office='NotImplemented', email='zalmpx@mail.ru', web='www.elxrda.ru', telegram='@kcrin')
         # Administrator Щукин О. id=1532026672080
         # Auditorium(number='140', seats=30, building=3)
         # [Teacher Гущин В. id=1532026672784, Teacher Кузнецова А. id=1532026673040, Teacher Гущин Г. id=1532026672720, Teacher Архипов Р. id=1532026673168, Teacher Кулагина А. id=1532026672848, Teacher Новикова М. id=1532026673296, Teacher Харитонов М. id=1532026672976, Teacher Савельева Е. id=1532026673424, Teacher Шашкова Г. id=1532026673104, Teacher Кузнецова А. id=1532026672592]
         # Кафедра Юриспруденции
         # Contact(mobile='+79138586106', office='NotImplemented', email='btffaoquw@ya.ru', web='www.deqlx.by', telegram='@phxecs')
         # Administrator Петухова А. id=1532026676880
         # Auditorium(number='169', seats=100, building=2)
         # [Teacher Дьячков А. id=1532026677328, Teacher Сорокина Г. id=1532026677584, Teacher Ширяева Я. id=1532026677520, Teacher Архипов Р. id=1532026677712, Teacher Алексеева С. id=1532026677648, Teacher Молчанова Л. id=1532026677840, Teacher Алексеева С. id=1532026677776, Teacher Зуева А. id=1532026677968, Teacher Цветкова А. id=1532026677904, Teacher Зуева А. id=1532026677392]
# Медицинский факультет
# Contact(mobile='+79768942446', office='NotImplemented', email='etglupsbhf@ya.ru', web='www.nwgoqatp.com', telegram='@mxtmfoik')
# Administrator Гордеев Д. id=1532026681744
# [Кафедра Внутренних болезней, Кафедра Медико-биологических дисциплин, Кафедра Постдипломного образования - Eдиный аккредитационно-симуляционный центр подготовки медицинских работников, Кафедра Хирургии]
         # Кафедра Внутренних болезней
         # Contact(mobile='+79955850443', office='NotImplemented', email='hzqziknldv@gmail.com', web='www.ccnegyua.ru', telegram='@tswivsmw')
         # Administrator Куликов К. id=1532026682448
         # Auditorium(number='169', seats=200, building=2)
         # [Teacher Соколов И. id=1532026682704, Teacher Гордеев Д. id=1532026683152, Teacher Блинов В. id=1532026683344, Teacher Козлов С. id=1532026683280, Teacher Новиков А. id=1532026699856, Teacher Кабанов И. id=1532026699920, Teacher Гордеев А. id=1532026699984, Teacher Цветкова А. id=1532026700048, Teacher Никитин И. id=1532026700112, Teacher Колесникова С. id=1532026683024]
         # Кафедра Медико-биологических дисциплин
         # Contact(mobile='+79915263596', office='NotImplemented', email='ehnzmp@ya.ru', web='www.ixolu.ru', telegram='@ggkvhyrv')
         # Administrator Зуева А. id=1532026703760
         # Auditorium(number='141', seats=100, building=1)
         # [Teacher Колесникова С. id=1532026704208, Teacher Коновалова Ж. id=1532026704464, Teacher Сысоев Ф. id=1532026704400, Teacher Кузнецов М. id=1532026704592, Teacher Иванов А. id=1532026704528, Teacher Гордеев А. id=1532026704720, Teacher Сидоров К. id=1532026704656, Teacher Дорофеева Л. id=1532026704848, Teacher Кулагина А. id=1532026704784, Teacher Сорокина Г. id=1532026704272]
         # Кафедра Постдипломного образования - Eдиный аккредитационно-симуляционный центр подготовки медицинских работников
         # Contact(mobile='+79304871384', office='NotImplemented', email='mekteeguou@gmail.com', web='www.epbfknf.com', telegram='@vjowyvb')
         # Administrator Давыдова К. id=1532026708368
         # Auditorium(number='129', seats=50, building=2)
         # [Teacher Сидоров К. id=1532026708880, Teacher Анисимова В. id=1532026709072, Teacher Щукин О. id=1532026709328, Teacher Кузнецов М. id=1532026709008, Teacher Артемьева Я. id=1532026709456, Teacher Куликов К. id=1532026709136, Teacher Козлов С. id=1532026709584, Teacher Ширяева В. id=1532026709264, Teacher Горбунов Р. id=1532026709712, Teacher Захарова Ю. id=1532026708944]
         # Кафедра Хирургии
         # Contact(mobile='+79800373454', office='NotImplemented', email='zqpkcjlx@mail.ru', web='www.qrktgpfx.ru', telegram='@eljwi')
         # Administrator Некрасов М. id=1532026713232
         # Auditorium(number='126', seats=30, building=2)
         # [Teacher Суворов В. id=1532026713872, Teacher Третьякова В. id=1532026713808, Teacher Петухова А. id=1532026714064, Teacher Воронова П. id=1532026714000, Teacher Исаев Г. id=1532026714192, Teacher Кошелев А. id=1532026714128, Teacher Цветкова А. id=1532026714320, Teacher Фролов Е. id=1532026714256, Teacher Тимофеева Л. id=1532026714448, Teacher Колесникова С. id=1532026713552]
# >>>