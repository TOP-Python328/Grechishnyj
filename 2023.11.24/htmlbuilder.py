"""Демонстратор строителя."""

from pathlib import Path
from sys import path
from typing import Self


class HTMLTag:
    """
    Описывает HTML тег, который может содержать вложенные теги.
    Может быть инициализирован с помощью строителя.
    """
    default_indent_spaces: int = 2
    
    def __init__(self, name: str, value: str = '', **kw_attrs):
        self.name = name
        self.value = value
        self.attrs: dict = {str(key): str(value) for key, value in kw_attrs.items()}
        self.__nested: list[HTMLTag] = []
    
    def nested(self, html_tag: Self):
        """Добавляет вложенный тег к текущему."""
        self.__nested.append(html_tag)
    
    def __str(self, indent_level: int) -> str:
        """Рекурсивно формирует строку с текущим и всеми вложенными тегами."""
        margin = ' ' * indent_level * self.default_indent_spaces
        eol = ''
        attrs = ' '.join(['='.join((f"{key}", f'"{value}"')) for key, value in self.attrs.items()])
        result = f"{margin}<{self.name}{attrs}>{self.value}"
        if self.__nested:
            for tag in self.__nested:
                result += '\n' + tag.__str(indent_level+1)
            eol = f'\n{margin}'
        result += f"{eol}</{self.name}>"
        return result
    
    def __str__(self):
        return self.__str(0)
    
    # в данной реализации нецелесообразно "прятать" класс HTMLBuilder
    @staticmethod
    def create(name: str, value: str = '') -> 'HTMLBuilder':
        return HTMLBuilder(name, value)


class HTMLBuilder:
    """
    Предоставляет методы для пошаговой инициализации экземпляра HTMLTag.
    """
    def __init__(self, root: HTMLTag | str, value: str = '', *, parent: Self = None):
        if isinstance(root, HTMLTag):
            pass
        elif isinstance(root, str):
            root = HTMLTag(root, value)
        else:
            raise TypeError('use HTMLTag or str instance for root parameter')
        self.root: HTMLTag = root
        self.__parent: Self = parent
    
    def nested(self, name: str, value: str = '', **kw_attrs) -> Self:
        """Добавляет вложенный тег к текущему тегу и возвращает строитель для вложенного тега."""
        tag = HTMLTag(name, value, **kw_attrs)
        self.root.nested(tag)
        return HTMLBuilder(tag, parent=self)
    
    def sibling(self, name: str, value: str = '', **kw_attrs) -> Self:
        """Добавляет вложенный тег к текущему тегу и возвращает текущий строитель."""
        tag = HTMLTag(name, value, **kw_attrs)
        self.root.nested(tag)
        return self

    def closest(self) -> Self:
        """Возвращает строитель родительского тега относительного текущего тега"""
        if self.__parent is None:
            return self
        else:
            return self.__parent
    
    def build(self) -> HTMLTag:
        if self.__parent is None:
            return self.root
        else:
            return self.__parent.build()

def write_html_file(html: HTMLTag, fileout: str = '2') -> None:
    """Запись html-DOM в файл"""
    (Path(path[0]) / f'{fileout}.html').write_text(str(html), encoding='utf-8')

# >>> html = HTMLTag.create('html')\
# ... .nested('body', 'Main', bg='yellow', font='sans')\
# ... .nested('header', bg='green', fontsize='20px')\
# ... .nested('div', border='1px sold white')\
# ... .nested('ul')\
# ... .sibling('li', 'Pos_1', color='grey')\
# ... .sibling('li', 'Pos_2', color='blue')\
# ... .sibling('li', 'Pos_3', color='grey')\
# ... .closest()\
# ... .nested('ul')\
# ... .sibling('li', 'Pos_4', color='grey')\
# ... .sibling('li', 'Pos_5', color='grey')\
# ... .sibling('li', 'Pos_6', color='blue')\
# ... .closest()\
# ... .closest()\
# ... .nested('main', class_='itembox')\
# ... .nested('div', class_='item', color='#f1f2f3')\
# ... .nested('ul')\
# ... .sibling('li', 'Pos_4', color='grey')\
# ... .sibling('li', 'Pos_5', color='grey')\
# ... .sibling('li', 'Pos_6', color='blue')\
# ... .closest()\
# ... .nested('div', class_='item', color='#f1f2f4')\
# ... .nested('ul')\
# ... .sibling('li', 'Pos_4', color='grey')\
# ... .sibling('li', 'Pos_5', color='grey')\
# ... .sibling('li', 'Pos_6', color='blue')\
# ... .build()
# >>>
# >>> print(html)
# <html >
  # <body bg="yellow" font="sans">Main
    # <header bg="green" fontsize="20px">
      # <div border="1px sold white">
        # <ul >
          # <li color="grey">Pos_1</li>
          # <li color="blue">Pos_2</li>
          # <li color="grey">Pos_3</li>
        # </ul>
        # <ul >
          # <li color="grey">Pos_4</li>
          # <li color="grey">Pos_5</li>
          # <li color="blue">Pos_6</li>
        # </ul>
      # </div>
      # <main class_="itembox">
        # <div class_="item" color="#f1f2f3">
          # <ul >
            # <li color="grey">Pos_4</li>
            # <li color="grey">Pos_5</li>
            # <li color="blue">Pos_6</li>
          # </ul>
          # <div class_="item" color="#f1f2f4">
            # <ul >
              # <li color="grey">Pos_4</li>
              # <li color="grey">Pos_5</li>
              # <li color="blue">Pos_6</li>
            # </ul>
          # </div>
        # </div>
      # </main>
    # </header>
  # </body>
# </html>
# >>>
