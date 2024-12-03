"""This module does blah blah."""

import re
import queue
import threading
import time
import requests
from bs4 import BeautifulSoup


from db import expand_map


EXIT_FLAG = False


class Crawler(threading.Thread):
    """_summary_

    Args:
        threading (_type_): _description_
    """

    def __init__(self, cid: int, que: queue.Queue):
        super().__init__()
        self.cid = cid
        self.que = que
        print(f"{cid}: crawler vytvoren")

    def run(self):
        print(f"{self.cid} spousteni ... ")
        crawl(self.cid, self.que)
        print(f"{self.cid}: ukoncuji se...")


def crawl(cid: int, que: queue.Queue):
    """_summary_

    Args:
        id (_type_): _description_
        queue (_type_): _description_
    """
    while True:
        try:
            url_to_crawl = que.get(timeout=0.2)
            # urlToCrawl=q.get(False)
            # print(urlToCrawl)
            get_urls(cid, url_to_crawl)
        except queue.Empty:
            # print(cid, ": dotaz ")
            pass
        if EXIT_FLAG:
            break


def get_urls(cid: int, origin_url: str):
    """_summary_

    Args:
        id (int): _description_
        url (str): _description_
    """
    try:
        page = requests.get(origin_url, timeout=(3, 30))
        if page.status_code == 200 and not page is None:
            soup = BeautifulSoup(page.text, "html.parser")
            urls = soup.find_all("a")
            urls_to_visit = []
            for url in urls:
                href = url.get("href")
                if href is not None:
                    if check_url(origin_url, href):
                        urls_to_visit.append(href)
            expand_map(origin_url, urls_to_visit)
            # print(origin_url, urls_to_visit)
            for url in urls_to_visit:
                # print(f"{id}: from: {url} page: {ur}")
                workQueue.put(url)
    except Exception as err:
        print(cid, ": ERROR", url, err)


def check_url(origin_url: str, target_url: str):
    """_summary_

    Args:
        origin_url (str): _description_
        target_url (str): _description_

    Returns:
        _type_: _description_
    """
    try:
        org = re.split(r"^(http[s]?)://w{0,3}\.?([a-z0-9\._-]+)/?(.*)", origin_url)
        tar = re.split(r"^(http[s]?)://w{0,3}\.?([a-z0-9\._-]+)/?(.*)", target_url)
        if len(tar)>1:
            # print(org,tar)
            return True if org[2] != tar[2] else False
    except Exception as err:
        print("ERROR", err)
        return False


if __name__ == "__main__":
    # url0="//www.google.com"
    # url = "https://www.google.com"
    # url1="https://www.google.com/idsad"
    # url3="https://www.maps.google.com"

    # print(checkUrl(url,url1))

    workQueue = queue.Queue()
    ids = [1, 2, 3, 4, 5, 6, 7, 8]
    crawlers = []

    URL = "https://www.google.com"
    # URL = "https://www.youtube.com/"
    workQueue.put(URL)

    for cid in ids:
        crawler = Crawler(cid, workQueue)
        crawler.start()
        crawlers.append(crawler)

    time.sleep(5)

    EXIT_FLAG = True

    for crawler in crawlers:
        crawler.join()
    print("Exiting Main Thread")

    # print(getUrls(url))
