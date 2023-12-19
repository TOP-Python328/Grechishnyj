from pytest import mark
import controller 
import model

Application = controller.Application()


data = [
    'email', 
    '12345@1234.12',
    'qwert@mail.ru',
    'q123_!F@..ru',
    'q123_!F@gmail.com',
    'q123_!F@yandex.ru',
    '',
    'почта@mail.ru',
    'good@adress.py'
]


@mark.parametrize('email', data)
def test_receive_email(email):
    try:
        # print(email)
        email = model.Email(email)
        Application.save_email(email)
        assert True
    except:
        assert False


# 11:22:53 > pytest -v 2023.12.08\test.py
# ======================================= test session starts =======================================
# platform win32 -- Python 3.11.3, pytest-7.4.3, pluggy-1.3.0 -- C:\Python311\python.exe
# cachedir: .pytest_cache
# rootdir: D:\temp\home
# collected 9 items

# 2023.12.08/test.py::test_receive_email[email] FAILED                                         [ 11%]
# 2023.12.08/test.py::test_receive_email[12345@1234.12] FAILED                                 [ 22%]
# 2023.12.08/test.py::test_receive_email[qwert@mail.ru] PASSED                                 [ 33%]
# 2023.12.08/test.py::test_receive_email[q123_!F@..ru] FAILED                                  [ 44%]
# 2023.12.08/test.py::test_receive_email[q123_!F@gmail.com] FAILED                             [ 55%]
# 2023.12.08/test.py::test_receive_email[q123_!F@yandex.ru] FAILED                             [ 66%]
# 2023.12.08/test.py::test_receive_email[] FAILED                                              [ 77%]
# 2023.12.08/test.py::test_receive_email[\u043f\u043e\u0447\u0442\u0430@mail.ru] FAILED        [ 88%]
# 2023.12.08/test.py::test_receive_email[good@adress.py] PASSED                                [100%]

# ============================================ FAILURES =============================================
# ____________________________________ test_receive_email[email] ____________________________________

# email = 'email'

    # @mark.parametrize('email', data)
    # def test_receive_email(email):
        # try:
# >           email = model.Email(email)

# 2023.12.08\test.py:28:
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 2023.12.08\model.py:18: in __init__
    # self.email = email
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# self = <model.Email object at 0x00000215DD4EDA50>, value = 'email'

    # @email.setter
    # def email(self, value: str):
        # """Проверяет, является ли переданныя строка корректным email адресом, и устанавливает значение поля __email."""
        # if self.pattern.fullmatch(value):
            # self.__email = value
        # else:
# >           raise ValueError(f'Invalid email address: {value}')
# E           ValueError: Invalid email address: email

# 2023.12.08\model.py:31: ValueError

# During handling of the above exception, another exception occurred:

# email = 'email'

    # @mark.parametrize('email', data)
    # def test_receive_email(email):
        # try:
            # print(email)
            # email = model.Email(email)
            # Application.save_email(email)
            # assert True
        # except:
# >           assert False
# E           assert False

# 2023.12.08\test.py:32: AssertionError
# -------------------------------------- Captured stdout call ---------------------------------------
# email
# ________________________________ test_receive_email[12345@1234.12] ________________________________

# email = '12345@1234.12'

    # @mark.parametrize('email', data)
    # def test_receive_email(email):
        # try:
# >           email = model.Email(email)

# 2023.12.08\test.py:28:
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 2023.12.08\model.py:18: in __init__
    # self.email = email
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# self = <model.Email object at 0x00000215DD43DED0>, value = '12345@1234.12'

    # @email.setter
    # def email(self, value: str):
        # """Проверяет, является ли переданныя строка корректным email адресом, и устанавливает значение поля __email."""
        # if self.pattern.fullmatch(value):
            # self.__email = value
        # else:
# >           raise ValueError(f'Invalid email address: {value}')
# E           ValueError: Invalid email address: 12345@1234.12

# 2023.12.08\model.py:31: ValueError

# During handling of the above exception, another exception occurred:

# email = '12345@1234.12'

    # @mark.parametrize('email', data)
    # def test_receive_email(email):
        # try:
            # email = model.Email(email)
            # Application.save_email(email)
            # assert True
        # except:
# >           assert False
# E           assert False

# 2023.12.08\test.py:32: AssertionError
# -------------------------------------- Captured stdout call ---------------------------------------
# 12345@1234.12
# ________________________________ test_receive_email[q123_!F@..ru] _________________________________

# email = 'q123_!F@..ru'

    # @mark.parametrize('email', data)
    # def test_receive_email(email):
        # try:
# >           email = model.Email(email)

# 2023.12.08\test.py:28:
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 2023.12.08\model.py:18: in __init__
    # self.email = email
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# self = <model.Email object at 0x00000215DD50E2D0>, value = 'q123_!F@..ru'

    # @email.setter
    # def email(self, value: str):
        # """Проверяет, является ли переданныя строка корректным email адресом, и устанавливает значение поля __email."""
        # if self.pattern.fullmatch(value):
            # self.__email = value
        # else:
# >           raise ValueError(f'Invalid email address: {value}')
# E           ValueError: Invalid email address: q123_!F@..ru

# 2023.12.08\model.py:31: ValueError

# During handling of the above exception, another exception occurred:

# email = 'q123_!F@..ru'

    # @mark.parametrize('email', data)
    # def test_receive_email(email):
        # try:
            # email = model.Email(email)
            # Application.save_email(email)
            # assert True
        # except:
# >           assert False
# E           assert False

# 2023.12.08\test.py:32: AssertionError
# -------------------------------------- Captured stdout call ---------------------------------------
# q123_!F@..ru
# ______________________________ test_receive_email[q123_!F@gmail.com] ______________________________

