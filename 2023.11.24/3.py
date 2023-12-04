"""HTML - портфолио человека"""

from htmlbuilder import HTMLTag, HTMLBuilder 
from typing import Self
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
    images: tuple[str, ...] = None
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

    # kwargs - не реализовано
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

    def new_project(self, name: str, link: str = None, *images: tuple[str, ...]) -> None:
        """Добавляет в раздел проектов проект."""
        project = Project()
        project.name = name
        project.link = link
        project.images = images
        self.projects.append(project)

    @staticmethod
    def create(name: str) -> 'CVProfiler':
        """Возвращает строитель класса для создания нового экземпляра"""
        return CVProfiler(name)
 
    def edit(self: Self) -> 'CVProfiler':
        """Возвращает строитель класса передавая ему себя."""
        return CVProfiler(self)

    def __str__(self):
        html = HTMLTag.create('html')
        
        # head
        html = html.nested('head')\
            .sibling('title', self.about['full_name'])\
            .closest()
            
        # body
        html = html.nested('body')\
            .nested('header')\
            .sibling('h1', f"Резюме: {self.about['full_name']}")\
            .closest()\
            .nested('main')
            
        # about me
        html = html.nested('section')\
            .sibling('h2', 'Обо мне')\
            .nested('div')\
            .sibling('p', f"ФИО: {self.about['full_name']}")\
            .sibling('p', f"Возраст: {self.about['age']}")\
            .sibling('p', f"Сфера деятельности: {self.about['employment']}")\
            .closest()
        
        # study
        html = html.closest()\
            .nested('section')\
            .sibling('h2', 'Образование')\
            .nested('div')
        for study in self.education:
            html.sibling('p', f"Учебное заведение: {study.institution}")
        
        # projects
        html = html.closest()\
            .closest()\
            .nested('section')\
            .sibling('h2', 'Проекты')\
            .nested('div')
        for project in self.projects:
            html.sibling('p', f"Проект: {project.name} {project.link} [{' '.join(project.images)}]")
        
        # contacts
        html = html.closest()\
            .closest()\
            .nested('section')\
            .sibling('h2', 'Контакты')\
            .nested('div')
        for key, value in self.contacts.items():
            html.nested('div')\
            .sibling('span', f"{key}")\
            .sibling('span', f"{value}")\
            .closest()
            
        html = html.build()
        return f"{html}"

    
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



# >>> ivanov = HTMLProfile.create('Иванов Иван Иванович')\
# ... .add_contact('mobile', '+79600000000')\
# ... .add_contact('telegram', '@ivanov')\
# ... .add_contact('email', 'ivanov@ivanov.iv')\
# ... .add_about('age', 30)\
# ... .add_about('employment', 'художник-фрилансер')\
# ... .add_education('Архитектурная академия', 'Компьютерный дизайн', 2010)\
# ... .add_education('Строительный техникум', 'Инженер-сметчик', 2016)\
# ... .add_project('UI разработка интернет-магазина', 'link1', 'img1', 'img2')\
# ... .build()
# >>>
# >>> print(ivanov)
# <html>
  # <head>
    # <title>Иванов Иван Иванович</title>
  # </head>
  # <body>
    # <header>
      # <h1>Резюме: Иванов Иван Иванович</h1>
    # </header>
    # <main>
      # <section>
        # <h2>Обо мне</h2>
        # <div>
          # <p>ФИО: Иванов Иван Иванович</p>
          # <p>Возраст: 30</p>
          # <p>Сфера деятельности: художник-фрилансер</p>
        # </div>
      # </section>
      # <section>
        # <h2>Образование</h2>
        # <div>
          # <p>Учебное заведение: Архитектурная академия</p>
          # <p>Учебное заведение: Строительный техникум</p>
        # </div>
      # </section>
      # <section>
        # <h2>Проекты</h2>
        # <div>
          # <p>Проект: UI разработка интернет-магазина link1 [img1 img2]</p>
        # </div>
      # </section>
      # <section>
        # <h2>Контакты</h2>
        # <div>
          # <div>
            # <span>mobile</span>
            # <span>+79600000000</span>
          # </div>
          # <div>
            # <span>email</span>
            # <span>ivanov@ivanov.iv</span>
          # </div>
          # <div>
            # <span>web</span>
            # <span>None</span>
          # </div>
          # <div>
            # <span>telegram</span>
            # <span>@ivanov</span>
          # </div>
        # </div>
      # </section>
    # </main>
  # </body>
# </html>
# >>>