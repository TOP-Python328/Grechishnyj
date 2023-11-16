from typing import Callable

from random import sample, choice

from data import random_humans, random_lessons_school, random_admins, data_structure_kgpu

from university import University, Administrator, HR, Faculty, Department, Contact, Person, Employee, Teacher, Administrator, Student, Auditorium

# class Contact:
# class Person:     
# class Employee(Person):
# class Teacher(Employee):
    # class Degree(Enum):
# class Administrator(Employee):
# class Gratebook(dict):
    # class GrateRecord:
        # class ExamType(Enum):
# class Student(Person):
    # class EducationForm(Enum):
    # class ContractForm(Enum):

# class OrganizationLevel(list):
# class Group(list):
# class Auditorium(Enum):
# class Department(OrganizationLevel):
# class Faculty(OrganizationLevel):
# class HR(OrganizationLevel):
# class University(OrganizationLevel):



# Students - генерируем из списка random_humans - экземпляры класса Student 
def generate_students(humans: list[str], count: int = 10) -> list[Student]:
    """Функция генерирует список экземпляров класса Student"""
    humans = list(sample(humans, count))
    students = list(Student(*human.split()) for human in humans)
    return students
  
# >>> students = generate_students(random_humans, 5)
# >>> print(*students, sep='\n')
# Student Федорова id=2875748400784
# Student Фролов id=2875748386640
# Student Попов id=2875748392656
# Student Третьякова id=2875748386832
# Student Дорофеева id=2875748390928
# >>> 
# >>> fedorova = students[0]
# >>> print(*list(attr for attr in fedorova.__dict__.items()), sep='\n')
# ('last_name', 'Федорова')
# ('first_name', 'Маргарита')
# ('patr_name', 'Эдуардовна')
# ('birthdate', None)
# ('contacts', <class 'university.Contact'>)
# ('id_', '2875748400784')
# ('form', очная)
# ('contract', бюджетный)
# ('semester', 1)
# ('gradebook', {})
# ('_stipendia', 0)

# Teachers - генерируем из списка random_humans - экземпляры класса Teacher 
def generate_teachers(humans: list[str], count: int = 10) -> list[Teacher]:
    """Функция генерирует список экземпляров класса Teachers"""
    humans = list(sample(humans, count))
    lesson = 'Преподаватель'
    # lesson = choice(random_lessons_school)
    income = 100000
    teachers = list(Teacher(*human.split(), lesson, income) for human in humans)
    return teachers
    
# >>> teachers = generate_teachers(random_humans, 5)
# >>> print(*teachers, sep='\n')
# Teacher Цветкова id=2088011136784
# Teacher Данилов id=2088014143504
# Teacher Никифоров id=2088014151248
# Teacher Титова id=2088014150992
# Teacher Воронова id=2088014148048
# >>>
# >>> silin = teachers[2]
# >>> print(*list(attr for attr in silin.__dict__.items()), sep='\n')
# ('last_name', 'Никифоров')
# ('first_name', 'Никита')
# ('patr_name', 'Степанович')
# ('birthdate', None)
# ('contacts', <class 'university.Contact'>)
# ('position', 'Информатика')
# ('income', 100000)
# ('courses', [])
# ('degree', кандидат)
# ('professor', False)

# Administrators - генерируем из списка random_humans - экземпляры класса Administrator
def generate_admins(humans: list[str], count: int = 10) -> list[Administrator]:
    """Функция генерирует список экземпляров класса Administrator"""
    humans = list(sample(humans, count))
    position = choice(random_admins)
    income = 10000
    admins = list(Administrator(*human.split(), position, income) for human in humans)
    return admins

# >>> admins = generate_admins(random_humans, 5)
# >>> print(*admins, sep='\n')
# Administrator Назаров id=2670600113872
# Administrator Петухова id=2670600112528
# Administrator Полякова id=2670600112592
# Administrator Козлова id=2670600112656
# Administrator Молчанова id=2670600114256
# >>>
# >>> nazarov = admins[0]
# >>> print(*list(attr for attr in nazarov.__dict__.items()), sep='\n')
# ('last_name', 'Назаров')
# ('first_name', 'Игорь')
# ('patr_name', 'Владиславович')
# ('birthdate', None)
# ('contacts', <class 'university.Contact'>)
# ('position', 'Заведующий кафедрой')
# ('income', 10000)
# ('head', None)
# ('subordinates', [])



# Создаем экземпляр класса University
KGPU_Tsiolkovsky = University('КГПУ им. К.Э. Циолковского', 'Государственный педагогический университет имени К.Э. Циолковского')


