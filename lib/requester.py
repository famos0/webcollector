from lib.response import Response
import requests

class Requester(object):
    def __init__(self, url, session, timeout=None, proxy=None, headers=None):
        self.url = url
        self.session = session
        self.timeout = timeout
        self.proxy = proxy
        self.headers = headers

    def request(self):
        try:
            response = self.session.get(self.url, headers = self.headers)
        except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema):
        # if something wrong in schema
            print("*Wrong schema*:", self.url)
                
            return None
        except (requests.exceptions.ConnectionError):
            print("*Connection refused*:", self.url)
                
            return None
        try:
            if not response.headers["content-type"].startswith("text/html"):
                return None # don't crawl non-HTML content
        except:
            return None

        result = Response(
            response.status_code,
            response.headers,
            response.text,
            response.content
        )
        return result
