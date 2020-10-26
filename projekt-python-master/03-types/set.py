'''
 Set je množina jedinečných hodnot

 Set je neuspořádaná a neindexovaná množina

 V Pythonu je zapisujeme mezi složené závorky
'''
my_set = {2, 3, 9, 7}
print('Množina my_set: ', my_set)
print('Typ my_set: ', type(my_set))

# Vytvoření množiny ze seznamu hodnot (list)
numbers = [1, 4, 1, 5, 3, 3, 1, 2, 8, 2]
print(f'Proměnná numbers - seznam (list): {numbers}')
set_numbers = set(numbers)
print(f'Proměnná set_numbers - množina (set): {set_numbers}')

# Vytvoření množiny jedinečných znaků z řetězce
chars = sorted(list('Hello world'))
set_chars = set(chars)
print(f'Uspořádaná množina (set) jedinečných hodnot: {set_chars}')

# Po vytvoření množiny již nemůžete měnit její členy, můžete však nové přidávat.

# Pro přidání prvku do množiny pouřijte metodu add()
set_chars.add('V')

# Pro přidání více hodnot použijte metodu update()
set_chars.update('X', 'Y', 'Z')

# Pro odstranění prvku máme metody remove() a discard()
set_chars.remove('H')
print(f'Proměnná set_chars: {set_chars}')

# clear() vymaže všechny prvky množiny
set_chars.clear()

# klíčovým slovem del vymažeme celou množinu
del set_chars

# Přístup k hodnotám množiny
# množiny jsou neuspořádaná, tudíž nemají indexi, proto k nim nemůžeme přistupvat jako u polí

# my_set[1]

# Jde však iterovat cyklem
for x in my_set:
  print(x)

'''
Množinové operace
'''
# Sjednocení množin
print(f'set_numbers | my_set: {set_numbers | my_set}')
print(f'set_numbers.union(my_set): {set_numbers.union(my_set)}')
# Průnik množin
print(f'set_numbers & my_set: {set_numbers & my_set}')
print(f'set_numbers.intersection(my_set): {set_numbers.intersection(my_set)}')
# Rozdíl množin
print(f'set_numbers - my_set: {set_numbers - my_set}')
print(f'set_numbers.difference(my_set): {set_numbers.difference(my_set)}')
# Doplněk množin
print(f'set_numbers ^ my_set: {set_numbers ^ my_set}')
print(f'set_numbers.symmetric_difference(my_set): {set_numbers.symmetric_difference(my_set)}')
# Zjištění zda množina obsahuje hodnotu
print(f'1 in set_numbers: {1 in set_numbers}')
