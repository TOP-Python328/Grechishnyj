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


class Person:
    """Персона"""
    
    def __init__(
            self,
            last_name: str,
            first_name: str,
            patr_name: str,
            birthdate: dt = None,
            contacts: Contact = None,
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name
        self.birthdate = birthdate
        self.contacts = Contact
        
    # def __repr__(self):
        # return f'{self.__class__.__name__} {self.last_name} id={id(self)}'
  
    
class Employee(Person):
    """Работник"""
    
    def __init__(
            self,
            last_name,
            first_name,
            patr_name,
            position: str = None,
            income: dec = None,
    ):
        super().__init__(last_name, first_name, patr_name)
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
            form: EducationForm = EducationForm.INTRAMURAL,
            contract: ContractForm = ContractForm.BUDGET,
            semester: int = 1,
            stipendia: dec = 0
    ):
        super().__init__(last_name, first_name, patr_name)
        self.id_ = str(id(self))
        self.form = form
        self.contract = contract
        self.semester = semester
        self.gradebook = Gratebook()
        self._stipendia = stipendia
    
    
    def stipendia(self, new_stipendia) -> None:
        """Стипендия - getter"""
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
            position,
            income, 
            courses: list[str] = [],
            degree: Degree = Degree.CANDIDATE,
            professor: bool = False
    ):
        super().__init__(last_name, first_name, patr_name, position, income)
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
            position,
            income,
            head: Self = None,
            subordinates: list[Employee] = []
    ):
        super().__init__(last_name, first_name, patr_name, position, income)
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
        
    def staff(self, new_people) -> None:
        """Персонал - getter"""
        self._staff = new_people
    staff = property(fset = staff)
    
    # def __repr__(self):
        # return f'{self.__class__.__name__} {id(self)}'
    
    
    

    


class Group(list):
    """Учебная группа"""
    
    def __init__(
            self,
            id_: str = '',
            chief: Student = None,
            curator: Teacher = None,
            students: list[Student] = []
    ):
        self.id_ = str(id(self))
        self.chief = chief
        self.curator = curator
        self.students = students
        
        
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
            staff = None,
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
            staff = None,
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
            description,
            head = None,
            staff = None,
            contact = None,
            facultets: list[Faculty] = [],
            hr = None
    ):
        super().__init__(title, description, head, staff, contact)
        self.facultets = facultets
        self.hr = hr

    def change_head(self, person: Administrator) -> None:
        """Выбрать управляющего"""
        self.head = person

