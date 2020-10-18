'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.80665 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

SPEED_OF_SOUND_WATER = 1400

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''


def volny_pad_na_zemi(cas):
    '''
    Funkce sloužící k výpočtu rychlosti volného pádu na Zemi (výsledek je v m/s)
    '''
    return str(round(cas * EARTH_GRAVITY, 2)) + ' m/s'


def volny_pad_na_mesici(cas):
    '''
    Funkce sloužící k výpočtu rychlosti volného pádu na Měsíci (výsledek je v m/s)
    '''
    return str(round(cas * MOON_GRAVITY, 2)) + ' m/s'


def doba_urazena_svetlem(draha):
    '''
    Funkce sloužící k výpočtu doby, za kterou světlo urazí dráhu (výsledek je v sekundách)
    '''
    return str(round(draha / SPEED_OF_LIGHT, 2)) + ' s'


def vlnova_delka_zvukoveho_vlneni(frekvence):
    '''
    Funkce sloužící k výpočtu vlnové délky příslušného zvukového vlnění (výsledek je v metrech)
    '''
    return str(round(SPEED_OF_SOUND / frekvence, 2)) + ' m'


def draha_urazena_zvukem_ve_vzduchu(cas):
    '''
    Funkce sloužící k výpočtu dráhy uražené zvukem ve vzduchu za dobu (výsledek je v metrech)
    '''
    return str(round(SPEED_OF_SOUND * cas, 2)) + ' m'


def draha_urazena_zvukem_ve_vode(cas):
    '''
    Funkce sloužící k výpočtu dráhy uražené zvukem ve vodě za dobu (výsledek je v metrech)
    '''
    return str(round(SPEED_OF_SOUND_WATER * cas, 2)) + ' m'
