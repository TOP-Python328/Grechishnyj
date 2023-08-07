fruits = list()

# КОММЕНТАРИЙ: отлично
while fruit := input('Введите название фрукта: '):
    fruits.append(fruit) 

fruits_format = ', '.join(fruits[:-1]) + ' и ' + fruits[-1] if len(fruits) > 1 else fruits[0]

# ИСПОЛЬЗОВАТЬ: ещё можно так
fruits_format = ', '.join(fruits[:-2] + [' и '.join(fruits[-2:])])

print(f'Форматированная строка: {fruits_format}') 


# Введите название фрукта: apple
# Введите название фрукта:
# Форматированная строка: apple

# Введите название фрукта: apple
# Введите название фрукта: apple
# Введите название фрукта:
# Форматированная строка: apple и apple

# Введите название фрукта: apple
# Введите название фрукта: apple
# Введите название фрукта: apple
# Введите название фрукта: apple
# Введите название фрукта: apple
# Введите название фрукта:
# Форматированная строка: apple, apple, apple, apple и apple


# ИТОГ: отлично — 3/3
