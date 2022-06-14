from modules.formule import *

userInput = True    #přenastavit nazačátku na False pro zadáváni výrokových formulí přímo do programu
if (userInput):
    print("************************************************************")
    print("Pro zapisování výrokových formulí používat pouze tyto znaky:\n~ \tnegace\n/\ \tkonjunkce\n\/ \tdisjunkce\n==> \timplikace\n<=> \tekvivalence")
    print("{}[]() \tzávorky\npísmena abecedy (všechna malá i velká) pro označení elementárních výroků\nmezi operací a negací musí být vždy mezera")
    print("************************************************************")
    formule = input("Zadejte výrokovou formuli: ")
else: formule = ("~A /\ a <=> ~(q ==> (~~~q \/ ~~p))") #sem zadávat formule

matrices = SetMatrices(formule)
result = Solve(matrices,Parsing(formule))
Vypis(matrices,formule,result)