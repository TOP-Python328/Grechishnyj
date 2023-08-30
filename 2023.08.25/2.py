def deck() -> 'generator':
    """Функция создает упорядоченную колоду игральных карт"""
    
    nominals = tuple(i for i in range(2, 15))
    cards_deck = ('черви', 'бубны', 'пики', 'трефы')
    
    for i in cards_deck:
        for j in nominals:
            yield (j, i)