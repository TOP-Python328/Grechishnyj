ml_i = input("Введите целую часть, миль: ")
ml_f = input("Введите дробную часть, миль: ")
mile = float(f'{ml_i}.{ml_f}')
# ИСПРАВИТЬ: если результат округления должен быть использован где-то ещё, тогда используете функцию round(); в данном случае выгоднее воспользоваться синтаксисом f-строк
print(f'{mile} миль = {mile * 1.61:.1f} км.')
# f'{2**0.3:.2f}'

# Введите целую часть, миль: 20
# Введите дробную часть, миль: 4
# 20.4 миль = 32.8 км


# ИТОГ: хорошо, немного доработать — 3/4
