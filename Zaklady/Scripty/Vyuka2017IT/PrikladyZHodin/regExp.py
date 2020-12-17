import re
import requests
import shutil

def savePageContent(url,name):
	r = requests.get(url)
	if r.status_code == 200:
		file=open(name,"w")
		file.write(str(r.content))
		file.close()
	else: print("Stránku se nepodařilo stáhnout")

def getImage(url,name):
	r = requests.get(url, stream=True)
	if r.status_code == 200:
	    with open(name, 'wb') as f:
	        r.raw.decode_content = True
	        shutil.copyfileobj(r.raw, f)  
	else: print("Obrázek se nepodařilo stáhnout") 

def readLocalPage(name):
	file=open(name,"r")
	html=file.read()
	file.close()
	return html

"""url='https://www.python.org/'
savePageContent(url,"WebPage.txt")
content=readLocalPage("WebPage.txt")
pattern = '<img.*?class=".+?".*?src="/([\w/]+/(.+?\..+?))".*?>'
result = re.search(pattern,content)
print(result.group(1))
print(result.group(2))
getImage(url+result.group(1),result.group(2))"""


"""pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
  print("Hledání proběhlo úspěšně")
else:
  print("Hledání bylo neúspěšné")	

print(result)"""

