from pathlib import Path
from sys import path
from csv import reader, writer

class CountableNouns:
    """Интерфейс для работы с файловой базой существительных.
    
    :attr db_path: путь к файлу с базой существительных.
    :attr words: соответсвие между существительным в единственном числе и кортежем из двух словоформ.
    :method pick: возвращает согласованное существительное с числом.
    :method save_words: запрашивает в stdin слова, добавляет в words и дописывает в файл.
    """
    
    db_path: Path = Path(path[0]) / 'words.csv'
    words: dict[str, tuple[str, str]] = {}
    with open(db_path, encoding='utf-8') as filein:
        file_reader = reader(filein, delimiter = ',')
        words = {line[0]: tuple(line[1:]) for line in file_reader}
    
    
    @classmethod
    def save_words(cls, word1: str = None) -> None:
        """Метод запрашивает в stdin слова, добавляет их в words и дописывает в файл.
        
        :param word1: слово добавляемое в словарь words
        """
        new_words = ['один', 'два', 'пять']
        template = 'введите слово, согласующееся с числительным "{}": '
        
        if not word1:
            new_words = [input(template.format(nw)) for nw in new_words]
            cls.words[new_words[0]] = tuple(new_words[1:])
        else:
            new_words = [input(template.format(nw)) for nw in new_words[1:]]
            cls.words[word1] = tuple(new_words)
    
    
    @classmethod
    def pick(cls, number: int, word: str) -> str:
        """Метод возвращает согласованное существительное с числом.
    
        :param number: число для согласования.
        :param word: существительное для согласования.
        :return: согласованное с числом существительное. 
        """
        if not word in cls.words:
            cls.save_words(word)
        
        choice_words = word, *cls.words[word]
        last_digit = number % 10
        decade_digit = number % 100 // 10
        
        if decade_digit == 1:
            return choice_words[2]
        if last_digit == 1:
            return choice_words[0]
        
        if 1 < last_digit < 5:
            return choice_words[1]
        else:
            return choice_words[2]
            
           




