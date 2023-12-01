"""Строитель кода Класса"""

from typing import Self

class CLSTemplate:
    """Шаблон класса"""
    space: str = ' ' * 4
    line: str = '\n' 

    def __init__(self, name: str):
        if name[0].islower():
            name = name.title()
        self.name: str = name
        print(self.name)
        self.__docstring: str = ''
        self.__fields: dict[str, str] = {}
        self.__constructor: dict[str, str] = {}
        self.__inherits: list[str] = []
   
    def docstring(self, docstring: str) -> None:
        """Устанавливает docstring для класса"""
        self.__docstring = docstring

    def fields(self, key: str, value: str = 'None') -> None:
        """Добавляет поле в словарь полей класса"""
        self.__fields[str(key)] = str(value)

    def constructor(self, key: str, value: str = 'None') -> None:
        """Добавляет атрибут в словарь конструктора класса"""
        self.__constructor[str(key)] = str(value)

    def inherits(self, class_name: str) -> None:
        """Добавляет в список имя родительского класса от которого наследован текущий"""
        if class_name[0].islower():
            class_name = class_name.title()
        self.__inherits.append(class_name)
    
    @staticmethod
    def create(name: str) -> 'ClassBuilder':
        """Создает и вызывает класс строитель"""
        return ClassBuilder(name)
   
    def __str__(self):
        name = self.name
        docstring = ''
        fields = ''
        constructor = ''
        inherits = ''
        
        if self.__inherits:
            inherits = f"({', '.join(self.__inherits)})"
        if self.__docstring:
            docstring = f'{self.space}\"\"\"{self.__docstring}\"\"\"{self.line}'
        if self.__fields:
            fields = f'{self.line}'.join(
                f"{self.space}{' = '.join(item)}" 
                for item in self.__fields.items())
            fields += self.line * 2
        if self.__constructor:
            constructor = f'{self.space}def __init__(self){self.line}' +\
                f'{self.line}'.join(f"{self.space * 2}self.{' = '.join(item)}" 
                for item in self.__constructor.items())
            constructor += self.line
   
        if all((not docstring, not fields, not constructor)):
            return f'class {name}{inherits}:{self.line}{self.space}pass'
        else:
            return f'class {name}{inherits}:{self.line}{docstring}{fields}{constructor}'


class ClassBuilder:
    """Строитель - формирует текст кода класса"""
    def __init__(self, root: CLSTemplate | str):
        if isinstance(root, CLSTemplate):
            self.root = root
        elif isinstance(root, str):
            self.root = CLSTemplate(root)
        else:
            raise TypeError('use ClassBuilder or str instance for root parameter')

    def add_docstring(self, docstring) -> Self:
        """Добавляет строку документации и возвращает текущий строитель"""
        self.root.docstring(docstring)
        return self

    def add_class_field(self, key, value = 'None'):
        """Добавляет поле класса и возвращает текущий строитель"""
        self.root.fields(key, value)
        return self
        
    def add_instance_attr(self, key, value = 'None') -> Self:
        """Добавляет атрибут экземпляра и возвращает текущий строитель"""
        self.root.constructor(key, value)
        return self
        
    def add_inherit(self, class_name) -> Self:
        """Добавляет класс наследования и возвращает текущий строитель"""
        self.root.inherits(class_name)
        return self
 
    def build(self):
        """Возвращает экземпляр созданного класса"""
        return self.root



# Вызов от класса CLSTemplate
# >>> cls = CLSTemplate.create('TestTemplate')\
# ... .build()
# >>>
# >>> print(cls)
# class TestTemplate:
    # pass
# >>>
# >>> cls = CLSTemplate.create('TestTemplate')\
# ... .add_inherit('cls')\
# ... .add_inherit('tmp')\
# ... .add_class_field('field_1')\
# ... .add_class_field('field_2', [])\
# ... .add_class_field('field_3', dict())\
# ... .add_class_field('field_4', 5)\
# ... .add_instance_attr('attr_1')\
# ... .add_instance_attr('attr_2')\
# ... .add_instance_attr('attr_3', 'Test')\
# ... .add_docstring('Test docstring')\
# ... .build()
# >>>
# >>>
# >>> print(cls)
# class TestTemplate(Cls, Tmp):
    # """Test docstring"""
    # field_1 = None
    # field_2 = []
    # field_3 = {}
    # field_4 = 5

    # def __init__(self)
        # self.attr_1 = None
        # self.attr_2 = None
        # self.attr_3 = Test

# >>>

# Вызов от класса ClassBuilder
# >>> bld = ClassBuilder('TestBuilder')\
# ... .add_inherit('cls')\
# ... .add_inherit('tmp')\
# ... .add_class_field('field_1')\
# ... .add_class_field('field_2', [])\
# ... .add_class_field('field_3', dict())\
# ... .add_class_field('field_4', 5)\
# ... .add_instance_attr('attr_1')\
# ... .add_instance_attr('attr_2')\
# ... .add_instance_attr('attr_3', 'Test')\
# ... .add_docstring('Test docstring')\
# ... .build()
# >>>
# >>>
# >>> print(bld)
# class TestBuilder(Cls, Tmp):
    # """Test docstring"""
    # field_1 = None
    # field_2 = []
    # field_3 = {}
    # field_4 = 5

    # def __init__(self)
        # self.attr_1 = None
        # self.attr_2 = None
        # self.attr_3 = Test

# >>>








# =================
# Начальный вариант
# =================
  
# from typing import Self

# class ClassBuilder:
    # """Строитель для формирования текста кода класса"""
    
    # def __init__(self, name: str):
        # self.name: str = name
        # self.__docstring: str = ''
        # self.__fields: dict[str, str] = {}
        # self.__constructor: dict[str, str] = {}


    # def docstring(self, docstring) -> None:
        # """Устанавливает docstring для класса"""
        # self.__docstring = docstring
        # return self

    # def fields(self, key: str, value: str = 'None') -> None:
        # """Добавляет поле в список(словарь) полей класса"""
        # self.__fields[key] = value
        # return self


    # def constructor(self, key: str, value: str = 'None') -> None:
        # """Добавляет атрибут в список(словарь) конструктора класса"""
        # self.__constructor[key] = value
        # return self

    
    # def __str(self) -> str:
        # """Текстовое представление класса"""
        # space: str = ' ' * 4
        # line: str = '\n'
        # name = f'{self.name}:{line}'
        # docstring = ''
        # fields = f"{space}pass"
        # constructor = ''
        
        # if self.__docstring:
            # docstring = f'{space}\"\"\"{self.__docstring}\"\"\"{line}'

        # if self.__fields:
            # fields = f'{line}'.join(
                # f"{space}{' = '.join(item)}" 
                # for item in self.__fields.items())

        # if self.__constructor:
            # constructor = f'{line}{space}def __init__(self){line}' +\
                # f'{line}'.join(f"{space * 2}self.{' = '.join(item)}" 
                # for item in self.__constructor.items())
            # if fields:
                # constructor = f'{line}{constructor}'

        # return f'class {name}{docstring}{fields}{constructor}'

    # def __str__(self):
        # return self.__str() 
        
        
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