import requests
import re
from os.path import join, dirname, realpath
from os import stat
from math import floor
from collections import Counter

# slova=re.findall(re_vety,bible)
# unikatni_slova = set(slova)
# # slova_pocty = {slovo:slova.count(slovo) for slovo in unikatni_slova}
# # print(slova_pocty)

# n=randrange(len(unikatni_slova))
def get_dictionary_of_words_re(text:str):
    re_slovo = r'[A-Za-z]+'
    text = text.lower()
    slova=re.findall(re_slovo,text)
    counter = Counter(slova)
    return counter.most_common(10)
        

def get_dictionary_of_words(text:str):
    word_dict={}
    slovo=[]
    delka=len(text)
    last=0
    for idx,char in enumerate(text):
        char= char.lower()
        if (floor(idx/delka*100)>last):
            last=floor(idx/delka*100)
            print(last, end='\r')
        if re.match('[A-Za-z]',char):
            slovo.append(char)
        elif slovo!=[]:
            slovo_str=''.join(slovo)
            if word_dict.get(slovo_str)==None:
                word_dict[slovo_str]=1
            else:
                word_dict[slovo_str]+=1
            slovo=[]
    return word_dict

path = join(dirname(realpath(__file__)), "bible.txt")

try:
    file_size =  stat(path).st_size
except FileNotFoundError:
    file_size =0

if not file_size>0:
    with open(path ,'w',encoding='utf-8') as f:
        x = requests.get('https://www.gutenberg.org/ebooks/8300.txt.utf-8')
        f.write(x.text)

with open(path,'r',encoding='utf-8') as f:
    bible=f.read()
  
# print(get_dictionary_of_words(bible))
print(get_dictionary_of_words_re(bible))
