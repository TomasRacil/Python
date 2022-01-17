"""
Dekorátory jsou funkce, které zabalí jinou funkci a tím jsou schopné ovlivnit
její vstup nebo výstup, nebo jestli bude vůbec zavolána,
aniž bychom přímo modifikovali samotnou funkci.
Tato vlastnost může být velice užitečná například v případě že nemáme možnost
funkci modifikovat, nechceme ji modifikovat, nebo chceme dekorovat více funkcí.
"""
# výchozí funkce
import functools
def zvysOJedna(number): return number + 1


print(f"Zvyš o jedna číslo 1: {zvysOJedna(1)}\n")


# V jazyku python je možné funkce předávat, jako by se jednalo o proměnnou.
# funkce, která vrací jinou funkci
def vratFunkci(): return zvysOJedna


# ukázka toho co nám tato funkce vlastně vrací
print(f"Vracena funkce {vratFunkci()}\n")

# volání funkce vrácené jinnou funkcí
f = vratFunkci()
print(f"Volání vrácené funkce s parametrem 1: {f(1)}\n")


# Také je možné mít funkce které jsou součástí další funkce (child function)
def rodic():
    print("Tisk z mateřské funkce")

    def prvniPotomek():
        print("Tisk z prvního potomka\n")

    def druhyPotomek():
        print("Tisk z druhého potomka")

    # volání funkcí definovaných v rámci funkce
    druhyPotomek()
    prvniPotomek()


print("Volání funkce s vnořenými funkcemi: ")
rodic()


# Na základě těchto dvou principů
# (předávání funkcí a volání funkcí uvnitř funkcí) fungují dekorátory

# dekorator jako parametr přijímá vždy funkci (většinou označujeme func)
def jednoduchyDekorator(func):
    # uvnitř definujeme wrapper
    def wrapper():
        print("Událost před vykonáním funkce")
        # dvojité zavolání funkce
        func()
        func()
        print("Událost po vykonání funkce")
    return wrapper

# budoucí dekorovaná funkce


def rekniAhoj(): print("Ahoj")


# dekorování funkce předáním funkce jako parametr pro dekorátor
rekniAhojDvakrat = jednoduchyDekorator(rekniAhoj)
print("\nVolání dekorované funkce: ")
rekniAhojDvakrat()

# Existuje ale i jednodušší cesta jak funkci dekorovat stačí využít symbol @


@jednoduchyDekorator
def rekniNashle(): print("Nashle")


print("\nVolání funkce dekorovane pomocí '@': ")
rekniNashle()

# V jazyku pathon existují funkce jako je __name__, __dict__ atd.
# Tyto funkce jsou velice užitečné pro získávání informací,
# ale náš wrapper bohužel znemožnil získávání informací o původní funkci
print(f"\nrekniNashle je: {rekniNashle.__name__}\n")
# rekni nashle se na venek tváří jako wrapper to nechceme


# Pokročilý dekorátor
# U pokročilého dekorátoru využijeme functools, které zabrání,
# aby se naše funkce vydávala za něco jiného než je.


def opakujDvakrat(func):
    # využití functools
    @functools.wraps(func)
    # abychom mohli předávat argumenty do volané funkce použijem *args **kwargs
    def wrapper(*args, **kwargs):
        # zavoláme funkce a předáme do ní všechny argumenty
        # func(*args, **kwargs)
        # vrátíme výsledek funkce
        return func(*args, **kwargs)
        # vrátíme náš vrapper
    return wrapper


@opakujDvakrat()
def zvysOJedna(number, number2, number3): return number + 1


print(f"Zvyš o jedna číslo 1: {zvysOJedna(1)}")
print(f"zvysOJedna je: {zvysOJedna.__name__}\n")
# Závěrem bych ještě chtěl zmínit,
# že dekorátory můžeme uplatňovat uplně stejně i na metody


# def test(args, kwargs):
#     print(args)
#     print(kwargs)


# test([1, 2, 3, 4, 5, 6], {'Tomas': 3, 'Pepa': 4})


# def test(*args, **kwargs):
#     print(args)
#     print(kwargs)


# test(1, 2, 3, 4, 5, 6, Tomas=3, Pepa=4)
