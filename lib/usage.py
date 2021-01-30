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
    
    -o --url-collector=DESTINATION      - collect and extract a list of all visited 
                                          domains/subdomains, and store them 
                                          in [destination]                                          
    -d --domains                        - not limit crawl links within startpage's 
                                          domain.
    -m --maxpages=NUMBER                - give max pages to crawl. Enter 0 for 
                                          infinite :). Default 500
    -t --threads=NUMBER                 - give max threads to run in the same time. 
                                          Default 10
    -H --header=HEADER                  - Header to add in request (example: --header 
                                          "Referer: example.com" --header "User-Agent: IE")
    -R --robots                         - Feed with robots.txt of the domain
    --timeout=SECONDS                   - Number of seconds to wait after a request
    """
    print(usage)
    sys.exit(0)

def extract(filename,list):
    with open(filename, mode='wt', encoding='utf-8') as f:
        f.write('\n'.join(list))