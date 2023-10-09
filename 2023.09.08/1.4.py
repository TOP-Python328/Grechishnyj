from urllib.request import urlopen, urlparse
from os.path import splitext
from pathlib import Path

url = f'https://www.python.org'
url2 = f'https://docs.python.org/3/py-modindex.html'
# url3 = f'https://www.world-art.ru/cinema/rating_top.php'


# html = urlopen(URL).read().decode('utf-8')
# html = html.decode('utf-8')

def json_from_html(url: str, template: str, encod: str='utf-8') -> Path:
    """Функция по заданному шаблону извлекает из HTML документа данные и помещает их в JSON файл"""
    html = urlopen(url).read().decode(encod)
    
    parsed = urlparse(url)
    print(parsed)
    # root, ext = splitext(parsed.path)
    
    
    print(url)
    # print(file_name)
    
    json_path = ''
    
    return json_path
    
json_from_html(url, 'd')
json_from_html(url2, 'd')
# json_from_html(url3, 'd')


