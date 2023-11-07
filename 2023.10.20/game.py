from random import choice

from team import Team
from hero import Hero
from warriors import Infantry, Archer, Cavalry




myrometc = Hero('Илья Муромец')
nikitich = Hero('Добрыня Никитич')
popovich = Hero('Алёша Попович')
gorinich = Hero('Змей Горыныч')
solovei = Hero('Соловей Разбойник')
cheburashka = Hero('Чебурашка')

terminator = Hero('Теминатор')
spiderman = Hero('Человек Паук')
superman = Hero('Супермен')
batman = Hero('Бэтман')
halk = Hero('Халк')
mickeymaus = Hero('Микки Маус')
donalddack = Hero('Дональд Дак')

cheburashka.create_team('ВСРФ')
cheburashka_team = cheburashka.team
myrometc.join_team(cheburashka_team)
nikitich.join_team(cheburashka_team)
popovich.join_team(cheburashka_team)
gorinich.join_team(cheburashka_team)
solovei.join_team(cheburashka_team)

nato = Team('НАТО')
terminator.join_team(nato)
spiderman.join_team(nato)
superman.join_team(nato)
batman.join_team(nato)
halk.join_team(nato)
mickeymaus.join_team(nato)
donalddack.join_team(nato)


for i in range(100):
    new_archer = Archer()
    new_archer.join_hero(choice(cheburashka_team.heroes))

for i in range(100):
    new_infantry = Infantry()
    new_infantry.join_hero(choice(cheburashka_team.heroes))

for i in range(100):
    new_cavalry = Cavalry()
    new_cavalry.join_hero(choice(cheburashka_team.heroes))

for i in range(100):
    new_archer = Archer()
    new_archer.join_hero(choice(nato.heroes))

for i in range(100):
    new_infantry = Infantry()
    new_infantry.join_hero(choice(nato.heroes))

for i in range(100):
    new_cavalry = Cavalry()
    new_cavalry.join_hero(choice(nato.heroes))
    

cheburashka_team_power = 0
for hero in cheburashka_team.heroes:
    cheburashka_team_power += hero.army.attack

nato_team_power = 0
for hero in nato.heroes:
    nato_team_power += hero.army.attack


for hero in cheburashka_team.heroes:
    print(f'{hero=}\n\t{hero.army.size=}\n\t{hero.army.attack=}\n\t{hero.army.shield=}\n\t{hero.army.power=}')
    
for hero in nato.heroes:
    print(f'{hero=}\n\t{hero.army.size=}\n\t{hero.army.attack=}\n\t{hero.army.shield=}\n\t{hero.army.power=}')

# >>> cheburashka.army
# Archer:
        # Archer: id=3018034151824
        # Archer: id=3018034152080
        # Archer: id=3018034152976
        # Archer: id=3018034153232
        # Archer: id=3018034153296
        # Archer: id=3018034153616
        # Archer: id=3018034153680
        # Archer: id=3018034154256
        # Archer: id=3018034154384
        # Archer: id=3018034156880
# Infantry:
        # Infantry: id=3018034157008
        # Infantry: id=3018034157136
        # Infantry: id=3018034157456
        # Infantry: id=3018034157776
        # Infantry: id=3018034157840
        # Infantry: id=3018034159120
        # Infantry: id=3018034159376
        # Infantry: id=3018034157712
        # Infantry: id=3018034160272
        # Infantry: id=3018034157200
        # Infantry: id=3018034158096
        # Infantry: id=3018034161104
        # Infantry: id=3018034161552
        # Infantry: id=3018034161616
        # Infantry: id=3018034162000
        # Infantry: id=3018034162128
        # Infantry: id=3018034162832
# Cavalry:
        # Cavalry: id=3018034163344
        # Cavalry: id=3018034164432
        # Cavalry: id=3018034164944
        # Cavalry: id=3018034165264
        # Cavalry: id=3018034165392
        # Cavalry: id=3018034165648
        # Cavalry: id=3018034165712
        # Cavalry: id=3018034166352
        # Cavalry: id=3018034163856
        # Cavalry: id=3018034164496
        # Cavalry: id=3018034166736
        # Cavalry: id=3018034167760
        # Cavalry: id=3018034200912
        # Cavalry: id=3018034201168
        # Cavalry: id=3018034201360
        # Cavalry: id=3018034201424
        # Cavalry: id=3018034201872
        # Cavalry: id=3018034202128

# >>> cheburashka.army.size
# 45
# >>> cheburashka.army.attack
# 755

# >>> cheburashka_team_power
# 4500

# >>> nato_team_power
# 4500


# hero='Чебурашка'
        # hero.army.size=35
        # hero.army.attack=535
        # hero.army.shield=535
        # hero.army.power=1070
# hero='Илья Муромец'
        # hero.army.size=50
        # hero.army.attack=780
        # hero.army.shield=780
        # hero.army.power=1560
# hero='Добрыня Никитич'
        # hero.army.size=59
        # hero.army.attack=905
        # hero.army.shield=905
        # hero.army.power=1810
# hero='Алёша Попович'
        # hero.army.size=47
        # hero.army.attack=705
        # hero.army.shield=705
        # hero.army.power=1410
# hero='Змей Горыныч'
        # hero.army.size=56
        # hero.army.attack=790
        # hero.army.shield=790
        # hero.army.power=1580
# hero='Соловей Разбойник'
        # hero.army.size=53
        # hero.army.attack=785
        # hero.army.shield=785
        # hero.army.power=1570
# hero='Теминатор'
        # hero.army.size=38
        # hero.army.attack=560
        # hero.army.shield=560
        # hero.army.power=1120
# hero='Человек Паук'
        # hero.army.size=43
        # hero.army.attack=635
        # hero.army.shield=635
        # hero.army.power=1270
# hero='Супермен'
        # hero.army.size=34
        # hero.army.attack=500
        # hero.army.shield=500
        # hero.army.power=1000
# hero='Бэтман'
        # hero.army.size=41
        # hero.army.attack=595
        # hero.army.shield=595
        # hero.army.power=1190
# hero='Халк'
        # hero.army.size=42
        # hero.army.attack=650
        # hero.army.shield=650
        # hero.army.power=1300
# hero='Микки Маус'
        # hero.army.size=47
        # hero.army.attack=675
        # hero.army.shield=675
        # hero.army.power=1350
# hero='Дональд Дак'
        # hero.army.size=55
        # hero.army.attack=885
        # hero.army.shield=885
        # hero.army.power=1770






















    
