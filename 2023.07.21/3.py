num, num_divisors = int(input('Введите целое число:')), list()

# ПЕРЕИМЕНОВАТЬ: имена переменных i, j, k традиционно используются только для индексов — здесь вы работаете с делителем
# ИСПРАВИТЬ: единица и само число всегда являются делителями, для них не нужно выполнять все проверки ниже — оптимизируйте
i = 1
while i ** 2 <= num:
    if not num % i:
        # КОММЕНТАРИЙ: оператор += работает быстрее, чем метод append()
        num_divisors.append(i)
        # УДАЛИТЬ: эта проверка может стать актуальной только тогда, когда i**2 == num, что не для каждого числа верно, но выполняете вы её на каждой итерации — оптимизируйте
        if i != num // i:
            num_divisors.append(num // i)
    i += 1
    
print(f'Сумма всех делителей: {sum(num_divisors)}')


# Введите целое число:5
# Сумма всех делителей: 6

# Введите целое число:17
# Сумма всех делителей: 18

# Введите целое число:50
# Сумма всех делителей: 93


# ИТОГ: хорошо, но можно лучше — 4/6
