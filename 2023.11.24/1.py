"""Строитель кода Класса"""

from typing import Self

class Class:
    """Шаблон класса без полей"""
    
    
    def __init__(self, name: str):
        self.name = name
        self.docstring: str = ''
        self.__fields: dict[str, str] = {}
        self.__constructor: dict[str, str] = {}
        
        # self.docstring: str = 'docstring'
        # self.__fields: dict[str, str] = {'1':'2', '3':'None'}
        # self.__constructor: dict[str, str] = {'attr1':'attr1', 'attr2':'attr2'}
    
    def fields(self, key: str, value: str = 'None') -> None:
        """Добавляет поле в список(словарь) полей класса"""
        self.__fields[key] = value


    def constructor(self, key: str, value: str = 'None') -> None:
        """Добавляет атрибут в список(словарь) конструктора класса"""
        self.__constructor[key] = value
    
    
    def __str(self) -> str:
        """Текстовое представление класса"""
        space: str = ' ' * 4
        line: str = '\n'
        name = f'{self.name}:{line}'
        docstring = ''
        fields = f"{space}pass"
        constructor = ''
        
        if self.docstring:
            docstring = f'{space}\"\"\"{self.docstring}\"\"\"{line}'

        if self.__fields:
            fields = f'{line}'.join(
                f"{space}{' = '.join(item)}" 
                for item in self.__fields.items())

        if self.__constructor:
            constructor = f'{line}{space}def __init__(self){line}' +\
                f'{line}'.join(f"{space * 2}self.{' = '.join(item)}" 
                for item in self.__constructor.items())
            if fields:
                constructor = f'{line}{constructor}'

        return f'class {name}{docstring}{fields}{constructor}'
        
    def __str__(self):
        return self.__str()





class ClassBuilder:
    """Формирует текст кода класса"""
    
    def __init__(self, name):
        self.class_ = Class(name)
    

    def add_cls_field(self, field_name: str, field_value: str = 'None'):
        """Добавляет поле класс"""
        self.class_.fields(field_name, field_value)
        return self


    def add_inst_attr(self, attr_name: str, attr_value: str = 'None'):
        """Добавляет атрибут в конструктор экземпляра"""
        self.class_.constructor(attr_name, attr_value)
        return self


    def build(self) -> Class:
        return self.class_
