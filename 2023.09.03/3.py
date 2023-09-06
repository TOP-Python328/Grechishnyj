from pathlib import Path
from sys import path


def ask_for_file():
    """Функция запрашивает путь к файлу и копирует этот файл"""
    
    while True:
        user_path = input(' > Введите путь к файлу: ')
        file_path = Path(path[0]) / user_path

        if file_path.is_file():
            break
        else:
            print('Файл не найден!')
     
    print(f'{file_path.name=}')     
    
