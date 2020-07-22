#!/usr/bin/env python3

"""Simple Python 3 web crawler, to be extended for various uses.
"""
import sys
import getopt
import os
import validators
from urllib.parse import urldefrag, urljoin, urlparse

from lib.counter import Counter
from lib.crawler import spider
from lib.usage import usage, banner, title, extract,options
import lib.settings as settings


def main(argv):
    settings.init()

    try:
        opts, args = getopt.getopt(argv,"hu:p:s:U:t:dm:T:H:R",["help","url=","test","pipeline=","subs-collector=","url-collector=","threads=","domains","maxpages=","header=","robots","timeout="])
    except getopt.GetoptError as err:
        print(str(err))
        print()
        usage()
    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-s","--subs-collector"):
            settings.subscollect = a
        elif o in ("-U","--url-collector"):
            settings.urlcollect = a       
        elif o in ("-d","--domains"):
            settings.domain = False
        elif o in ("-m","--maxpages"):
            if int(a) < 0 :
                print("Maxpages must be equal or greater than 0.")
                exit(0)
            settings.maxpages = int(a)
        elif o in ("-p","--pipeline"):
            if a not in ("urls","domains"):
                print("Wrong pipeline option")
                print()
                usage()
            settings.pipeline = a
        elif o in ("-u","--url"):
            if not validators.url(a) and not os.path.isfile(a):
                print("Please input a valid url or file of urls")
                exit(0)
            settings.url = a
        elif o in ("-t","--threads"):
            if int(a) <= 0:
                print("Threads must be greater than 0.")
                exit(0)
            settings.threads = int(a)
        elif o in ("-T","--test"):
            test = True
        elif o in ("-H","--header"):
            header, value = a.split(":")
            settings.header.update({header.strip() : value.strip()})
        elif o in ("-R","--robots"):
            settings.robots = True
        elif o in ("--timeout"):
            settings.timeout = a
        else:
            print(o)
            assert False,"Unhandle option"

    # set stdout to support UTF-8
    sys.stdout = open(sys.stdout.fileno(), mode="w", encoding="utf-8", buffering=1)
    if settings.pipeline == "":
        banner()
        options()
    if settings.test:
        if settings.pipeline == "":
            title("Test mode")
        subs, urls = spider(startpage="https://www.microsoft.com", maxpages=10,singledomain=True)        
    else:
        subs, urls = spider(startpage=settings.url, maxpages=settings.maxpages,singledomain=settings.domain)
    if len(settings.pipeline) == 0 :
        title("founded subdomains")
        for sub in subs:
            print(sub)
    
    if len(settings.subscollect) > 0:
        extract(settings.subscollect,subs)
    
    if len(settings.urlcollect) > 0:
        extract(settings.urlcollect,urls) 