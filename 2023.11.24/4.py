from dataclasses import dataclass
from os import name as os_name
from typing import Self
from sys import path


if os_name == 'nt':
    PATH_SEP = '\\'
else:
    PATH_SEP = '/'


@dataclass
class File:
    """Файл в файловой системе."""
    name: str
    dir: str
    
    @property
    def extension(self) -> str:
        return ''.join(self.name.rsplit('.', 1)[1:])
    
    def ls(self) -> str:
        return self.dir_path + PATH_SEP + self.name


class Folder(list):
    """Каталог в файловой системе. Может содержать вложенные каталоги и файлы."""
    
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.dir_path = path[0]
  
    def ls(self) -> str:
        return self.dir_path + PATH_SEP + self.name
 
    def add_nested(self, other: Self | File) -> None:
        """Добавить(переместить) в каталог элемент (файл либо каталог)"""
        if hasattr(other, 'folder'):
            other.folder.remove(other)
        other.folder = None
        other.dir_path = self.ls()
        other.folder = self
        self.append(other)


def ls(*objects: File | Folder) -> str:
    for obj in objects:
        print(obj.ls(), obj.name, obj.dir_path)


# D:\temp\home
 # 13:17:27 > python -i 2023.11.24\4.py
# >>> file1 = File('file1', path[0])
# >>> file2 = File('file2', path[0])
# >>> file3 = File('file3', path[0])
# >>> file4 = File('file4', path[0])
# >>> file5 = File('file5', path[0])
# >>> file6 = File('file6', path[0])
# >>> file7 = File('file7', path[0])
# >>>
# >>> folder1 = Folder('folder1')
# >>> folder2 = Folder('folder2')
# >>> folder3 = Folder('folder3')
# >>>
# >>> folder1.add_nested(file1)
# >>> folder1.add_nested(file2)
# >>>
# >>> folder2.add_nested(file3)
# >>> folder2.add_nested(file4)
# >>> folder2.add_nested(file5)
# >>>
# >>> folder3.add_nested(file6)
# >>> folder3.add_nested(file7)
# >>>
# >>> for item in folder1:
# ...     print(item.name)
# ...
# file1
# file2
# >>>
# >>> for item in folder2:
# ...     print(item.name)
# ...
# file3
# file4
# file5
# >>>
# >>> for item in folder3:
# ...     print(item.name)
# ...
# file6
# file7
# >>>
# >>> folder3.add_nested(folder2)
# >>>
# >>> for item in folder3:
# ...     print(item.name)
# ...
# file6
# file7
# folder2
# >>>
# >>> folder3.add_nested(file5)
# >>> for item in folder3:
# ...     print(item.name)
# ...
# file6
# folder2
# file7
# file5
# >>>
# >>> for item in folder2:
# ...     print(item.name)
# ...
# file3
# file4
# >>>
# >>> objects = [file1, file2, file3, file4, file5, file6, file7, folder1, folder2, folder3]
# >>>
# >>> ls(*objects)
# D:\temp\home\2023.11.24\folder1\file1 file1 D:\temp\home\2023.11.24\folder1
# D:\temp\home\2023.11.24\folder1\file2 file2 D:\temp\home\2023.11.24\folder1
# D:\temp\home\2023.11.24\folder2\file3 file3 D:\temp\home\2023.11.24\folder2
# D:\temp\home\2023.11.24\folder2\file4 file4 D:\temp\home\2023.11.24\folder2
# D:\temp\home\2023.11.24\folder3\file5 file5 D:\temp\home\2023.11.24\folder3
# D:\temp\home\2023.11.24\folder3\file6 file6 D:\temp\home\2023.11.24\folder3
# D:\temp\home\2023.11.24\folder3\file7 file7 D:\temp\home\2023.11.24\folder3
# D:\temp\home\2023.11.24\folder1 folder1 D:\temp\home\2023.11.24
# D:\temp\home\2023.11.24\folder3\folder2 folder2 D:\temp\home\2023.11.24\folder3
# D:\temp\home\2023.11.24\folder3 folder3 D:\temp\home\2023.11.24