num_first = int('1' + '0' * (int(input('Введите разрядность: ')) - 1))
numbers = list(i for i in range(num_first, num_first * 10))
digits_simple = []

for num in numbers:
    cnt = 0
    for i in range(1, num + 1):
        if not num % i:
            cnt += 1         
    if cnt == 2:
        digits_simple.append(num)

print(f'Простых чисел: {len(digits_simple)}')     
        
# Введите разрядность: 1
# Простых чисел: 4

# Введите разрядность: 2
# Простых чисел: 21

# Введите разрядность: 3
# Простых чисел: 143   