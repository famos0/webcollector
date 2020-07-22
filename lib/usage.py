#!/usr/bin/env python3

import sys
import lib.settings as settings

def title(title):
    print()
    print("##################################################################")
    print()
    print(title.upper())
    print()
    print("##################################################################")
    print()

def banner():
    print("""


     █     █░▓█████  ▄▄▄▄       ▄████▄   ▒█████   ██▓     ██▓    ▓█████  ▄████▄  ▄▄▄█████▓ ▒█████   ██▀███  
    ▓█░ █ ░█░▓█   ▀ ▓█████▄    ▒██▀ ▀█  ▒██▒  ██▒▓██▒    ▓██▒    ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
    ▒█░ █ ░█ ▒███   ▒██▒ ▄██   ▒▓█    ▄ ▒██░  ██▒▒██░    ▒██░    ▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
    ░█░ █ ░█ ▒▓█  ▄ ▒██░█▀     ▒▓▓▄ ▄██▒▒██   ██░▒██░    ▒██░    ▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
    ░░██▒██▓ ░▒████▒░▓█  ▀█▓   ▒ ▓███▀ ░░ ████▓▒░░██████▒░██████▒░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
    ░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒   ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▒░▓  ░░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
    ▒ ░ ░   ░ ░  ░▒░▒   ░      ░  ▒     ░ ▒ ▒░ ░ ░ ▒  ░░ ░ ▒  ░ ░ ░  ░  ░  ▒       ░      ░ ▒ ▒░   ░▒ ░ ▒░
    ░   ░     ░    ░    ░    ░        ░ ░ ░ ▒    ░ ░     ░ ░      ░   ░          ░      ░ ░ ░ ▒    ░░   ░ 
        ░       ░  ░ ░         ░ ░          ░ ░      ░  ░    ░  ░   ░  ░░ ░                   ░ ░     ░     
                        ░    ░                                        ░                                   


    """)

def usage():
    banner()
    usage = """Python Webcollector vO.O.1

    Usage: webcollector -u startup-url

    -u --url=startup-url                - url where to start crawling.
    -s --subs-collector=DESTINATION     - collect and extract a list of all visited 
                                          domains/subdomains, and store them 
                                          in [destination].
    -U --url-collector=DESTINATION      - collect and extract a list of all visited 
                                          domains/subdomains, and store them 
                                          in [destination]                                          
    -d --domains                        - not limit crawl links within startpage's 
                                          domain.
    -m --maxpages=NUMBER                - give max pages to crawl. Enter 0 for 
                                          infinite :). Default 10
    -t --threads=NUMBER                 - give max threads to run in the same time. 
                                          Default 1
    -p --pipeline                       - print only choosen output. 2 
                                          possibilities : "urls" or "domains"
    -H --header=HEADER                  - Header to add in request (example: --header 
                                          "Referer: example.com" --header "User-Agent: IE")
    -T --test                           - Test mode. Will launch 10 requests starting
                                          from www.microsoft.com and with staying at 
                                          this domain
    -R --robots                         - Feed the spider with robots.txt of the domain
    --timeout=SECONDS                   - Number of seconds to wait after a request
    """
    print(usage)
    sys.exit(0)

def extract(filename,list):
    with open(filename, mode='wt', encoding='utf-8') as f:
        f.write('\n'.join(list))

def options():
    print("Staying on domain: "+("Yes" if settings.domain else "No"))
    print("Maximum pages crawled: "+str(settings.maxpages))
    print("Number of thread(s): "+str(settings.threads))
    print("Header: "+str(settings.header))
    print("Feeding with robots.txt: "+("Yes" if settings.robots else "No"))
