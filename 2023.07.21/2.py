numbers = (
    int(input('> ')) 
    for _ in range(int(input('Введите количество чисел: ')))
)

print(f'Сумма положительных: {sum((i for i in numbers if i > 0))}')

# stdin
# Введите количество чисел: 6
# > 3
# > -5
# > 1
# > 10
# > -1
# > 8

# stdout
# Сумма положительных: 22


# ===========================================================

# Первоначальный вариант

# n = int(input('Введите количество чисел: '))
# nums = []
# for i in range(n):
#     k = int(input(' > '))
#     if k > 0:
#         nums.append(k)
# print(sum(nums))