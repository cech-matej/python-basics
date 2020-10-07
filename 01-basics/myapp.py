import math

vypocty = ['Čtverec', 'Obdelník', 'Trojúhelník', 'Kružnice', 'Rovnoběžník', 'Lichoběžník']
cont = 'y'


def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


while cont == 'y':
    print('\n')
    for idx, i in enumerate(vypocty):
        print(str(idx+1) + ' - ' + str(i))

    cal = input('Zadejte číslo, pro výpočet hodnot požadovaného tvaru: ')

    if cal == '1':
        while True:
            a = input('Zadejte velikost strany a: ')
            if isfloat(a):
                a = float(a)
                print('-- Obsah = {}'.format(pow(a, 2)))
                print('-- Obvod = {}'.format(4 * a))
                break

    elif cal == '2':
        while True:
            a = input('Zadejte velikost strany a: ')
            b = input('Zadejte velikost strany b: ')
            if isfloat(a) and isfloat(b):
                a = float(a)
                b = float(b)
                print('-- Obsah = {}'.format(a * b))
                print('-- Obvod = {}'.format(2 * a + 2 * b))
                break

    elif cal == '3':
        while True:
            a = input('Zadejte velikost základny a: ')
            v = input('Zadejte velikost výšky na stranu a: ')
            if isfloat(a) and isfloat(v):
                a = float(a)
                v = float(v)
                print('-- Obsah = {}'.format((a * v)/2))
                break

    elif cal == '4':
        while True:
            r = input('Zadejte poloměr kružnice: ')
            if isfloat(r):
                r = float(r)
                print('-- Obsah = {}'.format(math.pi * pow(r, 2)))
                print('-- Obvod = {}'.format(2 * math.pi * r))
                break

    elif cal == '5':
        while True:
            a = input('Zadejte velikost strany a: ')
            b = input('Zadejte velikost strany b: ')
            v = input('Zadejte velikost výšky na stranu a: ')
            if isfloat(a) and isfloat(b) and isfloat(v):
                a = float(a)
                b = float(b)
                v = float(v)
                print('-- Obsah = {}'.format(a * v))
                print('-- Obvod = {}'.format(2 * a + 2 * b))
                break

    elif cal == '6':
        while True:
            a = input('Zadejte velikost základny a: ')
            c = input('Zadejte velikost základny c: ')
            v = input('Zadejte velikost výšky na stranu a: ')
            if isfloat(a) and isfloat(c) and isfloat(v):
                a = float(a)
                c = float(c)
                v = float(v)
                print('-- Obsah = {}'.format(v * (a + c)/2))
                print('-- Střední příčka = {}'.format((a + c)/2))
                break

    else:
        print('Špatně zadané číslo!')

    user_cont = input('Chcete pokračovat (y/n): ')
    if user_cont != cont:
        cont = user_cont
