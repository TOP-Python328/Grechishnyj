from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from datetime import date as dt
from decimal import Decimal as dec 
from typing import Self


# ===============================================================
#   PEOPLE
# ===============================================================


@dataclass
class Contact:
    """Контактные данные"""
    mobile: str = None
    office: str = None
    email: str = None
    web: str = None
    telegram: str = None
    
    
class Person(ABC):
    """Персона (человек)"""
    
    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            birthdate: dt,
            contact: Contact = None,
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name
        self.birthdate = birthdate
        self.contact = Contact

    def __repr__(self):
        return f'{self.__class__.__name__} {self.last_name} {self.first_name[0]}. id={id(self)}'


class Employee(Person):
    """Работник"""
    
    def __init__(
            self,
            last_name,
            first_name,
            patr_name,
            birthdate: dt,
            contact: Contact = None,
            position: str = None,
            income: dec = 1,
    ):
        super().__init__(last_name, first_name, patr_name, birthdate, contact)
        self.position = position
        self.income = income
    
    @abstractmethod
    def calc_month_income(self) -> dec:
        """Ежемесячный доход"""
        pass


class Student(Person):
    """Студент"""
    
    class EducationForm(Enum):
        """Форма обучения"""
        
        INTRAMURAL = 'очная'
        EXTRAMURAL = 'заочная'
        REMOTE = 'удаленная'
        
        def __repr__(self):
            return f'{self.__dict__["_value_"]}'
        
    class ContractForm(Enum):
        """Форма договора"""
        
        BUDGET = 'бюджетный'
        COMPANY = 'целевой'
        PERSONAL = 'персональный'
        
        def __repr__(self):
            return f'{self.__dict__["_value_"]}'
    
    def __init__(
            self,
            last_name,
            first_name,
            patr_name,
            birthdate: dt,
            contact: Contact = None,
            form: EducationForm = EducationForm.INTRAMURAL,
            contract: ContractForm = ContractForm.BUDGET,
            semester: int = 1,
            stipendia: dec = 1
    ):
        super().__init__(last_name, first_name, patr_name, birthdate, contact)
        self.id_ = str(id(self))
        self.form = form
        self.contract = contract
        self.semester = semester
        self.gradebook = Gratebook()
        self._stipendia = stipendia
    
    
    def stipendia(self, new_stipendia) -> None:
        """Стипендия - setter"""
        self._stipendia = new_stipendia
    stipendia = property(fset = stipendia)


class Teacher(Employee):
    """Преподаватель"""
    
    class Degree(Enum):
        """Ученая степень"""
        CANDIDATE = 'кандидат'
        DOCTOR = 'доктор'
        
        def __repr__(self):
            return f'{self.__dict__["_value_"]}'
    
    def __init__(
            self,
            last_name,
            first_name,
            patr_name,
            birthdate: dt,
            contact: Contact = None,
            position: str = None,
            income: str = 1, 
            courses: list[str] = [],
            degree: Degree = Degree.CANDIDATE,
            professor: bool = False
    ):
        super().__init__(
            last_name, 
            first_name, 
            patr_name, 
            birthdate, 
            contact, 
            position, 
            income
        )
        self.courses = courses
        self.degree = degree
        self.professor = professor
        
    def calc_month_income(self) -> dec:
        """Расчёт оплаты труда - часы, научная степень, доп работа"""
        pass
        
        
    def make_examination(self, student: Student) -> 'Cratebook.GradeRecord':
        """Провести экзамен - сделать запись в зачётной книжке"""
        student.gratebook[self.courses]
        pass


class Administrator(Employee):
    """Администратор"""
    
    def __init__(
            self,
            last_name,
            first_name,
            patr_name,
            birthdate: dt,
            contact: Contact = None,
            position: str = None,
            income: str = 1, 
            head: Self = None,
            subordinates: list[Employee] = []
    ):
        super().__init__(
            last_name, 
            first_name, 
            patr_name,
            birthdate, 
            contact,             
            position, 
            income
        )
        self.head = head
        self.subordinates = subordinates
    
    
    def calc_month_income(self) -> dec:
        """Расчёт оплаты труда - оклад + премия"""
        pass

        
    
class Gratebook(dict):
    """Зачётная книжка"""
    
    @dataclass
    class GrateRecord:
        """Запись в зачётной книжке"""
        
        class ExamType(Enum):
            """Тип экзамена"""
            CHECK = 'зачёт'
            DIFF_CHECK = 'дифзачёт'
            EXAMEN = 'экзамен'
            PROJECT = 'проект'

        semester: int = None
        date: date = None
        _type: ExamType = ExamType.CHECK
        grade: int = None
        scale: int = 5
        examiner: Teacher = None
    
    def __init__(
            self,
            records: dict[str, GrateRecord] = {}
    ):
        self.id_ = str(id(self))
        self.records = records
        
    def avg_semester_grade(self) -> float:
        """Средняя оценка за семестр"""
        pass


# ===============================================================
#   ORGANIZATION LEVEL
# ===============================================================


class OrganizationLevel(list):
    """Организационный уровень"""

    def __init__(
            self,
            title: str,
            description: str = '',
            head: Administrator = None,
            staff: list[Administrator] = [],
            contact: Contact = None
    ):
        super().__init__()
        self.title = title
        self.description = description
        self.head = head
        self._staff = staff
        self.contact = contact
    
    @property    
    def staff(self) -> list:
        """Персонал - setter"""
        return self._staff
    
    @staff.setter
    def staff(self, human) -> None:
        """Персонал - getter"""
        self._staff.append(human)
        
    def __repr__(self):
        return f'{self.title}'
    
    
class Group(list):
    """Учебная группа"""
    
    def __init__(
            self,
            id_: str = '',
            chief: Student = None,
            curator: Teacher = None,
    ):
        self.id_ = str(id(self))
        self.chief = chief
        self.curator = curator


@dataclass
class Auditorium:
    """Аудитория"""
    
    number: str = ''
    seats: int = 0
    building: str = 0
    
    
class Department(OrganizationLevel):
    """Кафедра"""
    
    def __init__(
            self,
            title,
            description = None,
            head = None,
            staff = [],
            contact = None,
            teachers: list[Teacher] = [],
            auditoria: list[Auditorium] = []
    ):
        super().__init__(title, description, head, staff, contact)
        self.teachers = teachers
        self.auditoria = auditoria


class Faculty(OrganizationLevel):
    """Факультет"""
    
    def __init__(
            self,
            title,
            description = None,
            head = None,
            staff = [],
            contact = None,
            departments: list[Department] = []
    ): 
        super().__init__(title, description, head, staff, contact)
        self.departments = departments


    def enroll_student(self) -> None:
        """Зачислить студента"""
        pass

   
    def expel_student(self) -> None:
        """Отчислить студента"""
        pass
        
        
# @singleton
class HR(OrganizationLevel):
    """Human Resources"""


    def __init__(self, title): 
        super().__init__(title)


    def hire(self):
        """Нанимать"""


    def fire(self):
        """Увольнять"""            


# @singleton
class University(OrganizationLevel):
    """Университет"""
    
    def __init__(
            self,
            title,
            description = None,
            head = None,
            _staff = [],
            contact = None,
            hr = None,
            facultets: list[Faculty] = [],
    ):
        super().__init__(title, description, head, _staff, contact)
        self.hr = hr
        self.facultets = facultets

    def change_head(self, person: Administrator) -> None:
        """Выбрать управляющего"""
        self.head = person
