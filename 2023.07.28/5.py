scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}


word = input()
score = 0

for char in word:
    for key, value in scores_letters.items():
        if char.upper() in value:
            score += key

print(score)

# синхрофазатрон
# 29

# эрудит
# 15

# ааааа
# 5

# ффффф
# 40