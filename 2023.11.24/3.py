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
from typing import Self
from abc import ABC, abstractmethod
from dataclasses import dataclass



class About(dict):
    """Описывает раздел о себе.
    
    :param full_name: фио - полное имя
    :param age: возраст
    :param employment: сфера деятельности
    """
    def __init__(self, full_name: str = None, age: int = None, employment: str = None):
        self['full_name'] = full_name
        self['age'] = age
        self['employment'] = employment
        self['picture'] = None


class Contact(dict):
    """Описывает раздел контактов."""
    def __init__(self, email: str = None, mobile: str = None, web: str = None, telegram: str = None):
        self['mobile'] = mobile
        self['email'] = email
        self['web'] = web
        self['telegram'] = telegram 


@dataclass
class Study:
    """Описывает учебное заведение.

    :param institution: учебное заведение
    :param specialization: специальность
    :param graduation: год окончания
    """
    institution: str = None
    specialization: str = None
    graduation: int = None


@dataclass
class Project:
    """Описывае  работу/проект.
    
    :param name: наименование проекта
    :param images: список путей к изображениям
    :param link: web-ссылка на проект
    """
    name: str = None
    images: list[str] = None
    link: str = None
    

class HTMLProfile:
    """HTML документ - портфолио человека."""
    def __init__(
            self, 
            full_name: str, 
            age: int = None, 
            employment: str = None, 
            email: str = None
    ):
        self.about: About = About(full_name, age, employment)
        self.education: list[Study] = []
        self.projects: list[Project] = []
        self.contacts: Contact = Contact(email)   

    def new_about(self, field_name: str, field_value: str) -> None:
        """Добавить(изменить) запись в разделе о себе."""
        self.about[field_name] = field_value

    def new_contact(self, field_name: str, field_value: str) -> None:
        """Добавить(изменить) запись в разделе контакты."""
        self.contacts[field_name] = field_value

    def new_education(self, institution: str, specialization: str, graduation: int) -> None:
        """Добавляет в раздел образования учебное заведение."""
        study = Study()
        study.institution = institution
        study.specialization = specialization
        study.graduation = graduation
        self.education.append(study)

    def new_project(self, name: str, link: str = None, *images: list[str]) -> None:
        """Добавляет в раздел проектов проект."""
        project = Project()
        project.name = name
        project.link = link
        project.images = [images]
        self.projects.append(project)

    @staticmethod
    def create(name: str) -> 'CVProfiler':
        """Возвращает строитель класса для создания нового экземпляра"""
        return CVProfiler(name)
 
    def edit(self: Self) -> 'CVProfiler':
        """Возвращает строитель класса передавая ему себя."""
        return CVProfiler(self)
    
class CVProfiler:
    
    def __init__(
            self, 
            root: HTMLProfile | str, 
            age: int = None, 
            employment: str = None, 
            email: str = None
    ) -> None:
        if isinstance(root, HTMLProfile):
            self.root = root
        elif isinstance(root, str):
            self.root = HTMLProfile(root, age, employment, email)
        else:
            raise TypeError('use HTMLProfile or str instance for root parameter')

    def add_about(self, name: str, value: str) -> Self:
        self.root.new_about(name, value)
        return self

    def add_contact(self, name: str, value: str) -> Self:
        self.root.new_contact(name, value)
        return self

    def add_education(self, institution: str, specialization: str, graduation: int) -> Self:
        self.root.new_education(institution, specialization, graduation)
        return self

    def add_project(self, name: str, link: str = None, *images: list[str]) -> Self:
        self.root.new_project(name, link, *images)
        return self

    def build(self) -> HTMLProfile:
        return self.root
    

# >>> prof = HTMLProfile.create('Иванов Иван Иванович')\
# ... .add_contact('mobile', '+79050000000')\
# ... .add_contact('whatsapp', '+79050000000')\
# ... .add_education('university', 'special', 2010)\
# ... .add_education('university2', 'special2', 2016)\
# ... .add_project('project1', 'link1', 'img', 'img')\
# ... .add_project('project2', 'link2', 'img', 'img')\
# ... .build()
# >>>
# >>>
# >>>
# >>> for item in prof.__dict__.items():
# ...     print(item)
# ...
# ('about', {'full_name': 'Иванов Иван Иванович', 'age': None, 'employment': None, 'picture': None})
# ('education', [Study(institution='university', specialization='special', graduation=2010), Study(institution='university2', specialization='special2', graduation=2016)])
# ('projects', [Project(name='project1', images=[('img', 'img')], link='link1'), Project(name='project2', images=[('img', 'img')], link='link2')])
# ('contacts', {'mobile': '+79050000000', 'email': None, 'web': None, 'telegram': None, 'whatsapp': '+79050000000'})
# >>>
# >>>
# >>>
# >>> prof.edit().add_about('age', 30).build()
# <__main__.HTMLProfile object at 0x000001E3E05D54D0>
# >>> for item in prof.__dict__.items():
# ...     print(item)
# ...
# ('about', {'full_name': 'Иванов Иван Иванович', 'age': 30, 'employment': None, 'picture': None})
# ('education', [Study(institution='university', specialization='special', graduation=2010), Study(institution='university2', specialization='special2', graduation=2016)])
# ('projects', [Project(name='project1', images=[('img', 'img')], link='link1'), Project(name='project2', images=[('img', 'img')], link='link2')])
# ('contacts', {'mobile': '+79050000000', 'email': None, 'web': None, 'telegram': None, 'whatsapp': '+79050000000'})
# >>>
# >>>
# >>>
# >>> prof = CVProfiler('Иванов Иван Иванович')\
# ... .add_contact('mobile', '+79050000000')\
# ... .add_contact('whatsapp', '+79050000000')\
# ... .add_education('university', 'special', 2010)\
# ... .add_education('university2', 'special2', 2016)\
# ... .add_project('project1', 'link1', 'img', 'img')\
# ... .add_project('project2', 'link2', 'img', 'img')\
# ... .build()
# >>>
# >>>
# >>>
# >>> for item in prof.__dict__.items():
# ...     print(item)
# ...
# ('about', {'full_name': 'Иванов Иван Иванович', 'age': None, 'employment': None, 'picture': None})
# ('education', [Study(institution='university', specialization='special', graduation=2010), Study(institution='university2', specialization='special2', graduation=2016)])
# ('projects', [Project(name='project1', images=[('img', 'img')], link='link1'), Project(name='project2', images=[('img', 'img')], link='link2')])
# ('contacts', {'mobile': '+79050000000', 'email': None, 'web': None, 'telegram': None, 'whatsapp': '+79050000000'})