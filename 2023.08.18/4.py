def countable_nouns(num: int, choice_words: tuple[str, str, str]) -> str:
    """Функция возвращает существительное русского языка, согласованное с числом."""
    last_digit = num % 10
    decade_digit = num % 100 // 10
    
    if decade_digit == 1:
        return choice_words[2]
    if last_digit == 1:
        return choice_words[0]
    # ИСПОЛЬЗОВАТЬ: цепочку сравнительных операторов
    if 2 <= last_digit <= 4:
        return choice_words[1]
    # ИСПРАВИТЬ: данный блок else повторяет первый условный блок — обычно, лучше конструировать условия так, чтобы блоки ветвления не повторялись: в данном случае это не требует чрезмерно сложных условий
    else:
        return choice_words[2]


# >>> countable_nouns(1, ('год', 'года', 'лет'))
# 'год'
# >>> countable_nouns(2, ('год', 'года', 'лет'))
# 'года'
# >>> countable_nouns(10, ('год', 'года', 'лет'))
# 'лет'
# >>> countable_nouns(12, ('год', 'года', 'лет'))
# 'лет'
# >>> countable_nouns(22, ('год', 'года', 'лет'))
# 'года'
# >>> countable_nouns(1, ('рубль', 'рубля', 'рублей'))
# 'рубль'
# >>> countable_nouns(22, ('рубль', 'рубля', 'рублей'))
# 'рубля'
# >>> countable_nouns(111, ('рубль', 'рубля', 'рублей'))
# 'рублей'


# ИТОГ: хорошо, но можно лучше — 2/3
