m_Zobrazeni=["qwert","yuiop","asdfg","hjkl","zxcvb","nm","QWERT","YUIOP","ASDFG","HJKL","ZXCVB","NM"]
def Sifrovej():
    encoded=""
    text=input("[?]enter text:\n")
    for i in range(len(text)):
        isFounded= False
        for j in range(len(m_Zobrazeni)):
            index = m_Zobrazeni[j].find(text[i])
            if ( index!= -1):
                isFounded= True
                if (index == len(m_Zobrazeni[j]) - 1):
                    encoded+=m_Zobrazeni[j][0]
                else:
                    encoded+=m_Zobrazeni[j][index+1]
                break
        if(isFounded==False):
            encoded+=text[i]
    print("[+]encoded text:\n{}".format(encoded))

def Desifrovej():
    decoded=""
    text=input("[?]enter text:\n")
    for i in range(len(text)):
        isFounded=False
        for j in range(len(m_Zobrazeni)):
            index = m_Zobrazeni[j].find(text[i])
            if ( index!= -1):
                isFounded= True
                if (index == 0):
                    decoded+=m_Zobrazeni[j][len(m_Zobrazeni[j])-1]
                else:
                    decoded+=m_Zobrazeni[j][index-1]
                break
        if(isFounded== False):
            decoded+=text[i]
    print("[+]decoded text:\n{}".format(decoded))

def SetZobrazeni(zobrazeni):
    m_Zobrazeni=zobrazeni
