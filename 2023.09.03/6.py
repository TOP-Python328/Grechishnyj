import data.vars as datavars
from pathlib import Path
from sys import path
from utils import important_message
from random import choice
from shutil import get_terminal_size
from time import perf_counter

# Наименование викторины
print(important_message(datavars.APP_TITLE))

# Получение данных из файла
file = Path(path[0]) / 'data/questions.quiz'
with open(file, 'r', encoding='utf-8') as data_file:
    text_file = data_file.read()
    
# Создание словаря вопрсов
questions = text_file.split('\n\n')
data = {}

for question_text in questions:
    question = question_text.split('\n')
    answers = question[1:]
    data[question[0]] = {
        f'answer{i+1}': {
            'number': answers[i][:1],
            'text': answers[i][3:-1] if answers[i][-1:] == '+' else answers[i][3:],
            'correct': True if answers[i][-1:] == '+' else False}
        for i in range(len(answers))}

# Процесс викрорины
user_answers = {}
user_total = 0

# Задаём вопросы
for _ in range(datavars.N):
    item = choice(list(data.items()))
    question_text = item[0]
    answers = item[1].values()
    print(question_text)
    
    # Получаем ответы
    time_start = perf_counter()
    for value in answers:
        print(f'{value["number"]}. {value["text"]}')
    
    user_answer = input(datavars.PROMPT)
    time_end = perf_counter()
    for value in answers:
        if user_answer == value["number"]:
            user_answers[question_text] = {
                'user_text': value["text"], 
                'user_correct': value["correct"],
                'time': round(time_end - time_start)}
            
    # Подсчет и вывод результатов
    user_time = user_answers[question_text]['time']
    user_result = user_answers[question_text]['user_correct']
    
    if not user_result:
        msg_result = 'Неверно...'
        msg_time = ''
    else:
        msg_result = 'Верно'
        if user_time > datavars.TIMER:
            msg_time = f', но недостаточно быстро ({user_time} c)'
            user_total += datavars.CORRECT_TIMEOUT
        else:
            msg_time = f'{datavars.ERR_PREFIX}({user_time} c)'
            user_total += datavars.CORRECT_TIME
    
    line = '='*get_terminal_size().columns
    message = msg_result + msg_time
    print(message, line, sep='\n')    

# Вывод итогового результата   
print(important_message(f'Ваш счет {user_total}')) 

# #==============================================================================================#
# #                                                                                              #
# #                                 ИСТОРИЧЕСКАЯ БЛИЦ-ВИКТОРИНА                                  #
# #                                                                                              #
# #==============================================================================================#

# Как звучит фамилия первого в мире создателя практически пригодного электромагнитного телеграфа – 
# прибора для передачи письменных сообщений по проводам?
# 1. Шиллинг
# 2. Пенс
# 3. Цент
# 4. Копейка
#  > 1
# Верно, но недостаточно быстро (16 c)
# ================================================================================================

# В каком российском городе во время Первой русской революции 1905 года был образован первый в Рос
# сии общегородской Совет рабочих депутатов?
# 1. Москва
# 2. Рязань
# 3. Вологда
# 4. Иваново
#  > 1
# Неверно...
# ================================================================================================

# Как назывались первые советские цветные телевизоры?
# 1. «Горизонт»
# 2. «Рубин»
# 3. «Электроника»
# 4. «ЗиЛ»
#  > 2
# Верно, но недостаточно быстро (7 c)
# ================================================================================================

# На какой улице располагался телецентр, откуда вышла в эфир первая в СССР телевизионная программа?
# 1. Шаболовка
# 2. Никольская
# 3. Академика Королёва
# 4. Мясницкая
#  > 3
# Неверно...
# ================================================================================================

# Первый российский аэродром – это:
# 1. Куликово поле
# 2. Марсово поле
# 3. Красная площадь
# 4. Ходынское поле
#  > 4
# Верно! (5 c)
# ================================================================================================

# #==============================================================================================#
# #                                                                                              #
# #                                         Ваш счет 40                                          #
# #                                                                                              #
# #==============================================================================================#