from modules.formule import *

userInput = True    #prenastavit nazacatku na False pro zadavani vyrokovych formuli primo do pragramu
if (userInput):
    print("************************************************************")
    print("Pro zapisování výrokových formulí používat pouze tyto znaky:\n~ \tnegace\n/\ \tkonjunkce\n\/ \tdisjunkce\n==> \timplikace\n<=> \tekvivalence")
    print("p q r \tpro označení elementárních výroků\n{}[]() \tzávorky\n! mezi operací a negací musí být vždy mezera\n")
    print("************************************************************")
    formule = input("Zadejte výrokovou formuli: ")
else: formule = ("~p/\q==> ~(r\/p)") #sem zadávat formule
result = Solve(Parsing(formule))
Vypis(formule,result)