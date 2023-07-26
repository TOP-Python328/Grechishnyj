number = input('Номер билета: ')

number_left = [int(n) for n in number[:3]]
number_right = [int(n) for n in number[3:]]

print('Счастливый:', 'да' if sum(number_left) == sum(number_right) else 'нет')

# Номер билета: 192837
# Счастливый: нет

# Номер билета: 183534
# Счастливый: да

# Номер билета: 401367
# Счастливый: нет

# Номер билета: 115223
# Счастливый: да