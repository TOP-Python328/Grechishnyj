cell1, cell2 = input(), input()
horz, vert = 'abcdefgh', '12345678'
x1, y1 = horz.index(cell1[0]), vert.index(cell1[1])
x2, y2 = horz.index(cell2[0]), vert.index(cell2[1])

print('да') if (x1 + y1 + x2 + y2) % 2 == 0 else print('нет')

# ВАРИАНТ БЕЗ ТЕРНАРНОГО ОПЕРАТОРА
# msg = ['да', 'нет']
# print(msg[(x1 + y1 + x2 + y2) % 2]

# a1
# b2
# да

# a1
# c1
# да

# a1
# b1
# нет

# a1
# c2
# нет