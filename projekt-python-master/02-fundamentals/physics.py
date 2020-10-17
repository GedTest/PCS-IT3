'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.80665  # ? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.625  # ? měsíční gravitace
SPEED_OF_LIGHT = 299792458  # ? rychlost světla
SPEED_OF_SOUND = 343  # ? rychlost zvuku

KAPPA = 6.67e-11

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

def greet():
    '''
    Uvod do sbirky Fyziky
    '''

    print("Toto je sbirka fyzikalnich uloh z FYZIKY, zde najdete par vyreseneych prikladu:\n")

ZADANI_PRVE = r'1) Jak daleko je skala, od ktere se ozvenou vratil zvuk za 1,5 s?'
ZADANI_DRUHE = r'2) Zjistete frekvenci vlneni zluteho svetle ve vzduchu, vite-li jeho vlnovou delku 'u'\u03BB'' = 590nm?'
ZADANI_TRETI = r'3) Zjistete hmotnosti Zeme a Mesice, znate-li jejich gravitacni sily, polomer Mesice = 1.72*10^6, ' \
               r'polomer Zeme = 6.378*10^6 a konstantu 'u'\U0001D718'' = 6.67*10^-11:'

arrExplanation = [r'Podle vzorce s = v * t vypocteme vzdalenost, kterou urazi zvuk tam i zpátky, tuto vzdálenost ({v*t}) vydělíme 2 a dostaneme vysledek.',
                  r'Podle vzorce 'u'\u03BB'' = v / f odvodime => f = v / 'u'\u03BB''. Dosadime a vypocteme vysledek.',
                  r'Ze vzorce pro vypocet grav. konstanty ''\'g\''' odvodime hmotnost.\ng = (\U0001D718 * m) / r^2   =>   m = (g * r^2) / \U0001D718\nDosadime do vzorce a vypocteme vysledky:\n']

def CalcMethod(number,y,z,w1=0,w2=0):
    '''
    Funkce vypocte ulohu
    '''
    if number == 1:
        return round((z * y) / 2, 2)
    elif number == 2:
        return round(z / y, 2)
    elif number == 3:
        arrResults = []
        arrResults.append(format((EARTH_GRAVITY * w1**2) / KAPPA, '.3g'))
        arrResults.append(format((MOON_GRAVITY * w2**2) / KAPPA, '.3g'))
        return arrResults

def Vypocet(zadani,counter,X,Y,Z):
    '''
    Priklady vypoctenych civceni s postupem a vysvetelnim
    '''

    print(zadani)
    print(f"----------------------------------------------------------\n"
          f"{Y['name']}={Y['value']}{Y['unit']}\n"
          f"{Z['name']}={Z['value']}{Z['unit']}\n"
          f"{X['name']}=?[{X['unit']}]\n"
          f"----------------------------------------------------------\n"
          f"{arrExplanation[counter-1]}")
    if counter != 3:
        X['value'] = CalcMethod(counter, Y['value'], Z['value'])
        print(f"Vysledek je: {X['name']}={X['value']}{X['unit']}")
    else:
        results = CalcMethod(counter, 0, 0, Y['value'], Z['value'])
        print(f"Hmotnost Zeme je {results[0]}{Y['unit']} a hmotnost Mesice je {results[1]}{Z['unit']}")
    print(f"----------------------------------------------------------\n")