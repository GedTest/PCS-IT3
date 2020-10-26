'''
Tuples - neměnitelné n-tice hodnot (seřazený seznam prvků)
 V Pythonu je zapisujeme mezi kulaté závorky
'''

# Vytvoření tuples
numbers = (1, 2, 3)
print('numbers: ', numbers)
print('Type(numbers): ',type(numbers))

chars = tuple('Hello world')
print('chars: ', chars)
print('Type(chars): ',type(chars))

# Chceme-li vytvořit tuple jen s jedním prvkem, musíme připsat čárku, jinak Python ji python vyhodnotí jako chybu

colors = ('red',)
print('colors: ', colors)

# Součet tuples
print(f'chars + numbers: {chars + numbers}')

# Výpis hodnot
# Mužeme specifikovat rozsah indexů, zadáním začátku a konce rozsahu.

# Při specifikování rozsahu získáme nový tuple

print(f'chars[2:5]: {chars[2:5]}')

# Záporné indexy, znamenají prvky zezadu, -1 znamená poslední, -2, předposlední atd.

# Tento příklad vrací prvky z indexu -4(včetně) po index -1(mimo něj)
print(f'chars[-4:-1]: {chars[-4:-1]}')

# K zjištění velikosti, použijeme funkci len()
print(f'len(chars): {len(chars)}')

# Zjištění prvního výskytu a počtu výskytu prvku
if 'l' in chars:
    print(f'chars.index("l"): {chars.index("l")}')
    print(f'chars.count("l"): {chars.count("l")}')

# Záměna hodnot proměnných
x = 10
y = 2
x, y = y, x
print(f'x: {x}, y: {y}')
