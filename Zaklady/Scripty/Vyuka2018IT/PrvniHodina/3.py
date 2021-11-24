cislo=int(input("Zadej cislo: "))

def recurFaktorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recurFaktorial(n-1)

print(recurFaktorial(cislo))