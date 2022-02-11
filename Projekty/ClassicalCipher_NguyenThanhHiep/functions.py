from personal import *


def EncryptCaseShift(temp):
    """
        Todo: Nahradit znak znakem s posunem m_KeyShift
        Arg: plaintext
        Return: sifrovany text
    """
    encoded=""
    for i in range(len(temp)):
        cislo=((ord(temp[i])+m_KeyShift-32) % 95)+32 #there are 95 letters that can be printed(from index 32)
        encoded+= chr(cislo)
    return encoded

def EncryptCaseSubtitution(temp):
    """
        Todo: Nahradit znak dalsim znakem ve retezci(list m_Zobrazeni obsahuje retezci), ktera obsahuje tento znak
        Arg: plaintext
        Return: sifrovany text
    """ 
    encoded=""
    for i in range(len(temp)):
        isFounded= False
        for j in range(len(m_Zobrazeni)):
            index = m_Zobrazeni[j].find(temp[i])
            if ( index!= -1):
                isFounded= True
                if (index == len(m_Zobrazeni[j]) - 1):
                    encoded+=m_Zobrazeni[j][0]
                else:
                    encoded+=m_Zobrazeni[j][index+1]
                break
        if(isFounded==False):
            encoded+=temp[i]
    return encoded

def EncryptCaseXor(temp):
    """
        Todo: Nahradit znak znakem s indexovym cislem, ktere je vysledek funkce XOR mezi indexovym cislem toho znak
            a m_XoredNumber ( indexove cislo znaku je soucet ASCII cislo a m_IndexVariable) 
        Arg: plaintext
        Return: sifrovany text
    """
    encoded=""
    for i in range(len(temp)):
        cislo=(m_IndexVariable+ ord(temp[i]))^m_XoredNumber
        encoded+= chr(cislo)
    return encoded

def EncryptCaseColumnar(temp):
    """
        Todo: https://cs.wikipedia.org/wiki/Transpozi%C4%8Dn%C3%AD_%C5%A1ifra
        Arg: plaintext
        Return: sifrovany text
    """
    encoded=""
    orderedList= sorted(m_Keyword)
    for i in range(len(m_Keyword)):
        for j in range(len(orderedList)):
            if orderedList[j]==m_Keyword[i]:
                k=j
                while(k+1<=len(temp)+len(m_Keyword)-len(temp)%len(m_Keyword)):
                    if k+1<=len(temp):
                        encoded+= temp[k]
                        k+= len(m_Keyword)
                    else:
                        encoded+= "*" #libovolny znak
                        break
    return encoded
    
def DecryptCaseShift(temp):
        """
            Todo: vracena funkce EncryptCaseShift
            Arg: cipher text
            Return: desifrovany text
        """
        decoded=""
        for i in range(len(temp)):
            cislo=((ord(temp[i])-m_KeyShift-32) % 95)+32  
            decoded += chr(cislo)
        return decoded
def DecryptCaseSubtitution(temp):
        """
            Todo: vracena funkce EncryptSubtitution
            Arg: cipher text
            Return: desifrovany text
        """
        decoded=""
        for i in range(len(temp)):
            isFounded=False
            for j in range(len(m_Zobrazeni)):
                index = m_Zobrazeni[j].find(temp[i])
                if ( index!= -1):
                    isFounded= True
                    if (index == 0):
                        decoded+=m_Zobrazeni[j][len(m_Zobrazeni[j])-1]
                    else:
                        decoded+=m_Zobrazeni[j][index-1]
                    break
            if(isFounded== False):
                decoded+=temp[i]
        return decoded
def DecryptCaseXor(temp):
        """
            Todo: vracena funkce EncryptCaseXor
            Arg: cipher text
            Return: desifrovany text
        """
        decoded=""
        for i in range(len(temp)):
            cislo=(m_IndexVariable+ord(temp[i]))^m_XoredNumber
            decoded+= chr(cislo)
        return decoded
def DecryptCaseColumnar(temp):
        """
            Todo: vracena funkce DecryptCaseColumnar
            Arg: cipher text
            Return: desifrovany text
        """
        decoded=""
        orderedList= sorted(m_Keyword)
        t=len(temp)//len(m_Keyword)
        for m in range(t):
            for j in range(len(orderedList)):
                for i in range(len(m_Keyword)):
                    if orderedList[j]==m_Keyword[i]:
                        decoded+= temp[i*t+m]
        return decoded