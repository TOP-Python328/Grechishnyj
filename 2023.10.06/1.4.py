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
        else:
            new_words = [input(template.format(nw)) for nw in new_words[1:]]
            new_words.insert(0, word1)
        cls.words[new_words[0]] = tuple(new_words[1:])
        
        with open(cls.db_path, mode="a", encoding='utf-8') as fileout:
            file_writer = writer(fileout, delimiter = ",", lineterminator="\n")
            file_writer.writerow(new_words)

    
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
        
        if decade_digit == 1 or last_digit > 4:
            return choice_words[2]
        if last_digit == 1:
            return choice_words[0]
        return choice_words[1]
   
 

# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней')}
# >>> CountableNouns.pick(15, 'карандаш')
# введите слово, согласующееся с числительным "два": карандаша
# введите слово, согласующееся с числительным "пять": карандашей
# 'карандашей'
# >>>
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'карандаш': ('карандаша', 'карандашей')}
# >>>
# >>> CountableNouns.save_words()
# введите слово, согласующееся с числительным "один": рубль
# введите слово, согласующееся с числительным "два": рубля
# введите слово, согласующееся с числительным "пять": рублей
# >>>
# >>> CountableNouns.pick(103, 'рубль')
# 'рубля'
# >>>
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'карандаш': ('карандаша', 'карандашей'), 'рубль': ('рубля', 'рублей')}
# >>>
# >>> print(CountableNouns.db_path.read_text(encoding='utf-8'))
# год,года,лет
# месяц,месяца,месяцев
# день,дня,дней
# карандаш,карандаша,карандашей
# рубль,рубля,рублей
# >>> CountableNouns.pick(11, 'рубль')
# 'рублей'
# >>> CountableNouns.pick(2, 'рубль')
# 'рубля'
# >>> CountableNouns.pick(5, 'рубль')
# 'рублей'

