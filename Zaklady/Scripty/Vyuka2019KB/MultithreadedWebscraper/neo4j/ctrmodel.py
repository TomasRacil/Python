"""allow web map expansion"""
import re

from py2neo.ogm import Repository

from .model import WebPage

repo = Repository("bolt://neo4j@neo4j:7687", password="test")


def expand_map(root_url, target_urls):
    """_summary_

    Args:
        rootUrl (_type_): _description_
        targetUrls (_type_): _description_
    """
    temp = re.split(r'^(http[s]?)://w{0,3}\.?([a-z0-9\._-]+)/?(.*)',root_url)
    root = WebPage(
        url=root_url, ssl=True if temp[1][-1] == "s" else False, name=temp[2]
    )
    if not repo.exists(root):
        repo.save(root)
    for url in target_urls:
        temp = re.split(r'^(http[s]?)://w{0,3}\.?([a-z0-9\._-]+)/?(.*)',url)
        to = WebPage(url=url, ssl=True if temp[1][-1] == "s" else False, name=temp[2])
        if not repo.exists(root):
            repo.save(to)
        root.connected_webpages.add(to)
    repo.save(root)


# expandMap("https://www.google.com",["https://www.maps.google.com","https://www.play.google.com"])
