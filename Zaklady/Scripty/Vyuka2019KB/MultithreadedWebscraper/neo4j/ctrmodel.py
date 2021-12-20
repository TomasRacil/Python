from py2neo.ogm import Repository

from .model import WebPage

repo = Repository("bolt://neo4j@localhost:7687", password="heslo123")


def expandMap(rootUrl,targetUrls):
    temp1=rootUrl.split("://www.")
    temp2=temp1[1].split("/")
    root=WebPage(url=rootUrl,ssl=True if temp1[0][-1]=='s' else False,name=temp2[0])
    if not repo.exists(root):
        repo.save(root)
    for ur in targetUrls:
        temp1=ur.split("://www.")
        temp2=temp1[1].split("/")
        to=WebPage(url=ur, ssl=True if temp1[0][-1]=='s' else False,name=temp2[0])
        if not repo.exists(root):
            repo.save(to)
        root.connected_webpages.add(to)
    repo.save(root)

#expandMap("https://www.google.com",["https://www.maps.google.com","https://www.play.google.com"])