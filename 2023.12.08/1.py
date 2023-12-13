"""
Application (MVC): Главный исполняющий модуль. Точка входа.
"""

import controller
import view

def start() -> None:
    """Старт программы."""
    view.CLI.show_header()
    
def mainloop():
    """Главный цикл программы"""
    controller.Application.receive_email()
    
def end():
    """Завершение работы программы"""
    view.CLI.bye()

if __name__ == '__main__':
    start()
    mainloop()
    end()
    
# Программа запрашивает и сохраняет email адреса!

        # Введите email: > 123@mail.ru

# Email успешно сохранен в файл!

        # Введите email: > 123mail.ru

# Вы ввели некорректный email!

        # Введите email: > 1

# Вы ввели некорректный email!

        # Введите email: > 'd'@mail.ru

# Вы ввели некорректный email!

        # Введите email: > @mail.ru

# Вы ввели некорректный email!

        # Введите email: > 123@mail.ru.com

# Email успешно сохранен в файл!

        # Введите email: >

# Работа программы завершена.