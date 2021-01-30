#!/usr/bin/env python3

"""Simple Python 3 web crawler, to be extended for various uses.
"""
import sys
import getopt
import os
import validators
from urllib.parse import urldefrag, urljoin, urlparse

from lib.crawler import Controller
from lib.usage import usage, banner, title, extract


class Program(object):
    def __init__(self):
        self.outputfile = ""
        self.url = ""
        self.domain = True
        self.threads = 10
        self.header = {}
        self.maxpages = 500
        self.robots = False
        self.timeout = 0

    def main(self, argv):
        try:
            opts, args = getopt.getopt(argv,"hu:o:t:dm:T:H:R",["help","url=","outputfile=","threads=","domains","maxpages=","header=","robots","timeout="])
        except getopt.GetoptError as err:
            print(str(err))
            print()
            usage()
        for o,a in opts:
            if o in ("-h","--help"):
                usage()
            elif o in ("-o","--outputfile"):
                self.outputfile = a       
            elif o in ("-d","--domains"):
                self.singledomain = False
            elif o in ("-m","--maxpages"):
                if int(a) < 0 :
                    print("Maxpages must be equal or greater than 0.")
                    exit(0)
                self.maxpages = int(a)
            elif o in ("-u","--url"):
                if not validators.url(a) and not os.path.isfile(a):
                    print("Please input a valid url or file of urls")
                    exit(0)
                self.url = a
            elif o in ("-t","--threads"):
                if int(a) <= 0:
                    print("Threads must be greater than 0.")
                    exit(0)
                self.threads = int(a)
            elif o in ("-H","--header"):
                self.header, value = a.split(":")
                self.header.update({header.strip() : value.strip()})
            elif o in ("-R","--robots"):
                self.robots = True
            elif o in ("--timeout"):
                self.timeout = a
            else:
                print(o)
                assert False,"Unhandle option"

        # set stdout to support UTF-8
        sys.stdout = open(sys.stdout.fileno(), mode="w", encoding="utf-8", buffering=1)
        banner() 
        controller = Controller(startpage=self.url, maxpages=self.maxpages, singledomain=self.domain, concurancy = self.threads, robots = self.robots, timeout = self.timeout, header = self.header)      
        urls = controller.spider()
    
        if len(self.outputfile) > 0:
            extract(self.outputfile,urls) 