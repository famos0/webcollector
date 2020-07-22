import requests
from urllib.parse import urljoin,urlparse

def create_url(parent,url):
    return urljoin(parent,url)

def parse_robots(robots):
    urls= []
    for line in robots.text.splitlines():
        try :
            args,value = line.split(": ")
            if args in ("Disallow","Allow"):
                urls.append(create_url(robots.url,value))
        except:
            continue
    return urls

def get_robots(domain):
    response = requests.get("http://"+domain+"/robots.txt",header=settings.header, proxies=settings.proxy)
    return parse_robots(response)