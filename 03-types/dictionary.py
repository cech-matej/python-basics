'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Collection which is unordered, changeable and indexed.
#   Sbírka, která je neseřazená, měnitelná a indexovaná
# In Python dictionaries are written with curly brackets, and they have keys and values.
#   Slovníky v Pythonu jsou zapisovány pomocí složených závorek a mají klíč a hodnotu
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
  'child1' : {
    'name' : 'Emil',
    'year' : 2004
  },
  'child2' : {
    'name' : 'Tobias',
    'year' : 2007
  },
  'child3' : {
    'name' : 'Linus',
    'year' : 2011
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


kraje = {
  'Moravskoslezský': {
    'mesto': 'Ostrava',
    'rozloha': 5426.83,
    'pocet_obyvatel': 1203000,
    'okresy': {'Bruntál', 'Opava'},
    'sousedni_kraje': ('  Olomoucký', 'Zlínksý'),
    'reky': ['     Odra', 'Olše']
  },
  'Olomoucký': {
    'mesto': 'Olomouc',
    'rozloha': 5266.57,
    'pocet_obyvatel': 633000,
    'okresy': {'Jeseník', 'Olomouc'},
    'sousedni_kraje': ('Moravskoslezský', 'Zlínksý'),
    'reky': ['Morava', 'Odra']
  },
  'Zlínský': {
    'mesto': 'Zlín',
    'rozloha': 3963.55,
    'pocet_obyvatel': 583000,
    'okresy': {'Kroměříž', 'Vsetín'},
    'sousedni_kraje': ('Olomoucký', 'Jihomoravský'),
    'reky': ['Morava', 'Bečva']
  }
}

pass

kraje['Jihomoravský'] = {
  'mesto': 'Brno',
  'rozloha': 7187.7,
  'pocet_obyvatel': 1189000,
  'okresy': {'Blansko', 'Hodonín'},
  'sousedni_kraje': ('Jihočeský', 'Vysočina'),
  'reky': ['    Morava', 'Dyje']
}
kraje.pop('Olomoucký')

print("---------------------------------------------------------------------------------------------------------------------")
print("kraj             krajské město  rozloha    pocet obyvatel  2 okresy          2 sousední kraje         2 řeky")
print("---------------------------------------------------------------------------------------------------------------------")

for x in kraje:
  print(f"{x.ljust(17)}" 
        f"{kraje[x]['mesto'].ljust(15)}"
        f"{str(kraje[x]['rozloha']).ljust(11)}"
        f"{str(kraje[x]['pocet_obyvatel']).ljust(16)}", end='')
  print(*kraje[x]['okresy'], sep=', ', end='  ')
  print(*kraje[x]['sousedni_kraje'], sep=', ', end='  ')
  print(*kraje[x]['reky'], sep=', ')

print("---------------------------------------------------------------------------------------------------------------------\n"
      f"Počet záznamů: {len(kraje)}")
