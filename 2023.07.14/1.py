num_1 = float(input('Число 1: '))
num_2 = float(input('Число 2: '))
num_3 = float(input('Число 3: '))

total = num_1 if num_1 > 0 else 0
total += num_2 if num_2 > 0 else 0
total += num_3 if num_3 > 0 else 0

print(f'Сумма: {total}')


# Число 1: 4
# Число 2: -22
# Число 3: 1.5
# Сумма: 5.5


# ИТОГ: отлично — 3/3
