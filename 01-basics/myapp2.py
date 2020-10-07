import wikipedia as wiki
# import random

'''
Aby tato aplikace správně fungovala, musí se změnit v site-packages/wikipedia/wikipedia.py řádek 389 na:

lis = BeautifulSoup(html, 'html.parser').find_all('li')
'''

cont = 'y'

while cont == 'y':
    info = input('O čem si přejete zjístit více informací: ')
    lang = input('V jakém jazyce si přejte požadované informace (např. cs, en): ')

    try:
        wiki.set_lang(lang)
        print(wiki.page(info).content)
        # print(wiki.summary(info))

    except wiki.DisambiguationError as e:
        print('Bylo nalezeno více výsledků...')
        # print(wiki.page(random.choice(e.options)).content)
        # print(e.options)
        dupl = wiki.search(info)
        for i in dupl:
            print(i)

    user_cont = input('Chcete vyhledávat znova (y/n): ')
    if user_cont != cont:
        cont = user_cont
