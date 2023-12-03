# Реализуйте класс, HTMLProfile описывающий HTML документ портфолио человека.
# Добавьте класс Строителя CVProfiler для генерации такого HTML документа.
# Воспользуйтесь реализованными в предыдущей задаче классами HTMLTag и HTMLBuilder.

# Класс должен предоставить возможность добавить:
  # — обязательный раздел с фио, возрастом, и сферой занятости
  # — необязательный раздел с образованием (учебное заведение, специальность, год окончания)
  # — необязательный раздел с успешными работами/проектами
  # — обязательный раздел с произвольным набором полей контактов (email обязателен)

# В случае появления пункта из необязательного раздела, у этого раздела должен быть подзаголовок. 
# Если для раздела не заявлено ни одного пункта, то подзаголовок опускается.

# Добавьте к строителю метод build(), который вернёт сформированный объект.

# Реализуйте минимальную вёрстку.

# Человекочитаемое строковое представление CVProfiler должно вернуть строку с нужным кодом.

# Пример использования:

# cv1 = CVProfiler('Иванов Иван Иванович', 26, 'художник-фрилансер', 'ivv@abc.de')\
          # .add_education('Архитектурная Академия', 'Компьютерный дизайн', 2019)
          # .add_project('Разработка логотипа для компании по производству снеков', path_to_image)\
          # .add_project('UI разработка для интернет-магазина для восковых дел мастеров', path_to_image, path_to_image)\
          # .add_contact(devianart='ivovuvan_in_art')\
          # .add_contact(telegram='@ivovuvan')\
          # .build()
# print(cv1)
    
    
# <html>
    # <head>
        # <title>Иван: портфолио</title>
    # </head>
    # <body>
        # <div ...>
            # <h2>Обо мне</h2>
            # <p ...>...</p>
            # ...
        # </div>
        # ...
        # <div ...>
            # <h2>Образование</h2>
            # <ul ...>
                # <li>
                    # <p ...>...</p>
                # </li>
            # </ul>
            # ...
        # </div>
        # ...
    # </body>
# </html>


from htmlbuilder import HTMLTag, HTMLBuilder 
from datetime import date
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class About:
    """Описывает раздел о себе
    
    :param full_name: фио - полное имя
    :param age: возрастом
    :param employment: сфера деятельности
    """
    full_name: str = None
    age: int = None
    employment: str = None


@dataclass
class Study:
    """Описывает раздел с образованием

    :param institution: учебное заведение
    :param specialization: специальность
    :param graduation: год окончания
    """
    institution: str = None
    specialization: str = None
    graduation: int = None


@dataclass
class Project:
    """Описывае раздел с успешными работами/проектами
    
    :param name: наименование проекта
    :param images: список путей к изображениям
    :param link: web-ссылка на проект
    """
    name: str = None
    images: list[str] = None
    link: str = None

@dataclass
class Contact:
    """Описывает раздел с произвольным набором полей контактов"""
    mobile: str = None
    email: str = None
    web: str = None
    telegram: str = None
    

class HTMLProfile:
    """HTML документ - портфолио человека."""
    # обязательный раздел с произвольным набором полей контактов (email обязателен)
    # 'Иванов Иван Иванович', 26, 'художник-фрилансер', 'ivv@abc.de'
    
    def __init__(
            self, 
            full_name: str, 
            age: int = None, 
            employment: str = None, 
            email: str = None
    ):
        self.about: About = About()
        self.about.full_name = full_name
        self.about.age = age
        self.about.employment = employment
        self.education: list[Study] = []
        self.projects: list[Project] = []
        self.contacts: Contact = Contact()   
        self.contacts.email = email

   
    def set_contact(self, field_name: str, field_value: str) -> None:
        """Редактор раздела контактов"""
        setattr(self.contacts, field_name, field_value)


    def add_education(
            self,
            institution: str,
            specialization: str,
            graduation: int
    ) -> None:
        """Добавляет в раздел образования новое учебное заведение"""
        study = Study()
        study.institution = institution
        study.specialization = specialization
        study.graduation = graduation
        self.education.append(Study)

 
    def add_project(
            self, 
            name: str,
            link: str = None,
            *images: list[str]
            
    ) -> None:
        """Добавляет в раздел проектов новый проект"""
        project = Project()
        project.name = name
        project.link = link
        project.images = [images]
        self.projects.append(Project)


    @staticmethod
    def create(name: str, value: str = '') -> 'CVProfiler':
        return CVProfiler(name, value)
        
    
class CVProfiler:
    pass