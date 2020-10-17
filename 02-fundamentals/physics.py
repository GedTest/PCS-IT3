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
def Vypocet(zadani):
    '''
    Priklady vypoctenych civceni s postupem a vysvetelnim
    '''

    if zadani[0] == "1":
        t = 1.5
        v = SPEED_OF_SOUND
        s = (v * t) / 2
        print(f"Prvni zadani:\n"
              f"-------------\n"
              f"t={t}s\n"
              f"v={v}m/s\n"
              f"s=?[m]\n"
              f"-------------\n"
              f"podle vzorce s = v * t vypocteme vzdalenost, kterou urazi zvuk tam i zpátky\n"
              f"tuto vzdálenost ({v*t}) vydělíme 2 a dostaneme vysledek s = {s}m.\n"
              f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n\n")

    elif zadani[0] == "2":
        Lambda = 590
        v = SPEED_OF_LIGHT
        f = v / Lambda
        print(f"Druhe zadani:\n"
              f"-------------\n"
              f"\u03BB={Lambda}m\n"
              f"v={v}m/s\n"
              f"f=?[Hz]\n"
              f"-------------\n"
              f"podle vzorce \u03BB = v / f odvodime f = v / \u03BB.\n"
              f"Dosadime a vypocteme: f = {round(f,2)}Hz\n"
              f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n\n")

    elif zadani[0] == "3":
        Rm = 1.72e6
        Rz = 6.378e6
        k = 6.67e-11

        Mm = (MOON_GRAVITY * Rm**2) / k
        Mz = (EARTH_GRAVITY * Rz**2) / k
        print(f"Treti zadani\n"
              f"-------------\n"
              f"Rm={Rm}\n"
              f"Rz={Rz}\n"
              f"\U0001D718={k}\n"
              f"Mm=?[kg] Mz=?[kg]\n"
              f"-------------\n"
              f"Ze vzorce pro vypocet grav. konstanty 'g' odvodime hmotnost.\n"
              f"g = (\U0001D718 * m) / r^2   =>   m = (g * r^2) / \U0001D718\n"
              f"Dosadime do vzorce a vypocteme vysledky:\n"
              f"Hmotnost Zeme je {format(Mz, '.3g')}kg  |   Hmotnost Mesice je {format(Mm, '.3g')}kg.\n"
              f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n\n")