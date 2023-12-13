"""
Controller (MVC): управляющий модуль.
"""
import model
import view

class Application:
    
    @staticmethod
    def save_email(email: str) -> None:
        """Сохранение Email в файл."""
        model.FileIO.add_email(email)
        print(f'save_email {email}')
        
    @staticmethod
    def receive_email() -> None:
        """Получение адресов email от пользователя."""
        while user_input := view.CLI.get_email():
            try:
                email = model.Email(user_input)
                model.FileIO.add_email(email.email)
                view.CLI.success_save()
            except Exception:
                view.CLI.incorrect_email()
                continue