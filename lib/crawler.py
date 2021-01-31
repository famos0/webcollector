#!/usr/bin/env python3

import collections
import sys
import getopt
import os
import threading
import time
from urllib.parse import urldefrag, urljoin, urlparse
from lib.counter import Counter

import bs4
import requests

from lib.usage import title
from lib.robots import get_robots
from lib.requester import Requester
from lib.response import Response

class Controller(object):

    def __init__(self, startpage, cookies = {}, maxpages = 500, singledomain = True, concurancy = 10, robots = False, timeout = 0, header = {}, dump = False, proxy = None):
        self.pages = Counter()
        self.startpage = startpage
        self.maxpages = maxpages
        self.singledomain = singledomain
        self.robots = robots
        self.header = header
        self.dump = dump
        self.concurancy = concurancy
        self.crawled = collections.deque()
        self.urlqueue = collections.deque()
        self.timeout = timeout
        self.cookies = cookies

        if proxy != None:
            self.proxy = { urlparse(proxy).scheme : proxy}
        else:
            self.proxy = proxy

    def crawl(self, sess, url, domain):
        self.crawled.append(url)
        self.pages.increment()
        requester = Requester(url = url, session = sess, proxy = self.proxy, headers = self.header, cookies = self.cookies)
        response = requester.request()
        try: 
            if response != None:
                if self.dump:
                    response.dump(self.dump) 
                if self.pagehandler(url, response):

                    if response.status in [300,301,302,303,304,305,306,307,308]:
                        link = response.headers["Location"]
                        link if bool(urlparse(link).netloc) else urljoin(url, link)
                        if not self.url_in_list(link, self.crawled) and not self.url_in_list(link, self.urlqueue):
                            self.urlqueue.append(link)

                    if response.headers["content-type"].startswith("text/html"):
                            soup = response.soup()
                            # get the links from this page and add them to the queue
                            links = self.getlinks(url, domain, soup)
                            for link in links:
                                if not self.url_in_list(link, self.crawled) and not self.url_in_list(link, self.urlqueue):
                                    self.urlqueue.append(link)
                time.sleep(int(self.timeout))
            else:
                time.sleep(int(self.timeout))
                return None
        except: 
            return None

    def spider(self):
        self.show()

        self.urlqueue.append(self.startpage)
        domain = urlparse(self.startpage).netloc if self.singledomain else None

        if self.robots and domain:
            self.urlqueue.extend(get_robots(domain))
        sess = requests.session()  

        while 1:
            if self.pages.value == self.maxpages and self.maxpages != 0:
                break
            if self.urlqueue:
                if threading.active_count() <= self.concurancy:
                    url = self.urlqueue.popleft()  # FIFO
                    t = threading.Thread(target=self.crawl,args=(sess,url,domain,))
                    t.start()
            else:
                if threading.active_count() == 1:
                    time.sleep(1)
                    if not self.urlqueue:
                        break
                

        #while ((self.urlqueue or threading.active_count() > 1) and (True if self.maxpages == 0 else self.pages.value < self.maxpages)):
        print(self.urlqueue)
        print()
        while threading.active_count() > 1: continue

        print()
        print("{0} pages crawled".format(self.pages.value))
        return self.crawled

    def getlinks(self, url, domain, soup):
    
        # get target URLs for all links on the page
        links = [a.attrs.get("href") for a in soup.select("a[href]")]
        
        # remove fragment identifiers
        links = [urldefrag(link)[0] for link in links]

        # remove any empty strings
        links = [link for link in links if link]

        # if it's a relative link, change to absolute
        links = [
            link if bool(urlparse(link).netloc) else urljoin(url, link)
            for link in links
        ]
        # if only crawing a single domain, remove links to other domains
        if domain:
            links = [link for link in links if self.samedomain(urlparse(link).netloc, domain)]
        return links

    def pagehandler(self, url, response):

        print("{} : {}".format(url,str(int(response))))
        return True


    def samedomain(self, netloc1, netloc2):
        """Determine whether two netloc values are the same domain."""
        domain1 = netloc1.lower()
        if "." in domain1:
            domain1 = domain1.split(".")[-2] + "." + domain1.split(".")[-1]
        if isinstance(netloc2,str):
            domain2 = netloc2.lower()
            if "." in domain2:
                domain2 = domain2.split(".")[-2] + "." + domain2.split(".")[-1]
            return domain1 == domain2
        else:
            domain2 = []
            for nt2 in netloc2:
                d2 = nt2.lower()
                if "." in d2:
                    d2 = d2.split(".")[-2] + "." + d2.split(".")[-1]
                domain2.append(d2)
            return domain1 in domain2


    def url_in_list(self, url, listobj):
        http_version = url.replace("https://", "http://")
        https_version = url.replace("http://", "https://")
        return (http_version in listobj) or (https_version in listobj)

    def show(self):
        print("Starting from : {}".format(self.startpage))
        print("Maximum pages crawled: "+str(self.maxpages))
        print("Number of thread(s): "+str(self.concurancy))
        print("Header: "+str(self.header))
        print("Feeding with robots.txt: "+("Yes" if self.robots else "No"))
        print("")