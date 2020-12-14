import argparse

def vypisPascal(n) : 
    
    k = 2*n - 2 

    for i in range(0, n):

      for j in range(0, k):
        print(end=" ")

      k=k-1

      for z in range(0, i+1):
        print(binomickyKoeficient(i,z), end=" ")

      print("\n")      
      
def binomickyKoeficient(n, k) : 
    vysledek = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        vysledek = vysledek * (n - i) 
        vysledek = vysledek // (i + 1) 
      
    return vysledek 

parser = argparse.ArgumentParser(description='Velikost posloupnosti -n počet')
parser.add_argument('-n', metavar='pocet', type=int, default="Nebyla zadána velikost posloupnosti", help='Zadejte velikost posloupnosti větší než 0')
args=parser.parse_args()

if(args.n<=0):
  print("Zadejte číslo větší než 0!")
else:
  vypisPascal(args.n)




#13. Vytvořte program vypisující fibonaciho posloupnost ve tvaru pyramidy do konzole. 
#Velikost posloupnosti předáte pomocí vlajky při spuštění scriptu. (1)
#ukázka:
#      1
#    1   1
#  1   2   1
#      ...
