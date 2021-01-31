# WebCollector

WebCollector is a Python3 tool that simply crawl a website. But there is differents options that makes it cool.

# Installation & Usage

To use WebCollector, you need to install its dependencies: 

```
cd webcollector
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt
```

To run a simple crawl:

```
python3 webcollector.py -u www.target.com
```

To view different options:
``` 
python3 webcollector.py -h



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


    
Python WebCollector vO.1

    Usage: python3 webcollector.py -u startup-url

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
    -c --cookie=COOKIE                  - Cookies to add in request (example: --cookie 
                                          "isAdmin: yes" --cookie "username: root")                                          
    -R --robots                         - Feed with robots.txt of the domain
    --timeout=SECONDS                   - Number of seconds to wait after a request
    -D --dump=DIRECTORY                 - Download page content and headers of requested pages
    -p --proxy=PROXY                    - Specify a http proxy like -p "http://127.0.0.1:8080"

```


# TODO

- js file crawling