# Создаем экземпляр класса Administrator
rector = Administrator(*choice(random_humans).split(), position='ректор', income=1)
admin_hr = Administrator(*choice(random_humans).split(), position='руководитель HR', income=1)
# >>> print(*list(attr for attr in rector.__dict__.items()), sep='\n')
# ('last_name', 'Козлова')
# ('first_name', 'Дарья')
# ('patr_name', 'Кирилловна')
# ('birthdate', None)
# ('contacts', <class 'university.Contact'>)
# ('position', 'ректор')
# ('income', 1)
# ('head', None)
# ('subordinates', [])


# Устанавливаем значение атрибута hr - как экземпляр класса HR
KGPU_Tsiolkovsky.hr = HR('Отдел кадров')
KGPU_Tsiolkovsky.hr.head = admin_hr


# Назначаем руководителя Университета
KGPU_Tsiolkovsky.change_head(rector)


# Добавляем в Университет факультеты - экземпляры класса Faculty
for key in data_structure_kgpu.keys():
    KGPU_Tsiolkovsky.facultets.append(Faculty(key))
    
# >>> for F in KGPU_Tsiolkovsky.facultets:
# ...     print(f'{F.title} -> {F.__class__}')
# ...
# Инженерно-технологический факультет -> <class 'university.Faculty'>
# Факультет естествознания -> <class 'university.Faculty'>
# Факультет педагогики -> <class 'university.Faculty'>
# Факультет психологии -> <class 'university.Faculty'>
# Факультет искусств и социокультурного проектирования -> <class 'university.Faculty'>
# Факультет лингвистики и мировых языков -> <class 'university.Faculty'>
# Факультет филологии и массмедиа -> <class 'university.Faculty'>
# Факультет истории и права -> <class 'university.Faculty'>
# Медицинский факультет -> <class 'university.Faculty'>


# Создаем кафедры из заготовленного словаря - экземпляры Department
departments = []
for value in data_structure_kgpu.values():
    departments.append(Department(value))
    
# >>> for department in departments:
# ...     print(f'{department.title} -> {department.__class__}')
# ...
# ['Кафедра Инженерных и технологических дисциплин', 'Кафедра Информатики и информационных технологий', 'Кафедра Физики и математики', 'Кафедра Экономики и управления'] -> <class 'university.Department'>
# ['Ботанический сад', 'Кафедра Биологии и экологии', 'Кафедра Географии и безопасности жизнедеятельности', 'Кафедра Химии'] -> <class 'university.Department'>
# ['Кафедра Педагогики', 'Кафедра Теории и методики дошкольного, начального и специального образования'] -> <class 'university.Department'>
# ['Кафедра Общей и социальной психологии', 'Кафедра Психологии развития и образования'] -> <class 'university.Department'>
# ['Кафедра Искусств и социально-культурной деятельности', 'Кафедра Социальной адаптации и организации работы с молодежью', 'Кафедра Теории и методики физического воспитания', 'Кафедра Физического воспитания', 'Кафедра Философии, культурологии и социологии'] -> <class 'university.Department'>
# ['Кафедра Английского языка', 'Кафедра Лингвистики и иностранных языков', 'Кафедра Теории языкознания и немецкого языка', 'Кафедра Французского языка'] -> <class 'university.Department'>
# ['Кафедра Литературы', 'Кафедра Русского языка', 'Кафедра Русского языка как иностранного'] -> <class 'university.Department'>
# ['Кафедра Истории', 'Кафедра Таможенного дела и логистики', 'Кафедра Юриспруденции'] -> <class 'university.Department'>
# ['Кафедра Внутренних болезней', 'Кафедра Медико-биологических дисциплин', 'Кафедра Постдипломного образования - Eдиный аккредитационно-симуляционный центр подготовки медицинских работников', 'Кафедра Хирургии'] -> <class 'university.Department'>


