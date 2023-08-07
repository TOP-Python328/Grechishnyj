email = input('Введите e-mail: ')
correct = 'нет'

if '.' in email and '@' in email:
    # ИСПРАВИТЬ: операции со строками являются довольно ресурсозатратными, поэтому в общем случае их выполняют единожды, запоминая результат — оптимизируйте вызовы rindex('.')
    if email.rindex('.') - email.rindex('@') > 1 and email.rindex('.') < len(email) - 1:
        correct = 'да'

print(f'Корректный e-mail: {correct}')


# Введите e-mail: grechishny.p@mail.ru
# Корректный e-mail: да

# Введите e-mail: grechishny.p@mail.
# Корректный e-mail: нет

# Введите e-mail: grechishny.p@mail
# Корректный e-mail: нет

# Введите e-mail: grechishny.p@
# Корректный e-mail: нет

# Введите e-mail: grechishny.p
# Корректный e-mail: нет

# Введите e-mail: grechishny.p$mail.ru
# Корректный e-mail: нет

# Введите e-mail: grechishny.p.mail@ru
# Корректный e-mail: нет


# ИТОГ: хорошо — 2/3
