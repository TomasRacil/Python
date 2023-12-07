import requests
import re
from os.path import join, realpath, dirname, exists

if not exists(join(dirname(realpath(__file__)),"othelo.txt")):
    resp = requests.get("https://www.gutenberg.org/cache/epub/2267/pg2267.txt")
    if resp.ok:
        with open(join(dirname(realpath(__file__)),"othelo.txt"),"x", encoding=resp.apparent_encoding) as file:
            file.write(resp.text)

with open(join(dirname(realpath(__file__)),"othelo.txt"),"r") as file:
    book = file.read()
    #Pocet slov
    slova = re.findall(r"[A-Za-z]+",book)
    print(len(slova))
    # print(slova[:50])
    word_counts = {slovo:slova.count(slovo) for slovo in set(slova)}
    print(sorted(word_counts.items(), key= lambda x : x[1], reverse = True)[:10])
    
    #Pocet vet
    pat = r"(?<=[\.?!:\n)]\s)[A-Z][a-z]*[\s,][\w\s:',-]+\s[\w'-]+[\.?!:\n]\s+(?=[A-Z(])"
    # print(len(re.findall(r"\w+[^.!?]*[.!?]",book))) # Petráš
    # print(len(re.findall(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s",book))) #Tichá
    # print(len(re.findall(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', book))) #Kristlik
    
    book = re.sub(r"(?<=[a-z])\n\n\s*(?=[A-Z])",".\n",book)
    pat = r"(?<=[\.?!])\s+(?=[A-Z])"
    # vety =  re.findall(pat,book)
    vety = [veta for veta in re.split(pat, book) if len(veta.split())>1]
    # for veta in vety[:100]:
    #     print(re.sub(r"\n","",veta))
    #Pocet vet
    print(len(vety))
    #Prumerna delka vety
    print(sum([len(veta) for veta in vety])/len(vety))
    
    sorted_vety = sorted(vety,key=lambda x: len(x))
    for veta in sorted_vety[-20:]:
        print(re.sub(r"\n","",veta))
    
    # 
    
