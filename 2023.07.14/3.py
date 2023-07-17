year, answers = int(input('Введите год: ')), ['нет', 'да']
flag = year % 100 and not year % 4 or not year % 400
print(answers[flag])

# Введите год: 2016
# 2016 год - високосный

# Введите год: 1900
# 1900 год - не високосный