# Генерируем 99 экземпляров класса Teachers
teachers = generate_teachers(random_humans, 99)
# >>> teachers
# [<university.Teacher object at 0x000002011670DC10>, <university.Teacher object at 0x0000020116427C10>, <university.Teacher object at 0x000002011670F410>, <university.Teacher object at 0x000002011670C350>, <university.Teacher object at 0x000002011670EDD0>, <university.Teacher object at 0x000002011670C190>, <university.Teacher object at 0x000002011670C290>, <university.Teacher object at 0x000002011670C210>, <university.Teacher object at 0x000002011670ECD0>, <university.Teacher object at 0x000002011670F210>, <university.Teacher object at 0x000002011670C3D0>, <university.Teacher object at 0x000002011670D5D0>, <university.Teacher object at 0x000002011670D4D0>, <university.Teacher object at 0x000002011670D550>, <university.Teacher object at 0x000002011670D250>, <university.Teacher object at 0x000002011670D1D0>, <university.Teacher object at 0x000002011670D0D0>, <university.Teacher object at 0x000002011670D110>, <university.Teacher object at 0x000002011670D150>, <university.Teacher object at 0x000002011670D190>, <university.Teacher object at 0x000002011670CD90>, <university.Teacher object at 0x000002011670CE10>, <university.Teacher object at 0x000002011670D090>, <university.Teacher object at 0x000002011670CFD0>, <university.Teacher object at 0x000002011670CF50>, <university.Teacher object at 0x000002011670CF10>, <university.Teacher object at 0x000002011670CD50>, <university.Teacher object at 0x000002011670CCD0>, <university.Teacher object at 0x000002011670CC10>, <university.Teacher object at 0x000002011670CC50>, <university.Teacher object at 0x000002011670CC90>, <university.Teacher object at 0x000002011670CB50>, <university.Teacher object at 0x000002011670CB90>, <university.Teacher object at 0x000002011670CB10>, <university.Teacher object at 0x000002011670CA50>, <university.Teacher object at 0x000002011670C990>, <university.Teacher object at 0x000002011670C850>, <university.Teacher object at 0x000002011670C810>, <university.Teacher object at 0x000002011670C6D0>, <university.Teacher object at 0x000002011670C710>, <university.Teacher object at 0x000002011670C750>, <university.Teacher object at 0x000002011670C790>, <university.Teacher object at 0x000002011670C7D0>, <university.Teacher object at 0x000002011670C690>, <university.Teacher object at 0x000002011670C610>, <university.Teacher object at 0x000002011670C550>, <university.Teacher object at 0x000002011670C4D0>, <university.Teacher object at 0x000002011670C450>, <university.Teacher object at 0x000002011670E7D0>, <university.Teacher object at 0x000002011670E710>, <university.Teacher object at 0x000002011670E6D0>, <university.Teacher object at 0x000002011670E690>, <university.Teacher object at 0x000002011670E650>, <university.Teacher object at 0x000002011670E610>, <university.Teacher object at 0x000002011670E5D0>, <university.Teacher object at 0x000002011670E590>, <university.Teacher object at 0x000002011670C390>, <university.Teacher object at 0x000002011670C2D0>, <university.Teacher object at 0x000002011670C250>, <university.Teacher object at 0x000002011670C0D0>, <university.Teacher object at 0x000002011670C090>, <university.Teacher object at 0x000002011670E3D0>, <university.Teacher object at 0x000002011670E350>, <university.Teacher object at 0x000002011670E310>, <university.Teacher object at 0x000002011670E2D0>, <university.Teacher object at 0x000002011670E1D0>, <university.Teacher object at 0x000002011670E190>, <university.Teacher object at 0x000002011670E150>, <university.Teacher object at 0x000002011670E110>, <university.Teacher object at 0x00000201166DF810>, <university.Teacher object at 0x00000201166DF850>, <university.Teacher object at 0x00000201166DEE50>, <university.Teacher object at 0x00000201166DEB50>, <university.Teacher object at 0x00000201166DF950>, <university.Teacher object at 0x00000201166DFB10>, <university.Teacher object at 0x00000201166DF9D0>, <university.Teacher object at 0x00000201166DFB50>, <university.Teacher object at 0x00000201166DF5D0>, <university.Teacher object at 0x00000201166DF610>, <university.Teacher object at 0x00000201166DF650>, <university.Teacher object at 0x00000201166DF690>, <university.Teacher object at 0x00000201166DF990>, <university.Teacher object at 0x00000201166DFE90>, <university.Teacher object at 0x00000201166DF0D0>, <university.Teacher object at 0x00000201166DFA90>, <university.Teacher object at 0x00000201166DF8D0>, <university.Teacher object at 0x00000201166F2A50>, <university.Teacher object at 0x00000201166F0D90>, <university.Teacher object at 0x00000201166F1190>, <university.Teacher object at 0x00000201166F2650>, <university.Teacher object at 0x00000201166F2550>, <university.Teacher object at 0x00000201166F2590>, <university.Teacher object at 0x00000201166F38D0>, <university.Teacher object at 0x00000201166F21D0>, <university.Teacher object at 0x00000201166F2210>, <university.Teacher object at 0x00000201166F36D0>, <university.Teacher object at 0x00000201166F3710>, <university.Teacher object at 0x00000201166F2110>, <university.Teacher object at 0x00000201166F34D0>]

# Добавляем преподавателей в кафедры - случайным образом  
while len(teachers) > 0:
    rand_teacher = teachers.pop(choice(range(len(teachers))))
    choice(departments).append(rand_teacher)

# >>> teachers
# []


# Генерируем 200 аудиторий - экземпляры класса Auditorium
nums = [str(num) for num in range(101, 201)]
auditoriums = []
while len(nums) > 0:
    num = nums.pop(choice(range(len(nums))))
    aud = Auditorium(num, choice([30, 50, 100, 200]), choice([1, 2, 3]))
    auditoriums.append(aud)

