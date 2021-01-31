from lib.response import Response
import requests

class Requester(object):
    def __init__(self, url, session, cookies = None, timeout=None, proxy=None, headers=None):
        self.url = url
        self.session = session
        self.timeout = timeout
        self.proxy = proxy
        self.headers = headers
        self.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0"
        self.cookies = cookies

    def request(self):
        try:
            requests.packages.urllib3.disable_warnings()
            response = self.session.get(self.url, headers = self.headers, proxies = self.proxy, allow_redirects = False, verify = False, cookies = self.cookies)
        except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema):
        # if something wrong in schema
            print("*Wrong schema*:", self.url)
                
            return None
        except (requests.exceptions.ConnectionError):
            print("*Connection refused*:", self.url)
                
            return None

        result = Response(
            response.status_code,
            response.headers,
            response.text,
            response.content,
            self.url
        )
        return result
