import requests
from bs4 import BeautifulSoup
import webbrowser

def soup():
    """Funkce pomocí odkazu https://en.wikipedia.org/wiki/Special:Random
    načte náhodný článek v html kódu, vypíše titulek a první odstavec
    a nabídne jeho zobrazení ve webovém prohlížeči
    """
    while True:
        address = requests.get("https://en.wikipedia.org/wiki/Special:Random")      #získá html adresu náhodného článku pomocí odkazu
        html = BeautifulSoup(address.content, 'html.parser')                        #získá html kód článku
        title = html.find(id = "firstHeading").text                                 #získá titulek článku
        odstavec = html.find_all('p')                                               #získá odstavece v html
        print(title + "\n\n" + odstavec[0].text + "\nChcete tento článek? (Y/N)")   #získá první odstavec textu 
        ans = str(input(""))                                                        # a společně s titulkem je vypíše
        if (ans.lower() == "y"):
            url = 'https://en.wikipedia.org/wiki/%s' %title
            webbrowser.open(url)
            break
        elif (ans.lower() == "n"):
            continue
        else:
            print("Špatná odpověď!")
            break