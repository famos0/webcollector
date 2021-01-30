import bs4

class Response(object):
    def __init__(self, status, headers, text, body):
        self.status = status
        self.headers = headers
        self.text = text
        self.body = body

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