def deck() -> 'generator':
    """Функция создает упорядоченную колоду игральных карт"""
    
    nominals = tuple(num for num in range(2, 15))
    cards_deck = ('черви', 'бубны', 'пики', 'трефы')
    
    for card_deck in cards_deck:
        for nominal in nominals:
            yield (nominal, card_deck)