# >>> auditoriums    
# [Auditorium(number='181', seats=50, building=2), Auditorium(number='197', seats=30, building=1), Auditorium(number='191', seats=100, building=2), Auditorium(number='111', seats=50, building=3), Auditorium(number='188', seats=50, building=1), Auditorium(number='166', seats=100, building=3), Auditorium(number='126', seats=200, building=2), Auditorium(number='153', seats=200, building=3), Auditorium(number='130', seats=30, building=3), Auditorium(number='146', seats=200, building=1), Auditorium(number='169', seats=50, building=2), Auditorium(number='112', seats=200, building=2), Auditorium(number='154', seats=30, building=2), Auditorium(number='155', seats=200, building=2), Auditorium(number='129', seats=200, building=2), Auditorium(number='121', seats=50, building=2), Auditorium(number='104', seats=30, building=3), Auditorium(number='176', seats=200, building=2), Auditorium(number='113', seats=50, building=1), Auditorium(number='125', seats=50, building=2), Auditorium(number='150', seats=50, building=2), Auditorium(number='138', seats=50, building=2), Auditorium(number='194', seats=50, building=1), Auditorium(number='119', seats=30, building=3), Auditorium(number='136', seats=50, building=1), Auditorium(number='192', seats=30, building=3), Auditorium(number='178', seats=100, building=1), Auditorium(number='168', seats=30, building=2), Auditorium(number='122', seats=200, building=3), Auditorium(number='108', seats=200, building=2), Auditorium(number='134', seats=100, building=1), Auditorium(number='161', seats=30, building=2), Auditorium(number='144', seats=200, building=3), Auditorium(number='124', seats=50, building=1), Auditorium(number='128', seats=50, building=1), Auditorium(number='163', seats=200, building=2), Auditorium(number='135', seats=100, building=3), Auditorium(number='182', seats=200, building=1), Auditorium(number='193', seats=100, building=1), Auditorium(number='131', seats=100, building=1), Auditorium(number='186', seats=200, building=3), Auditorium(number='147', seats=50, building=1), Auditorium(number='101', seats=50, building=3), Auditorium(number='120', seats=100, building=3), Auditorium(number='185', seats=50, building=2), Auditorium(number='106', seats=200, building=1), Auditorium(number='196', seats=30, building=3), Auditorium(number='165', seats=200, building=3), Auditorium(number='160', seats=30, building=3), Auditorium(number='164', seats=100, building=1), Auditorium(number='141', seats=200, building=3), Auditorium(number='187', seats=30, building=2), Auditorium(number='139', seats=200, building=2), Auditorium(number='177', seats=30, building=2), Auditorium(number='167', seats=200, building=2), Auditorium(number='175', seats=50, building=3), Auditorium(number='199', seats=50, building=3), Auditorium(number='123', seats=200, building=2), Auditorium(number='184', seats=100, building=3), Auditorium(number='151', seats=50, building=1), Auditorium(number='103', seats=30, building=2), Auditorium(number='105', seats=50, building=1), Auditorium(number='190', seats=200, building=3), Auditorium(number='170', seats=50, building=2), Auditorium(number='137', seats=200, building=2), Auditorium(number='159', seats=50, building=2), Auditorium(number='195', seats=30, building=2), Auditorium(number='143', seats=30, building=3), Auditorium(number='183', seats=200, building=3), Auditorium(number='172', seats=30, building=1), Auditorium(number='115', seats=30, building=1), Auditorium(number='173', seats=30, building=2), Auditorium(number='156', seats=50, building=1), Auditorium(number='180', seats=30, building=3), Auditorium(number='109', seats=100, building=2), Auditorium(number='142', seats=200, building=3), Auditorium(number='114', seats=200, building=1), Auditorium(number='157', seats=100, building=1), Auditorium(number='198', seats=100, building=1), Auditorium(number='107', seats=200, building=3), Auditorium(number='152', seats=50, building=1), Auditorium(number='149', seats=30, building=1), Auditorium(number='158', seats=200, building=2), Auditorium(number='118', seats=100, building=1), Auditorium(number='162', seats=30, building=3), Auditorium(number='110', seats=30, building=3), Auditorium(number='145', seats=30, building=1), Auditorium(number='102', seats=30, building=3), Auditorium(number='200', seats=200, building=1), Auditorium(number='116', seats=100, building=1), Auditorium(number='117', seats=30, building=2), Auditorium(number='127', seats=30, building=1), Auditorium(number='148', seats=30, building=1), Auditorium(number='171', seats=200, building=2), Auditorium(number='132', seats=100, building=1), Auditorium(number='174', seats=30, building=1), Auditorium(number='133', seats=50, building=3), Auditorium(number='179', seats=200, building=1), Auditorium(number='189', seats=50, building=2), Auditorium(number='140', seats=30, building=3)]
    

# Добавляем аудитории к кафедрам


















