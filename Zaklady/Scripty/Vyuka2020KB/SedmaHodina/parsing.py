import requests
from bs4 import BeautifulSoup

req=requests.get("https://google.com")
#print(req.headers)
#print(req.text)
#print(req.content.decode(req.encoding))
soup = BeautifulSoup(req.text, 'html.parser')
print(soup.a.string)
urls=[a.get('href') for a in soup.find_all('a')]
print(urls)
#print(soup.prettify())