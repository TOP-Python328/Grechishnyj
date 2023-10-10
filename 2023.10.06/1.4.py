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
    def pick(cls, number: int, word: str) -> str:
        """Метод возвращает согласованное существительное с числом.
    
        :param number: число для согласования.
        :param word: существительное для согласования.
        :return: согласованное с числом существительное. 
        """
        
        print(cls.words[word])
     
     
    @classmethod
    def save_words(cls, word1: str = None) -> None:
        """Метод запрашивает в stdin слова, добавляет их в words и дописывает в файл."""









# ======================================================================================

       

# with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
    # file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    # file_writer.writerow(["Имя", "Класс", "Возраст"])
    # file_writer.writerow(["Женя", "3", "10"])    