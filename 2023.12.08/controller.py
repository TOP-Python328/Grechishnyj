"""
Controller (MVC): управляющий модуль.
"""
import model
import view

class Application:
    
    @staticmethod
    def save_email(email: str) -> None:
        """Сохранение Email в файл."""
        model.FileIO.add_email(email.email)
        view.CLI.success_save()

    @classmethod
    def receive_email(cls) -> None:
        """Получение адресов email от пользователя."""
        while user_input := view.CLI.get_email():
            try:
                email = model.Email(user_input)
                cls.save_email(email)
            except Exception:
                view.CLI.incorrect_email()
                continue