# from time import sleep
import requests
from bs4 import BeautifulSoup
import re
import queue
import threading
import time

exitFlag=False

class Crawler(threading.Thread):

    def __init__(self,id,q):
        super().__init__()
        self.id=id
        self.q=q
        print(f"{id}: crawler vytvoren")
    
    def run(self):
        print (f"{self.id} spousteni ... ")
        crawl(self.id,self.q)
        print(f"{self.id}: ukoncuji se...")

def crawl(id,q):
    while True:
        try:
            urlToCrawl=q.get(timeout=0.2)
            #urlToCrawl=q.get(False)
            #print(urlToCrawl)
            getUrls(id,urlToCrawl)
        except queue.Empty:
            print(id,": dotaz ")
            pass
        if exitFlag:
                break

def getUrls(id,url):
    try:
        page = requests.get(url,timeout=(3, 30))
        if page.status_code==200 and not page==None:
            soup = BeautifulSoup(page.text, 'html.parser')
            urls=soup.find_all('a')
            urlsToVisit=[]
            for ur in urls:
                href=ur.get('href')
                #input(href)
                if href[0]!='/':
                    #if not href.split("/")[2]==url.split("/")[2]:
                    urlsToVisit.append(href)
            for ur in urlsToVisit:
                print(f"{id}: from: {url} page: {ur}")
                workQueue.put(ur)
    except Exception as e:
        print(id,": ERROR",url,e)



if __name__=="__main__":
    workQueue = queue.Queue()
    ids=[1,2]
    crawlers=[]

    url="https://www.google.com"

    workQueue.put(url)

    for id in ids:
        crawler=Crawler(id,workQueue)
        crawler.start()
        crawlers.append(crawler)
    
    


    time.sleep(2)

    exitFlag = True

    for crawler in crawlers:
        crawler.join()
    print ("Exiting Main Thread")


    #print(getUrls(url))
