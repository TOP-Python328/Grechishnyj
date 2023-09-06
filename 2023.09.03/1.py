from pathlib import Path
from sys import path

def list_files(catalog_path: str) -> tuple[str] | None:
    """Функция возвращает кортеж с именами файлов по переданному пути"""
   
    catalog = Path(path[0]) / catalog_path
  
    try:
        files_names = tuple(file.name for file in filter(lambda f: f.is_file(), catalog.iterdir()))
        return files_names
        
    except FileNotFoundError:
        return None


# >>> list_files(r'D:\temp\home\2023.09.03\data')
# ('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')

# >>> print(list_files(r'D:\temp\home\2023.09.03\none'))
# None