numbers = int(input('stdin: '))
num_1 = num_2 = 1
sequence = list()

for _ in range(numbers):
    sequence.append(num_1)
    num_1, num_2 = num_2, num_1 + num_2
    
print('stdout: ', end='')
print(*sequence)


# stdin: 1
# stdout: 1

# stdin: 7
# stdout: 1 1 2 3 5 8 13

# stdin: 17
# stdout: 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597


# ИТОГ: отлично — 5/5
