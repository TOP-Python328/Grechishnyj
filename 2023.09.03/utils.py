from shutil import get_terminal_size, copy2
from pathlib import Path
from sys import path, modules

def important_message(text: str) -> str:
    """Функция возвращает форматированную строку сообщения в рамке по ширине CLI"""
    
    width = get_terminal_size().columns
    inside = width - 6
    
    char_line = '='
    char_spot = '#'
    char_empt = ' '
    
    bord_line = char_spot + char_line * (width - 2) + char_spot
    empt_line = char_spot + char_empt * (width - 2) + char_spot
    
    text_main = bord_line + empt_line
    
    start = 0
    batch = inside
    text_split = []
    
    while batch < len(text):
        text_split.append(text[start:batch])
        start, batch = batch,  batch + inside
    text_split.append(text[start:])
    
    for text_part in text_split:
        if len(text_part) < inside:
            start_remains = int((inside - len(text_part)) / 2) + 2
            end_remains = inside - start_remains - len(text_part) + 4
        else:
            start_remains = end_remains = 2
        
        text_main += (
            char_spot + 
            char_empt * start_remains +
            text_part +
            char_empt * end_remains +
            char_spot
        )
            
    text_main += (empt_line + bord_line)
    return text_main
    
    # >>> important_message('Функция возвращает форматированную строк
    # у сообщения в рамке по ширине CLI')
    # '#=============================================================
    # ##                                                             
    # ##  Функция возвращает форматированную строку сообщения в рам  
    # ##                      ке по ширине CLI                       
    # ##                                                             
    # ##=============================================================
    # #'

def load_file(file_path: str | Path) -> Path:
    """
        Функция копирует файл в каталог задания
        Возвращает объект скопированного модуля
    """
    
    copy_name = 'copy_' + file_path.name
    path_out = Path(path[0]) / copy_name
    copy2(file_path, path_out)

    return path_out
    

    # ============================================================
    # Первый вариант копирования - менеджер контекста
    
    # with open(file_path, 'r', encoding='utf-8') as file_content:
    #     text = file_content.read()
    
    # with open(r'D:\temp\home\2023.09.03\copy2.py', 'w', encoding='utf-8') as file_out:
    #     file_out.write(text)
    # ============================================================


def clear_text(text_fragment: str) -> str:
    """docstring"""
    
    text_clear = ''
    punctuations = '.,;:/?<>«»"\'!@#$%^&*()[]{}=+-_|~`1234567890…'
    text = filter(lambda char: char not in punctuations, text_fragment)
    
    for char in text:
        text_clear += char
    
    return text_clear



    
def get_context(text: str) -> dict:
    """docstring"""
    dict_context = {
        'keyword': None,
        'filename': None,
        'line': None,
        'context': None,
        'text': None
    }
    
    