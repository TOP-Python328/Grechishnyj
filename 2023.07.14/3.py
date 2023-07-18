year, answers = int(input('Введите год: ')), ['нет', 'да']
flag = year % 100 and not year % 4 or not year % 400
print(f'Високосный: {answers[flag]}')

# Введите год: 2100
# Високосный: нет

# Введите год: 2024
# Високосный: да
