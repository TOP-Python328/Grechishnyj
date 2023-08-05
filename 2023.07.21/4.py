num_first = int('1' + '0'*(int(input('Введите разрядность: ')) - 1))
numbers = list()

# ПЕРЕИМЕНОВАТЬ: имена переменных i, j, k традиционно используются только для индексов — здесь вы работаете с произвольными числами
for num in range(num_first, num_first*10):
    if ((not num % 2 or not num % 3 or not num % 5 or not num % 7 or
        not num % 11 or not num % 13 or not num % 17 or not num % 19) 
        and num not in [2, 3, 5, 7, 11, 13, 17, 19] or num == 1):
        continue
    numbers.append(num)

# УДАЛИТЬ: в контексте текущей задачи нет необходимости сохранять сами простые числа
count_simples_nums = 0

for num in numbers:
    cnt = 0
    # ПЕРЕИМЕНОВАТЬ: имена переменных i, j, k традиционно используются только для индексов — здесь вы работаете с делителем
    # ИСПРАВИТЬ: используйте более оптимальные алгоритм и диапазон для поиска делителей из предыдущей задачи — в данной задаче это ещё более актуально
    for divisor in range(2, num // 2):
        if not num % divisor:
            cnt += 1
            break
        # ДОБАВИТЬ: для определения, простое или нет число, необязательно находить все делители — если есть хоть один кроме единицы и самого числа, то число уже не простое — это сэкономит очень большое количество итераций
    if not cnt:
        count_simples_nums += 1

print(f'Простых чисел: {count_simples_nums}')

# Введите разрядность: 1
# Простых чисел: 4

# Введите разрядность: 2
# Простых чисел: 21

# Введите разрядность: 3
# Простых чисел: 143

# Введите разрядность: 4
# Простых чисел: 1061

# Введите разрядность: 5
# Простых чисел: 8363
# На 5-ти уже долго!!!

# КОММЕНТАРИЙ: а если бы оптимизировали, то посчитали бы и до шести разрядов без длительного ожидания — а вам уже и на трёх разрядах поди ждать пришлось =) впрочем, решето Эратосфена, конечно, ещё быстрее даже сокращённого перебора


# ИТОГ: хорошо, но можно лучше — 3/5
