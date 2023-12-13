"""
View (MVC): представление с интерфейсом командной строки.
"""
from enum import Enum

class CLI:
    """Взаимодействие с пользователем."""
    
    @staticmethod
    def show_header() -> None:
        """Заствка."""
        print("\nПрограмма запрашивает и сохраняет email адреса!")
    
    @staticmethod
    def get_email() -> str:
        """Запрашивает у пользователя email."""
        return input("\n\tВведите email: > ")
 
    @staticmethod
    def incorrect_email() -> None:
        """Вывод в stdout сообщения о некорректном email."""
        print("\nВы ввели некорректный email!")

    @staticmethod
    def success_save() -> None:
        """Вывод в stdout сообщения о некорректном email."""
        print("\nEmail успешно сохранен в файл!")

    @staticmethod
    def bye() -> None:
        """Сообщение об окончании работы программы."""
        print("\nРабота программы завершена.")