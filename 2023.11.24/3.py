"""HTML - портфолио человека"""

from htmlbuilder import HTMLTag, HTMLBuilder 
from typing import Self
from dataclasses import dataclass


@dataclass
class Contact:
    """Описывает раздел контактов."""
    mobile: str = None
    email: str = None
    web: str = None
    telegram: str = None 


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
        # self.about: About = About(full_name, age, employment)
        self.full_name: str = full_name
        self.age: int = age
        self.employment: str = employment
        self.picture: str = None
        self.education: list[Study] = []
        self.projects: list[Project] = []
        self.contacts: Contact = Contact() 
        self.contacts.email = email

    def new_contact(self, **kwargs) -> None:
        """Добавить(изменить) запись в разделе контакты."""
        for key, value in kwargs.items():
            setattr(self.contacts, key, value)
        
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
    def create(full_name: str, age: int = None, employment: str = None, email: str = None) -> 'CVProfiler':
        """Возвращает строитель класса для создания нового экземпляра"""
        instance_profile = HTMLProfile(full_name, age, employment, email)
        return CVProfiler(instance_profile)
 
    def edit(self: Self) -> 'CVProfiler':
        """Возвращает строитель класса передавая ему себя для редактирования"""
        return CVProfiler(self)

    def __str__(self):
        html = HTMLTag.create('html')
        
        # head
        html = html.nested('head')\
            .sibling('title', self.full_name)\
            .closest()
            
        # body
        html = html.nested('body')\
            .nested('header')\
            .sibling('h1', f"Резюме: {self.full_name}")\
            .closest()\
            .nested('main')
            
        # about me
        html = html.nested('section')\
            .sibling('h2', 'Обо мне')\
            .nested('div')\
            .sibling('p', f"ФИО: {self.full_name}")\
            .sibling('p', f"Возраст: {self.age}")\
            .sibling('p', f"Сфера деятельности: {self.employment}")\
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
        for key, value in self.contacts.__dict__.items():
            html.nested('div')\
            .sibling('span', f"{key}")\
            .sibling('span', f"{value}")\
            .closest()
            
        html = html.build()
        return f"{html}"

    
class CVProfiler:
    """ Строитель для класса HTMLProfile - портфолио"""
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

    def add_contact(self, **kwargs) -> Self:
        self.root.new_contact(**kwargs)
        return self

    def add_education(self, institution: str, specialization: str, graduation: int) -> Self:
        self.root.new_education(institution, specialization, graduation)
        return self

    def add_project(self, name: str, link: str = None, *images: list[str]) -> Self:
        self.root.new_project(name, link, *images)
        return self

    def build(self) -> HTMLProfile:
        return self.root


# >>> ivanov = HTMLProfile.create('Иванов Иван Иванович', 30, 'художник')\
# ... .add_contact(mobile='+79600000000', vKontakte='ivanov.vk', github='@ivangithub', email='iii@gmail.com')\
# ... .add_education('Архитектурная академия', 'Компьютерный дизайн', 2010)\
# ... .add_education('Строительный техникум', 'Инженер-конструктор', 2016)\
# ... .add_project('Разработка архитектурной концепции миктрорайона', 'link1', 'img1', 'img2')\
# ... .add_project('Разработка проекта реставрации здания', 'link2', 'img1', 'img2')\
# ... .add_project('Организация выставки современных архитектурных направлений', 'link3', 'img1', 'img2')\
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
          # <p>Сфера деятельности: художник</p>
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
          # <p>Проект: Разработка архитектурной концепции миктрорайона link1 [img1 img2]</p>
          # <p>Проект: Разработка проекта реставрации здания link2 [img1 img2]</p>
          # <p>Проект: Организация выставки современных архитектурных направлений link3 [img1 img2]</p>
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
            # <span>iii@gmail.com</span>
          # </div>
          # <div>
            # <span>web</span>
            # <span>None</span>
          # </div>
          # <div>
            # <span>telegram</span>
            # <span>None</span>
          # </div>
          # <div>
            # <span>vKontakte</span>
            # <span>ivanov.vk</span>
          # </div>
          # <div>
            # <span>github</span>
            # <span>@ivangithub</span>
          # </div>
        # </div>
      # </section>
    # </main>
  # </body>
# </html>
# >>>