# email = 'q123_!F@gmail.com'

    # @mark.parametrize('email', data)
    # def test_receive_email(email):
        # try:
# >           email = model.Email(email)

# 2023.12.08\test.py:28:
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 2023.12.08\model.py:18: in __init__
    # self.email = email
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# self = <model.Email object at 0x00000215DECF0E50>, value = 'q123_!F@gmail.com'

    # @email.setter
    # def email(self, value: str):
        # """Проверяет, является ли переданныя строка корректным email адресом, и устанавливает значение поля __email."""
        # if self.pattern.fullmatch(value):
            # self.__email = value
        # else:
# >           raise ValueError(f'Invalid email address: {value}')
# E           ValueError: Invalid email address: q123_!F@gmail.com

# 2023.12.08\model.py:31: ValueError

# During handling of the above exception, another exception occurred:

# email = 'q123_!F@gmail.com'

    # @mark.parametrize('email', data)
    # def test_receive_email(email):
        # try:
            # email = model.Email(email)
            # Application.save_email(email)
            # assert True
        # except:
# >           assert False
# E           assert False

# 2023.12.08\test.py:32: AssertionError
# -------------------------------------- Captured stdout call ---------------------------------------
# q123_!F@gmail.com
# ______________________________ test_receive_email[q123_!F@yandex.ru] ______________________________

# email = 'q123_!F@yandex.ru'

    # @mark.parametrize('email', data)
    # def test_receive_email(email):
        # try:
# >           email = model.Email(email)

# 2023.12.08\test.py:28:
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 2023.12.08\model.py:18: in __init__
    # self.email = email
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# self = <model.Email object at 0x00000215DED06950>, value = 'q123_!F@yandex.ru'

    # @email.setter
    # def email(self, value: str):
        # """Проверяет, является ли переданныя строка корректным email адресом, и устанавливает значение поля __email."""
        # if self.pattern.fullmatch(value):
            # self.__email = value
        # else:
# >           raise ValueError(f'Invalid email address: {value}')
# E           ValueError: Invalid email address: q123_!F@yandex.ru

# 2023.12.08\model.py:31: ValueError

# During handling of the above exception, another exception occurred:

# email = 'q123_!F@yandex.ru'

    # @mark.parametrize('email', data)
    # def test_receive_email(email):
        # try:
            # email = model.Email(email)
            # Application.save_email(email)
            # assert True
        # except:
# >           assert False
# E           assert False

# 2023.12.08\test.py:32: AssertionError
# -------------------------------------- Captured stdout call ---------------------------------------
# q123_!F@yandex.ru
# ______________________________________ test_receive_email[] _______________________________________

# email = ''

    # @mark.parametrize('email', data)
    # def test_receive_email(email):
        # try:
# >           email = model.Email(email)

# 2023.12.08\test.py:28:
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 2023.12.08\model.py:18: in __init__
    # self.email = email
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# self = <model.Email object at 0x00000215DED0A690>, value = ''

    # @email.setter
    # def email(self, value: str):
        # """Проверяет, является ли переданныя строка корректным email адресом, и устанавливает значение поля __email."""
        # if self.pattern.fullmatch(value):
            # self.__email = value
        # else:
# >           raise ValueError(f'Invalid email address: {value}')
# E           ValueError: Invalid email address:

# 2023.12.08\model.py:31: ValueError

# During handling of the above exception, another exception occurred:

# email = ''

    # @mark.parametrize('email', data)
    # def test_receive_email(email):
        # try:
            # email = model.Email(email)
            # Application.save_email(email)
            # assert True
        # except:
# >           assert False
# E           assert False

# 2023.12.08\test.py:32: AssertionError
# -------------------------------------- Captured stdout call ---------------------------------------

# ___________________ test_receive_email[\u043f\u043e\u0447\u0442\u0430@mail.ru] ____________________

# email = 'почта@mail.ru'

    # @mark.parametrize('email', data)
    # def test_receive_email(email):
        # try:
# >           email = model.Email(email)

# 2023.12.08\test.py:28:
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# 2023.12.08\model.py:18: in __init__
    # self.email = email
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# self = <model.Email object at 0x00000215DECF2AD0>, value = 'почта@mail.ru'

    # @email.setter
    # def email(self, value: str):
        # """Проверяет, является ли переданныя строка корректным email адресом, и устанавливает значение поля __email."""
        # if self.pattern.fullmatch(value):
            # self.__email = value
        # else:
# >           raise ValueError(f'Invalid email address: {value}')
# E           ValueError: Invalid email address: почта@mail.ru

# 2023.12.08\model.py:31: ValueError

# During handling of the above exception, another exception occurred:

# email = 'почта@mail.ru'

    # @mark.parametrize('email', data)
    # def test_receive_email(email):
        # try:
            # email = model.Email(email)
            # Application.save_email(email)
            # assert True
        # except:
# >           assert False
# E           assert False

# 2023.12.08\test.py:32: AssertionError
# -------------------------------------- Captured stdout call ---------------------------------------
# почта@mail.ru
# ===================================== short test summary info =====================================
# FAILED 2023.12.08/test.py::test_receive_email[email] - assert False
# FAILED 2023.12.08/test.py::test_receive_email[12345@1234.12] - assert False
# FAILED 2023.12.08/test.py::test_receive_email[q123_!F@..ru] - assert False
# FAILED 2023.12.08/test.py::test_receive_email[q123_!F@gmail.com] - assert False
# FAILED 2023.12.08/test.py::test_receive_email[q123_!F@yandex.ru] - assert False
# FAILED 2023.12.08/test.py::test_receive_email[] - assert False
# FAILED 2023.12.08/test.py::test_receive_email[\u043f\u043e\u0447\u0442\u0430@mail.ru] - assert False
# =================================== 7 failed, 2 passed in 0.29s ===================================