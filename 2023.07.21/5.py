text = input('Текст телеграммы: ')
chars = [char for char in text if char != ' ']

price_msg = str(round(len(chars) * 30))

print(f'{price_msg[:-2] or 0} руб. {price_msg[-2:]} коп.')


# Текст телеграммы:
# 0 руб. 0 коп.

# Текст телеграммы: 1 2            3
# 0 руб. 90 коп.

# Текст телеграммы: грузите апельсины бочках братья карамазовы
# 11 руб. 40 коп.