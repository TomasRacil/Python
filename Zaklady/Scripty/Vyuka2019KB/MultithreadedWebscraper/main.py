# from time import sleep
import requests
from bs4 import BeautifulSoup
import re
import queue
import threading
import time

workQueue = queue.Queue()

# def getUrls(url):
#     page = requests.get(url)
#     if page.status_code==200:
#         soup = BeautifulSoup(page.text, 'html.parser')
#         urls=soup.find_all('a')
#         urlsToVisit=[]
#         for ur in urls:
#             href=ur.get('href')
#             #href.startswith(root_url)
#             if href!='/':
#                 urlsToVisit.append(href)
#     return urlsToVisit

# print(getUrls("https://www.google.com"))
    

exitFlag=0

def getUrls(url):
    try:
        page = requests.get(url,timeout=(3, 30))
        if page.status_code==200:
            soup = BeautifulSoup(page.text, 'html.parser')
            urls=soup.find_all('a')
            urlsToVisit=[]
            for ur in urls:
                href=ur.get('href')
                if href[0]!='/':
                    urlsToVisit.append(href)
            queueLock.acquire()
            for ur in urlsToVisit:
                print(id,ur)
                workQueue.put(ur)
            queueLock.release()
    except:
        pass


class Crawler(threading.Thread):

    def __init__(self,id,q):
        super().__init__()
        self.id=id
        self.q=q
        print(f"{id}: crawler vytvoren")
    
    def run(self):
        while exitFlag==0:
            urlToCrawl=''
            queueLock.acquire()
            if not workQueue.empty():
                urlToCrawl=workQueue.get()
            queueLock.release()
            if len(urlToCrawl)>0: getUrls(urlToCrawl)
            time.sleep(1)
        print(f"{self.id}: ukoncuji se")

    
queueLock = threading.Lock()
workQueue = queue.Queue()
ids=[1,2,3,4]
crawlers=[]

url="https://adventofcode.com/2021/"
workQueue.put(url)

for id in ids:
    crawler=Crawler(id,workQueue)
    crawler.start()
    crawlers.append(crawler)



time.sleep(10)

exitFlag = 1

for crawler in crawlers:
   crawler.join()
print ("Exiting Main Thread")


#print(getUrls(url))
