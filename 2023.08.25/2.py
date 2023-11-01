def deck() -> 'generator':
    """Функция создает упорядоченную колоду игральных карт"""
    # ИСПРАВИТЬ: не нужно создавать кортеж из генераторного выражения по объекту range, для того, чтобы перебрать элементы в объекте range
    nominals = tuple(num for num in range(2, 15))
    cards_deck = ('черви', 'бубны', 'пики', 'трефы')
    
    for card_deck in cards_deck:
        for nominal in nominals:
            yield nominal, card_deck


# >>> cards = deck()
# >>> type(cards)
# <class 'generator'>
# >>> cards.__next__()
# (2, 'черви')
# >>> cards.__next__()
# (3, 'черви')
# >>> cards.__next__()
# (4, 'черви')
# >>> cards.__next__()
# (5, 'черви')

# >>> cards = deck()
# >>> list(cards)[::13]
# [(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]


# ИТОГ: хорошо — 3/4
