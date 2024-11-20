import random

def faktorial(cislo:int)->int:
    if cislo<0: raise Exception("Cislo je mensi jak nula.")
    faktorial = 1
    for i in range(1, cislo + 1):
        faktorial *= i
    return faktorial

def faktorialRekurze(cislo:int)->int:
  if cislo<0: raise Exception("Cislo je mensi jak nula.")
  if cislo == 0:
    return 1
  else:
    return cislo * faktorialRekurze(cislo - 1)
  
def kontrolaHesla(heslo:str)->bool:
  if len(heslo) < 8:
    return False

  maVelkePismeno = False
  maMalePismeno = False
  maCislici = False

  for znak in heslo:
    if znak.isupper():
      maVelkePismeno = True
    elif znak.islower():
      maMalePismeno = True
    elif znak.isdigit():
      maCislici = True

  return maVelkePismeno and maMalePismeno and maCislici

def hadejNahodneCislo()->None:
    nahodneCislo = random.randint(1, 10)
    tip = 0
    pocetPokusu = 0

    print("Myslim si cislo mezi 1 a 10. Zkus ho uhodnout!")

    while tip != nahodneCislo:
        try:
            tip = int(input("Zadej svuj tip: "))
        except ValueError:
           print("To asi neni cislo.")
           continue
        pocetPokusu += 1

        if tip < nahodneCislo:
            print("Moje cislo je vetsi.")
        elif tip > nahodneCislo:
            print("Moje cislo je mensi.")
        else:
            print("Gratuluji! Uhodl jsi moje cislo", nahodneCislo, "na", pocetPokusu, "pokusu.")

if __name__=="__main__":
    try:
        cislo:int = int(input("Zadejte cele cislo: "))
        print("Faktorial cisla", cislo, "je:", faktorial(cislo))
        print("Faktorial cisla", cislo, "je:", faktorialRekurze(cislo))
    except ValueError:
       print("To asi neni cislo.")
    except Exception as e:
       print(e)

    

    heslo = input("Zadejte heslo: ")
    print("Platne" if kontrolaHesla(heslo) else "Neplatne")

    hadejNahodneCislo()