import requests
from bs4 import BeautifulSoup

# some helpers
def merge(original={}, new={}):
    for key, value in new.items():
        original[key] = original.get(key, 0) + value


def crawl(url, links={}):
    resp = requests.get(url)

    if resp.status_code != requests.codes.ok:
        return {}

    # content = unicode(resp.content, errors='replace')
    soup = BeautifulSoup(resp.text)

    for link in soup.body.find_all('a'):
        href = link.get('href')

        if isinstance(href, basestring) and href.startswith('http'):
            links[href] = links.get(href, 0) + 1


def crawler(url, depth=1):
    urls = {}
    crawl(url, urls)
    current = urls

    while depth > 1:
        next_urls = {}
        for item in current:
            crawl(item, next_urls)
        current = next_urls
        merge(urls, next_urls)
        depth -= 1
    return urls


def recursive_crawl(url, depth=1, urls={}):
    next_urls = {}
    crawl(url, next_urls)

    if not next_urls:
        return {}

    merge(urls, next_urls)

    if depth > 1:
        for item in next_urls:
            recursive_crawl(item, depth-1, urls)
    return urls


####
our_urls = {}
#ans = crawler('http://repository.apache.org/snapshots/', 3)
recursive_crawl('http://repository.apache.org/snapshots/', 3, our_urls)

#print type(our_urls)

def print_urls(n={}):
    for k,v in n.items():
        print k, v

#print_urls(ans)
print_urls(our_urls)

