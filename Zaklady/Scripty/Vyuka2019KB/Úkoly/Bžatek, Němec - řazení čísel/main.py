from random import randint

from Sort import *

def vytvorSoubor(nameFile):
    soubor=open(nameFile,"w+")
    soubor.close()

def generateValuesInFile(nameFile):
    
    soubor=open(nameFile,"w")
    for i in range(10000):
        soubor.write(str(randint(0,100000))+"\n")  

    soubor.close()

def loadValuesFromFile(nameFile):
    intArray=[]
    soubor=open(nameFile,"r")
    for line in soubor:
        intArray.append(int(line.split('\n')[0]))

    return intArray

def printArray(array):
    for i in range(len(array)):
        print(str(array[i]))

vytvorSoubor("soubor1.txt")
vytvorSoubor("soubor2.txt")

generateValuesInFile("soubor1.txt")
generateValuesInFile("soubor2.txt")

hodnoty1=loadValuesFromFile("soubor1.txt")
hodnoty2=loadValuesFromFile("soubor2.txt")

sorter(hodnoty1, "soubor1_sorted.txt")
sorter(hodnoty2, "soubor2_sorted.txt")

print(findSame(open("soubor1_sorted.txt", "r"), open("soubor2_sorted.txt", "r")))

#printArray(hodnoty1)
#printArray(hodnoty2)
