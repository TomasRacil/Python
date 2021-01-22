from exchangeratesapi import Api

def DostanKurzy(zadanaMena):
    """
    ziskava kurzy z Evropske narodni banky diky knihobne exchangeratesapi
    odmaze nepotrebny text
    rozparcuje
    """
    kurzy=str(Api().get_rates(zadanaMena)).split(",")
    for i in range(len(kurzy)):     
        kurzy[i]=kurzy[i].replace("'",'')
        kurzy[i]=kurzy[i].replace("{",'')
        kurzy[i]=kurzy[i].replace("}",'')
        kurzy[i]=kurzy[i].replace(" ",'')

        kurzy[i]=kurzy[i].split(":")

        if("rates" in kurzy[i][0]):
            del kurzy[i][0]

    if("date" in kurzy[len(kurzy)-1][0]):
        del kurzy[len(kurzy)-1]
    if("base" in kurzy[len(kurzy)-1][0]):
        del kurzy[len(kurzy)-1]
    return kurzy

def GetValidCurrency():
    #TODO: dostupne meny by nemeli mit fixne definovane meny, ale mely by cerpat data z webu. Vzhledem k tomu ze jsem se s tim vypisoval, nehodlam to ja upravovat.
    dostupneMeny=["CAD","HKD","ISK","PHP","DKK","HUF","CZK","GBP","RON","SEK","IDR","INR","BRL","RUB","HRK","JPY","THB","CHF","EUR","MYR","BGN","TRY","CNY","NOK","NZD","ZAR","USD","MXN","SGD","AUD","ILS","KRW","PLN"]
    return dostupneMeny