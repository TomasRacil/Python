import requests
from bs4 import BeautifulSoup
import webbrowser


while True:
    address = requests.get("https://en.wikipedia.org/wiki/Special:Random")#získá html adresu random článku
    html = BeautifulSoup(address.content, 'html.parser')#html kód
    title = html.find(id = "firstHeading").text#získá titulek
    print(title + "\nChcete tento článek? (Y/N)")
    ans = str(input(""))
    if (ans.lower() == "y"):
        url = 'https://en.wikipedia.org/wiki/%s' %title
        webbrowser.open(url)
        break
    elif (ans.lower() == "n"):
        #print("\nHledám jiný")
        continue
    else:
        print("Špatná odpověď!")
        break