from pathlib import Path
from csv import reader, writer

class CountableNouns:
    """Интерфейс для работы с файловой базой существительных.
    
    :attr db_path: путь к файлу с базой существительных.
    :attr words: соответсвие между существительным в единственном числе и кортежем из двух словоформ.
    :method pick: возвращает согласованное существительное с числом.
    :method save_words: запрашивает в stdin слова, добавляет в words и дописывает в файл.
    """
    
    db_path: Path = None
    words: dict[str, tuple[str, str]] = []
    
    
    @classmethod
    def pick(cls, number: int, word: str) -> str:
        """Метод возвращает согласованное существительное с числом.
    
        :param number: число для согласования.
        :param word: существительное для согласования.
        :return: согласованное с числом существительное. 
        """
        
    @classmethod
    def save_words(cls, word1: str = None) -> None:
        """Метод запрашивает в stdin слова, добавляет их в words и дописывает в файл."""









# ======================================================================================

# with open("classmates.csv", encoding='utf-8') as r_file:
    # # Создаем объект reader, указываем символ-разделитель ","
    # file_reader = csv.reader(r_file, delimiter = ",")
    # # Счетчик для подсчета количества строк и вывода заголовков столбцов
    # count = 0
    # # Считывание данных из CSV файла
    # for row in file_reader:
        # if count == 0:
            # # Вывод строки, содержащей заголовки для столбцов
            # print(f'Файл содержит столбцы: {", ".join(row)}')
        # else:
            # # Вывод строк
            # print(f'    {row[0]} - {row[1]} и он родился в {row[2]} году.')
        # count += 1
    # print(f'Всего в файле {count} строк.')       

# with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
    # file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    # file_writer.writerow(["Имя", "Класс", "Возраст"])
    # file_writer.writerow(["Женя", "3", "10"])    