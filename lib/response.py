import bs4
import hashlib
import os, sys
from urllib.parse import urlparse

class Response(object):
    def __init__(self, status, headers, text, body, url):
        self.status = status
        self.headers = headers
        self.text = text
        self.body = body
        self.url = url

    def __str__(self):
        return self.body

    def __int__(self):
        return self.status

    def __len__(self):
        return len(self.body)
        
    def redirect(self):
        headers = dict((key.lower(), value) for key, value in self.headers.items())
        return headers.get("location")

    def soup(self):
        return bs4.BeautifulSoup(self.text, "html.parser")

    def dump(self, destination):
        hash = hashlib.md5((str(self.status) + str(self.headers) + str(self.text) + str(self.body) + str(self.url)).encode('utf-8')).hexdigest()
        parsed_url = urlparse(self.url)
        path = destination + "/" + parsed_url.netloc + "/" + parsed_url.path
        os.makedirs(path, 0o0750, exist_ok = True)
        with open(path + "/" + hash + ".body","w") as f:
            f.write(str(self.body))
        with open(path + "/" + hash + ".headers","w") as f:
            f.write(str(self.headers))

