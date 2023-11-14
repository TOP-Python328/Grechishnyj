from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from datetime import date as dt
from decimal import Decimal as dec 


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
            patr_name: str = None,
            birthdate: dt = None,
            contact: Contact = None,
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name
        self.birthdate = birthdate
        self.contact = Contact
        
    def __repr__(self):
        return f'{self.__class__.__name__} {self.last_name} {self.first_name[:1]}. id={id(self)}'

  
    
class Employee(Person):
    """Работник"""
    
    def __init__(
            self,
            last_name,
            first_name,
            position: str,
            income: dec,
    ):
        super().__init__(last_name, first_name)
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
        
    class ContractForm(Enum):
        """Форма договора"""
        
        BUDGET = 'бюджетный'
        COMPANY = 'целевой'
        PERSONAL = 'персональный'
        
    
    def __init__(
            self,
            last_name,
            first_name,
            id_: str = None,
            form: EducationForm = EducationForm.INTRAMURAL,
            contract: ContractForm = ContractForm.BUDGET,
            semester: int = None,
            gradebook: 'Gradebook' = None,
            stipendia: dec = None
    ):
        super().__init__(last_name, first_name)
        self.id_ = str(id(self))
        self.form = form
        self.contract = contract
        self.semester = semester
        self.gradebook = gradebook
        self._stipendia = stipendia
    
    
    def stipendia(self, new_stipendia) -> None:
        """Стипендия - getter"""
        self._stipendia = new_stipendia
    stipendia = property(fset = stipendia)
    
    
    
#class Gratebook   
# @dataclass
# class GradeRecord:
    # """Оценка - запись"""
    
    # semester: int = None
    # date: date = None
    # _type: ExamType
    # grade: int = None
    # scale: int = None
    # examiner: Teacher = None
    





# >>> person = Person('Иванов', 'Иван')
# >>> person
# Person Иванов И. id=2145804966480 


# >>> employee = Employee('Иванов', 'Иван', 'Преподаватель', 50000)
# >>> employee
# Employee Иванов И. id=2548274928848
# >>> employee.__dict__
# {'last_name': 'Иванов', 'first_name': 'Иван', 'patr_name': None, 'birthdate': None, 'contact': <class '__main__.Contact'>, 'position': 'Преподаватель', 'income': 50000}


# >>> diana = Student('Дмитриева', 'Диана')
# >>> diana
# Student Дмитриева Д. id=2088149874448
# >>>
# >>> for item in diana.__dict__.items():
# ...     print(*item)
# ...
# last_name Дмитриева
# first_name Диана
# patr_name None
# birthdate None
# contact <class '__main__.Contact'>
# id_ 2088149874448
# form EducationForm.INTRAMURAL
# contract ContractForm.BUDGET
# semester None
# gradebook None
