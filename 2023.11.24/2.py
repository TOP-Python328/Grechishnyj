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
    
    def __init__(self, name: str, value: str = ''):
        self.name = name
        self.value = value
        self.__nested: list[HTMLTag] = []
    
    def nested(self, html_tag: Self):
        """Добавляет вложенный тег к текущему."""
        self.__nested.append(html_tag)
    
    def __str(self, indent_level: int) -> str:
        """Рекурсивно формирует строку с текущим и всеми вложенными тегами."""
        margin = ' ' * indent_level * self.default_indent_spaces
        eol = ''
        result = f"{margin}<{self.name}>{self.value}"
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
    
    def nested(self, name: str, value: str = '') -> Self:
        """Добавляет вложенный тег к текущему тегу и возвращает строитель для вложенного тега."""
        tag = HTMLTag(name, value)
        self.root.nested(tag)
        return HTMLBuilder(tag, parent=self)
    
    def sibling(self, name: str, value: str = '') -> Self:
        """Добавляет вложенный тег к текущему тегу и возвращает текущий строитель."""
        tag = HTMLTag(name, value)
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
# ... .nested('head')\
# ... .sibling('title')\
# ... .sibling('script')\
# ... .sibling('style')\
# ... .closest()\
# ... .nested('body')\
# ... .nested('header')\
# ... .nested('div', 'Menu')\
# ... .nested('ul')\
# ... .sibling('li')\
# ... .closest()\
# ... .nested('main')\
# ... .build()
# >>>
# >>> write_html_file(html)
# >>>
# >>> print(html)
# <html>
  # <head>
    # <title></title>
    # <script></script>
    # <style></style>
  # </head>
  # <body>
    # <header>
      # <div>Menu
        # <ul>
          # <li></li>
        # </ul>
        # <main></main>
      # </div>
    # </header>
  # </body>
# </html>
