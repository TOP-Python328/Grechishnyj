"""Строитель кода Класса"""

from typing import Self

class ClassBuilder:
    """Строитель для формирования текста кода класса"""
    
    def __init__(self, name: str):
        self.name: str = name
        self.__docstring: str = ''
        self.__fields: dict[str, str] = {}
        self.__constructor: dict[str, str] = {}


    def docstring(self, docstring) -> None:
        """Устанавливает docstring для класса"""
        self.__docstring = docstring
        return self

    def fields(self, key: str, value: str = 'None') -> None:
        """Добавляет поле в список(словарь) полей класса"""
        self.__fields[key] = value
        return self


    def constructor(self, key: str, value: str = 'None') -> None:
        """Добавляет атрибут в список(словарь) конструктора класса"""
        self.__constructor[key] = value
        return self

    
    def __str(self) -> str:
        """Текстовое представление класса"""
        space: str = ' ' * 4
        line: str = '\n'
        name = f'{self.name}:{line}'
        docstring = ''
        fields = f"{space}pass"
        constructor = ''
        
        if self.__docstring:
            docstring = f'{space}\"\"\"{self.__docstring}\"\"\"{line}'

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
        
        
# >>> c = ClassBuilder('Root')\
# ... .docstring('test docstring')\
# ... .fields('field1')\
# ... .fields('field2')\
# ... .fields('field3')\
# ... .fields('field4')\
# ... .fields('field5')\
# ... .constructor('attr1')\
# ... .constructor('attr2')\
# ... .constructor('attr3')\
# ... .constructor('attr4')\
# ... .constructor('attr2')\
# ...
# >>> print(c)
# class Root:
    # """test docstring"""
    # field1 = None
    # field2 = None
    # field3 = None
    # field4 = None
    # field5 = None

    # def __init__(self)
        # self.attr1 = None
        # self.attr2 = None
        # self.attr3 = None
        # self.attr4 = None