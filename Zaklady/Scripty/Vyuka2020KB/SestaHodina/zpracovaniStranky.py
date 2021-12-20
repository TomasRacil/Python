import requests
import re

stazena=False
with open("C:\Vyuka\Python\Zaklady\Scripty\Vyuka2020KB\SestaHodina\kniha.txt","rb") as f:
    if len(f.read())>0: stazena=True

if not stazena:
    print("Stahovani")
    r = requests.get('https://www.gutenberg.org/files/1342/1342-0.txt')
    if r.status_code == 200:
        with open("C:\Vyuka\Python\Zaklady\Scripty\Vyuka2020KB\SestaHodina\kniha.txt","wb") as f:
            f.write(r.content)
else:
    print("Kniha stazena")

with open("C:\Vyuka\Python\Zaklady\Scripty\Vyuka2020KB\SestaHodina\kniha.txt","rb") as f:
    # for radek in f:
	#     input(radek.decode("utf-8").strip())
    kniha=f.read().decode("utf-8")
    jmena=set(re.findall(r"(Mr.|Mrs.|Miss|Colonel) ([A-Z][a-z]+)",kniha))
    print(jmena)
    print()
    jmena2=set(re.findall(r"\b([A-Z][a-z]+) ([A-Z][a-z]+)",kniha))
    print(jmena2)