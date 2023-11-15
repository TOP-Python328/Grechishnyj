from random import sample

from data import random_humans

from university import Contact, Person, Employee, Teacher, Administrator

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



# Tecт Person, Employee,  - генерируем из списка random_humans - 10 Person  
def generate_persons(humans: list[str], count: int = 10) -> list[Person]:
    """Функция генерирует экземпляры класса Person
    
    :return: объект генератор
    """
    humans = list(sample(humans, count))
    return (Employee(*human.split()) for human in humans)
  
# >>> print(*generate_persons(random_humans), sep='\n')
# Person Федорова М. id=1165206791120
# Person Денисова М. id=1165206792976
# Person Дорофеева П. id=1165206794832
# Person Петухова А. id=1165206794704
# Person Панфилова Ж. id=1165206790992
# Person Данилов К. id=1165206793936
# Person Воронова П. id=1165206794896
# Person Хохлова Е. id=1165206794960
# Person Давыдова К. id=1165206795024
# Person Сорокина Г. id=1165206795088

# >>> print(*generate_persons(random_humans), sep='\n')
# Employee Никитин И. id=1826992055824
# Employee Князев Р. id=1826991953424
# Employee Баранова А. id=1826992130000
# Employee Козлова П. id=1826991994832
# Employee Шашкова Г. id=1826994722960
# Employee Фролов Е. id=1826994723920
# Employee Коновалова Ж. id=1826994718928
# Employee Кошелев А. id=1826994718736
# Employee Рыбаков И. id=1826994719184
# Employee Сидоров К. id=1826994719504








