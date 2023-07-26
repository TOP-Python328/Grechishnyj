num, num_divisors = int(input('Введите целое число:')), list()

i = 1
while i ** 2 <= num:
    if not num % i:
        num_divisors.append(i)
        if i != num//i:
            num_divisors.append(num//i)
    i += 1
    
print(f'Сумма всех делителей: {sum(num_divisors)}')


# Введите целое число:5
# Сумма всех делителей: 6

# Введите целое число:17
# Сумма всех делителей: 18

# Введите целое число:50
# Сумма всех делителей: 93