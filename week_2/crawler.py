import requests
from bs4 import BeautifulSoup
import re

def crawl(url, urls={}):
    resp = requests.get(url)
    if resp.status_code == requests.codes.ok:
        soup = BeautifulSoup(resp.content)
        for link in soup.find_all('a'):
            href = link.get('href')
            try:
                m = re.search(r"^http", href)
            except TypeError:
                m = False
            if m:
                urls[href] = urls.get(href, 0) + 1


def crawler(url, depth):
    if depth < 1:
        return []

    urls = {}
    crawl(url, urls)

    while depth > 1:
        for url in urls.keys():
            crawl(url, urls)
        depth -= 1

    return urls


# recursive crawler
def r_crawler(url, depth, urls = {}):
    resp = requests.get(url)
    if resp.status_code != requests.codes.ok:
        return

    soup = BeautifulSoup(resp.content)
    for link in soup.find_all('a'):
        href = link.get('href')
        try:
            m = re.search(r"^http", href)
        except TypeError:
            m = False

        if m:
            urls[href] = urls.get(href, 0) + 1

    if depth > 1:
        for u in urls.keys():
            r_crawler(u, depth-1, urls)
    return urls


ans = crawler('http://repository.apache.org/snapshots/', 2)
#ans = crawler('http://i.ua', 2)
#ans = r_crawler('http://repository.apache.org/snapshots/', 3, urls = {})
for i, v in ans.items():
    print i, v
