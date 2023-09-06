from pathlib import Path
from sys import path
from utils import clear_text

def search_context(keyword: str, *key_words: str, n: int=0) -> list[dict]:
    """
        Функция осуществляет поиск в текстовых файлах строк, содержащих ключевые слова
        Только для файлов с расширением .txt
    """
    
    files = (Path(path[0]) / 'data').glob('*.txt')
    kws = keyword, *key_words
    data_list = list()
    
    for file in files:
        print('=====================')
        print(file)
        
        with open(file, 'r', encoding='utf-8') as file_content:
            text_content = file_content.read()
            
        text = clear_text(text_content)    
        lines = text.split('\n')
        filename = file.name
        number_line = 1
        
        for line in lines:
            words = line.split(' ')
            
            for word in words:
                if word.lower() in kws:
                    data_list.append({
                        'keyword': word,
                        'filename': filename,
                        'line': number_line,
                        'context': n,
                        'text': f'{line[:10]}... ...{line[-10:]}'
                    })
            
            number_line += 1
        
    print(*data_list, sep='\n')
    
# >>> search_context('мысль', 'мысли')
# =====================
# D:\temp\home\2023.09.03\data\E3ln1.txt
# =====================
# D:\temp\home\2023.09.03\data\le1UO.txt
# =====================
# D:\temp\home\2023.09.03\data\r62Bf.txt
# {'keyword': 'мысль', 'filename': 'E3ln1.txt', 'line': 147, 'context': 0, 'text': '  А знаете... ...углубиться'}
# {'keyword': 'мысли', 'filename': 'E3ln1.txt', 'line': 163, 'context': 0, 'text': 'Манилов до... ...мого ужина'}
# {'keyword': 'Мысль', 'filename': 'E3ln1.txt', 'line': 163, 'context': 0, 'text': 'Манилов до... ...мого ужина'}
# {'keyword': 'мысли', 'filename': 'le1UO.txt', 'line': 13, 'context': 0, 'text': 'Как и все ... ...альванизма'}
# {'keyword': 'мысль', 'filename': 'r62Bf.txt', 'line': 19, 'context': 0, 'text': 'Вдруг он в... ...о в глазах'}
# {'keyword': 'мысль', 'filename': 'r62Bf.txt', 'line': 19, 'context': 0, 'text': 'Вдруг он в... ...о в глазах'}
# {'keyword': 'мысль', 'filename': 'r62Bf.txt', 'line': 19, 'context': 0, 'text': 'Вдруг он в... ...о в глазах'}
# {'keyword': 'Мысли', 'filename': 'r62Bf.txt', 'line': 61, 'context': 0, 'text': 'Несмотря н... ...ем сызнова'}
# {'keyword': 'мысль', 'filename': 'r62Bf.txt', 'line': 63, 'context': 0, 'text': 'А куда ж я... ...мечательно'}