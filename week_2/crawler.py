import requests
from bs4 import BeautifulSoup
import re


def merge(original={}, new={}):
    for key, value in new.items():
        original[key] = original.get(key, 0) + value


def crawl(url, next_urls={}):
    resp = requests.get(url)
    if resp.status_code != requests.codes.ok:
        return
    content = unicode(resp.content, errors='replace')
    soup = BeautifulSoup(content)
    for link in soup.find_all('a'):
        href = link.get('href')
        try:
            m = re.search(r"^http", href)
        except TypeError:
            m = False
        if m:
            next_urls[href] = next_urls.get(href, 0) + 1


def crawler(url, depth=1):
    urls = {}
    crawl(url, urls)

    current = urls
    while depth > 1:
        next_urls = {}
        for u in current.keys():
            crawl(u, next_urls)
        current = next_urls
        merge(urls, next_urls)
        depth -= 1
    if depth == 1:
        return urls

our_urls = {}
def recursive_crawl(url, depth=1, urls={}):
    resp = requests.get(url)
    if resp.status_code != requests.codes.ok:
        return {}

    next_urls = {}
    content = unicode(resp.content, errors='ignore')
    soup = BeautifulSoup(content)
    for link in soup.find_all('a'):
        href = link.get('href')
        try:
            m = re.search(r"^http", href)
        except TypeError:
            m = False
        if m:
            next_urls[href] = next_urls.get(href, 0) + 1
    merge(urls, next_urls)
    if depth > 1:
        #merge(urls, next_urls)
        print urls
        for u in next_urls.keys():
            recursive_crawl(u, depth-1, urls)
    if depth == 1:
        return urls

#ans = crawler('http://repository.apache.org/snapshots/', 3)
recursive_crawl('http://repository.apache.org/snapshots/', 3, our_urls)

def print_urls(n={}):
    for k,v in n:
        print k, v

print_urls(our_urls)
