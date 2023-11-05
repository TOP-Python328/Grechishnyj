from urllib.request import urlopen, urlparse
from posixpath import basename
from json import loads as json_loads

from os.path import splitext
from pathlib import Path
from sys import path
from re import findall, S

url = f'https://www.python.org'
url2 = f'https://docs.python.org/3/py-modindex.html'
# url3 = f'https://www.world-art.ru/cinema/rating_top.php'


def json_from_html(url: str, template: str, encod: str='utf-8') -> Path:
    """Функция по заданному шаблону извлекает из HTML документа данные и помещает их в JSON файл"""
    html = urlopen(url).read().decode(encod)
    url_name = basename(urlparse(url).path)
    
    
    html_data = findall(template, html, S)
     
    html_text = '{\n' + ''.join(f'\t"{line[0]}": "{line[1]}",\n' for line in html_data) + '\n}'

    
    if url_name.endswith('.html'):
        json_name = url_name.replace('.html', '.json')
    else:
        json_name = f'{splitext(__loader__.path)[0]}.json' 

    json_path = Path(path[0]) / json_name
    
    
    with open(json_path, 'w', encoding='utf-8') as file_out:
        file_out.write(html_text)
        
    
    
    return json_path
    
films_pattern = (r'<tr .*?>'
                    r'<td .*?<a.*?>(?P<name>.*?)</a>.*?</td>'
                    r'<td .*?>(?P<rating>.*?)</td>')

modules_pattern = r'<tr>.+?>(\w+?)<.+?</td><td>.*?<em>(.*?)</em>'

json_from_html(url2, modules_pattern)
json_from_html(url, films_pattern)