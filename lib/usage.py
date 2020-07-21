#!/usr/bin/env python3

import sys

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
    -s --subs-collector=destination     - collect and extract a list of all visited 
                                          domains/subdomains, and store them 
                                          in [destination].
    -U --url-collector=destination      - collect and extract a list of all visited 
                                          domains/subdomains, and store them 
                                          in [destination]                                          
    -d --domains                        - not limit crawl links within startpage's 
                                          domain.
    -m --maxpages=number                - give max pages to crawl. Enter 0 for 
                                          infinite :). Default 10
    -t --threads=number                 - give max threads to run in the same time. 
                                          Default 1
    -p --pipeline                       - print only choosen output. 2 
                                          possibilities : "urls" or "domains"
    -H --header=HEADER                  - Header to add in request (example: --header 
                                          "Referer: example.com" --header "User-Agent: IE")
    -T --test                           - Test mode. Will launch 10 requests starting
                                          from www.microsoft.com and with staying at 
                                          this domain
    """
    print(usage)
    sys.exit(0)

def extract(filename,list):
    with open(filename, mode='wt', encoding='utf-8') as f:
        f.write('\n'.join(list))
