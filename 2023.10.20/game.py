from random import choice

from team import Team
from unit import Unit
from hero import Hero
from soldiers import Infantry, Archer, Cavalry 


"""Тест игры"""

# Создаем Героев (не менее 2-х)
myrometc = Hero('Илья Муромец')
dobrynia = Hero('Добрыня Никитич')
popovich = Hero('Алеша Попович')
cheburashka = Hero('Чебурашка')
syperman =  Hero('Супермен')
spiderman =  Hero('Человек Паук')
terminator =  Hero('Терминатор')
donalddack =  Hero('Дональд Дак')


# Любые два Героя создают собственные команды
cheburashka.create_team('Богатыри')
donalddack.create_team('Нато')

# Для удобства создаются итерируемые объекты (объектов)
# Список героев (будет сортироваться)
heroes = [myrometc, dobrynia, popovich, cheburashka, syperman, spiderman, terminator, donalddack]
# Кортеж Команд
teams = cheburashka.team, donalddack.team
# Кортеж Солдат
units = Infantry, Archer, Cavalry

# Герои добавляются в команды (вручную)
for unit in myrometc, dobrynia, popovich:
    unit.join_team(cheburashka.team)
    
for unit in syperman, spiderman, terminator:
    unit.join_team(donalddack.team)
    
# Результаты добавления созданных Героев в команды
print('\nРезультаты добавления созданных Героев в команды\n') 
print(cheburashka.team.heroes)
print(donalddack.team.heroes)

# Генерируем 1000 Солдат из возможных вариантов в Кортеже солдат
# Тут же заставляем сгенерированного солдата вступить в армию Героя (случайный выбор)
for soldier in range(1000):
    choice(units)().join_hero(choice(heroes))
  
# Сортируем Героев по размеру получившейся армии по убыванию
heroes.sort(key=lambda hero: hero.army.size, reverse=False)

# Смотрим результат сортировки Героев
print('\n\nСмотрим результат сортировки Героев\n') 
for hero in heroes:
    print(f'{hero}: {hero.army.size=}')

# Повышаем уровень Героя в зависимости от размера армии (в обратном порядке)
# Герою с самой маленькой армией уровень не повышаем (далее +1 по нарастающей)
for i in range(len(heroes)):
    heroes[i].update_level(i)

# Результат выполнения после повышения уровней Героям
print('\n\nРезультат выполнения после повышения уровней Героям\n')    
for hero in heroes:
    print(f'{hero}: {hero.level=}')  


# Складываем результаты команд (сумма показателя уровня каждого героя)
cheburashka_result_by_level_heroes = 0
for hero in cheburashka.team.heroes:
    cheburashka_result_by_level_heroes += hero.level
    
donalddack_result_by_level_heroes = 0
for hero in donalddack.team.heroes:
    donalddack_result_by_level_heroes += hero.level 

# Выводим итоговый результ команд 
print('\n\nВыводим итоговый результ команд\n')
print(f'{cheburashka.team.name=} {cheburashka_result_by_level_heroes}')  
print(f'{donalddack.team.name=} {donalddack_result_by_level_heroes}')   



# >>> ilya = Hero('Илья Муромец')
# >>> ilya.army.add_soldier(Archer())
# >>> ilya.army
# {'Archer': [Archer id=1849298350160]}
# >>>
# >>> arc = Archer()
# >>> print(arc.team)
# None
# >>> arc.join_hero(ilya)
# >>> print(arc.team)
# None
# >>> ilya.create_team('Богатыри')
# {'name': 'Богатыри', 'heroes': [Илья Муромец id=1849298813200]}
# >>> arc.team
# {'name': 'Богатыри', 'heroes': [Илья Муромец id=1849298813200]}
# >>> ilya.quit_team()
# >>> arc.team
# >>> print(arc.team)
# None
# >>> alesha = Hero('Алёша Попович')
# >>> alesha.create_team('Супер Богатыри')
# {'name': 'Супер Богатыри', 'heroes': [Алёша Попович id=1849298814416]}
# >>> ilya.join_team(alesha.team)
# >>> ilya.team
# {'name': 'Супер Богатыри', 'heroes': [Алёша Попович id=1849298814416, Илья Муромец id=1849298813200]}
# >>> ilya.army
# {'Archer': [Archer id=1849298350160, Archer id=1849298814096]}
# >>> for group in ilya.army.values():
# ...     for unit in group:
# ...             print(unit.team)
# ...
# {'name': 'Супер Богатыри', 'heroes': [Алёша Попович id=1849298814416, Илья Муромец id=1849298813200]}
# {'name': 'Супер Богатыри', 'heroes': [Алёша Попович id=1849298814416, Илья Муромец id=1849298813200]}


