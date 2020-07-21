#!/usr/bin/env python3

import collections
import sys
import getopt
import os
import threading
from urllib.parse import urldefrag, urljoin, urlparse
from lib.counter import Counter

import bs4
import requests

from lib.usage import title
import lib.settings as settings

pages = Counter()
failed = Counter()

sublist = collections.deque()
crawled = collections.deque()

pagequeue = collections.deque()

def crawl(sess, url, domain):

    try:
        print(url)
        response = sess.get(url,headers = settings.header)
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema):
    # if something wrong in schema
        if len(settings.pipeline) == 0:
            print("*Wrong schema*:", url)
            failed.increment()
        return
    except (requests.exceptions.ConnectionError):
        if len(settings.pipeline) == 0:
            print("*Connection refused*:", url)
            failed.increment()
        return
    if not response.headers["content-type"].startswith("text/html"):
        return  # don't crawl non-HTML content

    soup = bs4.BeautifulSoup(response.text, "html.parser")

    # process the page
    crawled.append(url)
    pages.increment()
    if pagehandler(url, response, soup):
        # get the links from this page and add them to the crawler queue
        links = getlinks(url, domain, soup)
        for link in links:
            if collectsubs(sublist, link):
                sublist.append(urlparse(link).netloc)
            if not url_in_list(link, crawled) and not url_in_list(link, pagequeue):
                pagequeue.append(link)


def spider(startpage, maxpages, singledomain):
    """Crawl the web starting from specified page.

    1st parameter = URL of starting page
    maxpages = maximum number of pages to crawl
    singledomain = whether to only crawl links within startpage's domain
    """
    # queue of pages to be crawled
    pagequeue.append(startpage)
    domain = urlparse(startpage).netloc if singledomain else None
    sess = requests.session()  # initialize the session

    #######################
    #
    # TOADD: fill the buffer with robots.txt
    #
    ########################
    if settings.pipeline == "" :
        print(settings.pipeline)
        title("crawled urls")
    while ((pagequeue or threading.active_count() > 1 )and (True if maxpages == 0  else  pages.value < maxpages)):
        if threading.active_count() <= settings.threads and pagequeue:
            url = pagequeue.popleft()  # get next page to crawl (FIFO queue)
            t = threading.Thread(target=crawl,args=(sess,url,domain,))
            t.start()
    
    while threading.active_count() > 1: continue

    if len(settings.pipeline) == 0:
        print()
        print("{0} pages crawled, {1} links failed.".format(pages.value, failed.value))
    return sublist, crawled


def collectsubs(sublist,url):
    """Check if the tested subdomain's url is already gathered, if not, add it and return the list.

    sublist = list of subdomains
    url = tested url
    """
    sub = urlparse(url).netloc
    if sub.lower() in (string.lower() for string in sublist):
        return False
    else:
        if settings.pipeline == 'domains':
            print(sub)
        return True

def getlinks(pageurl, domain, soup):
    """Returns a list of links from from this page to be crawled.

    pageurl = URL of this page
    domain = domain being crawled (None to return links to *any* domain)
    soup = BeautifulSoup object for this page
    """

    # get target URLs for all links on the page
    links = [a.attrs.get("href") for a in soup.select("a[href]")]

    # remove fragment identifiers
    links = [urldefrag(link)[0] for link in links]

    # remove any empty strings
    links = [link for link in links if link]

    # if it's a relative link, change to absolute
    links = [
        link if bool(urlparse(link).netloc) else urljoin(pageurl, link)
        for link in links
    ]

    # if only crawing a single domain, remove links to other domains
    if domain:
        links = [link for link in links if samedomain(urlparse(link).netloc, domain)]

    return links

def pagehandler(pageurl, pageresponse, soup):
    """Function to be customized for processing of a single page.

    """
    if settings.pipeline !="domains":
        if settings.pipeline=="urls":
            print(pageurl)
        else:
            print(pageurl + " ({0} bytes)".format(len(pageresponse.text)))
    return True


def samedomain(netloc1, netloc2):
    """Determine whether two netloc values are the same domain."""
    domain1 = netloc1.lower()
    if "." in domain1:
        domain1 = domain1.split(".")[-2] + "." + domain1.split(".")[-1]

    domain2 = netloc2.lower()
    if "." in domain2:
        domain2 = domain2.split(".")[-2] + "." + domain2.split(".")[-1]

    return domain1 == domain2


def url_in_list(url, listobj):
    """Determine whether a URL is in a list of URLs."""
    http_version = url.replace("https://", "http://")
    https_version = url.replace("http://", "https://")
    return (http_version in listobj) or (https_version in listobj)