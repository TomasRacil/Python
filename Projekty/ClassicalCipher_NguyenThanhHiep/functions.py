from personal import *


def Encrypt1(temp):
    encoded=""
    for i in range(len(temp)):
        cislo=((ord(temp[i])+m_KeyShift-32) % 95)+32 #there are 95 letters that can be printed(from index 32)
        encoded+= chr(cislo)
    return encoded
def Encrypt2(temp):
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
def Encrypt3(temp):
        encoded=""
        for i in range(len(temp)):
            cislo=(m_IndexVariable+ ord(temp[i]))^m_XoredNumber
            encoded+= chr(cislo)
        return encoded
def Encrypt4(temp):
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
    
def Decrypt1(temp):
        decoded=""
        for i in range(len(temp)):
            cislo=((ord(temp[i])-m_KeyShift-32) % 95)+32  
            decoded += chr(cislo)
        return decoded
def Decrypt2(temp):
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
def Decrypt3(temp):
        decoded=""
        for i in range(len(temp)):
            cislo=(m_IndexVariable+ord(temp[i]))^m_XoredNumber
            decoded+= chr(cislo)
        return decoded
def Decrypt4(temp):
        decoded=""
        orderedList= sorted(m_Keyword)
        t=len(temp)//len(m_Keyword)
        for m in range(t):
            for j in range(len(orderedList)):
                for i in range(len(m_Keyword)):
                    if orderedList[j]==m_Keyword[i]:
                        decoded+= temp[i*t+m]
        return decoded