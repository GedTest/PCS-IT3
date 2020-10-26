'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Neuspořádaní, měnitelná množina s indexi
#
#  V Pythonu je zapisujeme mezi hranaté závorky, mají klíče a hodnoty.
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

point = {'x': 1, 'y': 10}

# Vytvoření slovníku pomocí konstruktoru dict()
point = dict(x=1, y=10)

# Změna hodnoty jednoho prvku slovníku
point['x'] = 2

# Vložení nového prvku do slovníku
point['z'] = 20

# Přístup k položkám slovníku
print(f'point["x"]: {point["x"]}')
print(f'point.get("x"): {point.get("x")}')

# Zjištění, zda existuje hodnota
if 'z' in point:
    print(f'point.get("z"): {point.get("z")}')

# Když hodnota neexistuje, vrací 0    
print(f'point.get("v", 0): {point.get("v", 0)}')

# Odstranění prvku ze slovníku  
del point['x']
print(f'point: {point}')

print(f'car.pop(): {car.pop("model")}')

# Odstraní poslední prvek ze slovníku
print(f'car.popitem(): {car.popitem()}')

# Procházení slovníkem - vypíše vždy pár klíč - hodnota
for key, value in point.items():
    print(f'{key} - {value}')

# Dictionary comprehension - zkráceně vytvoří slovník, jehož klíče tvoří čísla od 0 do 9 a hodnoty druhé mocniny 
values = {x: x ** 2 for x in range(10)}
print(f'values: {values}')

# Unpacking operator - pro slovníky se používají **
first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 5}
common = {**first, 'a': 15, **second}
print(f'common: {common}')

# Nested dictionary - vnořené slovníky
myfamily = {
    'child1': {
        'name': 'Emil',
        'year': 2004
    },
    'child2': {
        'name': 'Tobias',
        'year': 2007
    },
    'child3': {
        'name': 'Linus',
        'year': 2011
    }
}
print(f'Nested dictionary myfamily: {myfamily}')

# ??? 4. cvičení ???
# a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
# viz níže uvedený vzor.
'''
Slovník myfamily
---------------------------------------------
child           name                year
---------------------------------------------
child1          Emil                2004
child2          Tobias              2007
child3          Linus               2011
---------------------------------------------
Počet záznamů: 3
'''
import datetime

Game = {
    "level_01": {
        "name": "Letajici ostrov",
        "player": {"HP": 10, "score": "Awesome", "items_found": [True, True, False]},
        "enemyCounterByType": (15, 8, 1, 20, 13),
        "secret": True,
        "mode": 0,
        "last_played": datetime.datetime(2002, 3, 17)
    },
    "level_02": {
        "name": "Rybarska vesnice",
        "player": {"HP": 25, "score": "Super", "items_found": [False, True]},
        "enemyCounterByType": (5, 8, 10, 7, 55),
        "secret": False,
        "mode": 0,
        "last_played": datetime.datetime(2002, 6, 22)
    },
    "level_03": {
        "name": "Strasidelny zamek",
        "player": {"HP": 3, "score": "Bad", "items_found": [False, False, True]},
        "enemyCounterByType": (5, 0, 1, 2, 3),
        "secret": True,
        "mode": 2,
        "last_played": datetime.datetime(2002, 6, 25)
    }
}
# print(Game)
Game.pop("level_03")
# print(f'Game after removing level_03: {Game}')

Game["level_04"] = {
    "name": "Bonus",
    "player": {"HP": 10, "score": "SSStylish", "items_found": [True]},
    "enemyCounterByType": (100, 200, 300, 400, 500),
    "secret": False,
    "mode": 1,
    "last_played": datetime.datetime(2002, 4, 10)
}
# print(f'Game after adding bonus level_04: {Game}')

print("\n{:<16} {:<34} {:<33} {:<6} {:<20} {:<1} {:<6} {:<1} {:<4} {:<3} {:<4}".format('name', '|', 'player', '|', 'enemyCounterByType', '|', 'secret', '|', 'mode', '|', 'last time played'))
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
for key, value in Game.items():
    name = value['name']
    player = str(value['player'])
    enemyCounterByType = str(value['enemyCounterByType'])
    secret = str(value['secret'])
    mode = value['mode']
    last_played = str(value['last_played'])
    print("{:<16} {:<1} {:<66} {:<1} {:<25} {:<1} {:<6} {:<3} {:<2} {:<1} {:<7}".format(name, '|', player, '|', enemyCounterByType, '|', secret, '|', mode, '|', last_played))
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")