# =================================================================================================================================
# 1. TECT
# Результаты добавления созданных Героев в команды

# [Чебурашка id=2770289658960, Илья Муромец id=2770289522640, Добрыня Никитич id=2770289601488, Алеша Попович id=2770289661776]
# [Дональд Дак id=2770292168144, Супермен id=2770292163664, Человек Паук id=2770292167376, Терминатор id=2770292168080]


# Смотрим результат сортировки Героев

# Добрыня Никитич id=2770289601488: hero.army.size=104
# Человек Паук id=2770292167376: hero.army.size=105
# Чебурашка id=2770289658960: hero.army.size=114
# Терминатор id=2770292168080: hero.army.size=128
# Алеша Попович id=2770289661776: hero.army.size=135
# Дональд Дак id=2770292168144: hero.army.size=135
# Супермен id=2770292163664: hero.army.size=137
# Илья Муромец id=2770289522640: hero.army.size=142


# Результат выполнения после повышения уровней Героям

# Добрыня Никитич id=2770289601488: hero.level=0
# Человек Паук id=2770292167376: hero.level=1
# Чебурашка id=2770289658960: hero.level=2
# Терминатор id=2770292168080: hero.level=3
# Алеша Попович id=2770289661776: hero.level=4
# Дональд Дак id=2770292168144: hero.level=5
# Супермен id=2770292163664: hero.level=6
# Илья Муромец id=2770289522640: hero.level=7


# Выводим итоговый результ команд

# cheburashka.team.name='Богатыри' 13
# donalddack.team.name='Нато' 15

# =================================================================================================================================
# 2. TECT
# Результаты добавления созданных Героев в команды

# [Чебурашка id=1983113301072, Илья Муромец id=1983113164752, Добрыня Никитич id=1983113243600, Алеша Попович id=1983113303888]
# [Дональд Дак id=1983115810256, Супермен id=1983115805776, Человек Паук id=1983115809488, Терминатор id=1983115810192]


# Смотрим результат сортировки Героев

# Чебурашка id=1983113301072: hero.army.size=116
# Алеша Попович id=1983113303888: hero.army.size=118
# Человек Паук id=1983115809488: hero.army.size=118
# Терминатор id=1983115810192: hero.army.size=118
# Илья Муромец id=1983113164752: hero.army.size=123
# Добрыня Никитич id=1983113243600: hero.army.size=125
# Дональд Дак id=1983115810256: hero.army.size=137
# Супермен id=1983115805776: hero.army.size=145


# Результат выполнения после повышения уровней Героям

# Чебурашка id=1983113301072: hero.level=0
# Алеша Попович id=1983113303888: hero.level=1
# Человек Паук id=1983115809488: hero.level=2
# Терминатор id=1983115810192: hero.level=3
# Илья Муромец id=1983113164752: hero.level=4
# Добрыня Никитич id=1983113243600: hero.level=5
# Дональд Дак id=1983115810256: hero.level=6
# Супермен id=1983115805776: hero.level=7


# Выводим итоговый результ команд

# cheburashka.team.name='Богатыри' 10
# donalddack.team.name='Нато' 18

# =================================================================================================================================
# 3. TECT
# Результаты добавления созданных Героев в команды

# [Чебурашка id=2032517418064, Илья Муромец id=2032517281744, Добрыня Никитич id=2032517360592, Алеша Попович id=2032517420880]
# [Дональд Дак id=2032519927248, Супермен id=2032519922768, Человек Паук id=2032519926480, Терминатор id=2032519927184]


# Смотрим результат сортировки Героев

# Чебурашка id=2032517418064: hero.army.size=102
# Илья Муромец id=2032517281744: hero.army.size=117
# Человек Паук id=2032519926480: hero.army.size=123
# Алеша Попович id=2032517420880: hero.army.size=126
# Дональд Дак id=2032519927248: hero.army.size=129
# Добрыня Никитич id=2032517360592: hero.army.size=131
# Супермен id=2032519922768: hero.army.size=133
# Терминатор id=2032519927184: hero.army.size=139


# Результат выполнения после повышения уровней Героям

# Чебурашка id=2032517418064: hero.level=0
# Илья Муромец id=2032517281744: hero.level=1
# Человек Паук id=2032519926480: hero.level=2
# Алеша Попович id=2032517420880: hero.level=3
# Дональд Дак id=2032519927248: hero.level=4
# Добрыня Никитич id=2032517360592: hero.level=5
# Супермен id=2032519922768: hero.level=6
# Терминатор id=2032519927184: hero.level=7


# Выводим итоговый результ команд

# cheburashka.team.name='Богатыри' 9
# donalddack.team.name='Нато' 19