from modules.formule import *

UserInput = True    #prenastavit nazacatku na False pro zadavani vyrokovych formuli primo do pragramu
if (UserInput):
    print("************************************************************")
    print("Pro zapisování výrokových formulí používat pouze tyto znaky:\n~ \tnegace\n/\ \tkonjunkce\n\/ \tdisjunkce\n==> \timplikace\n<=> \tekvivalence")
    print("p q r \tpro označení elementárních výroků\n{}[]() \tzávorky\n")
    print("************************************************************")
    formule = input("Zadejte výrokovou formuli: ")
else: formule = ("~(p /\ q)") #sem zadávat formule
result = Solve(Parsing(formule))
Vypis(formule,result)