cell1, cell2 = input(), input()
horz, vert = 'abcdefgh', '12345678'
# ИСПРАВИТЬ: для первого символа можно применить встроенную функцию ord() — она тоже выполнится быстрее, чем метод index()
x1, y1 = horz.index(cell1[0]), vert.index(cell1[1])
x2, y2 = horz.index(cell2[0]), vert.index(cell2[1])

print('да') if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1 else print('нет')


# g3
# f2
# да

# c6
# d4
# нет

# a1
# b2
# да

# h8
# h6
# нет


# ИТОГ: отлично — 4/5
