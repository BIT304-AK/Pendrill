"""sql injection functions here."""
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup


class Sql:
    """Place Sql injection functions here."""

    def __init__(self, url, data=None, cookies=None):
        """Construct Class."""
        self.url = url
        self.data = data
        self.response = " "
        self.objects = []
        self.cookies = cookies
    
    # This function is unused
    def getReq(self, data=None, json=None, files=None, allow_redirects=True,
               username=None, password=None, cert=None, cookies=None,
               headers=None, proxies=None, stream=False, timeout=None,
               verify=True):
        """Get get response from webpage."""
        r = requests.get(self.url, data=data, json=json, files=files,
                         allow_redirects=allow_redirects,
                         auth=(username, password), cert=cert, cookies=cookies,
                         headers=headers, proxies=proxies, stream=stream,
                         timeout=timeout, verify=verify)
        self.saveResponse(r)

    def postReq(self, data=None, json=None, files=None, allow_redirects=True,
                username=None, password=None, cert=None, cookies=None,
                headers=None, proxies=None, stream=False, timeout=None,
                verify=True):
        """Get post response from webpage."""
        try:
            r = requests.post(self.url, data=data, json=json, files=files,
                              allow_redirects=allow_redirects,
                              auth=(username, password), cert=cert,
                              cookies=cookies, headers=headers, proxies=proxies,
                              stream=stream, timeout=timeout, verify=verify)
        except ConnectionError:
            self.response = '404'
            return '404'
        self.saveResponse(r)
        self.cookies = cookies
        
    def parsePage(self):
        """Parse page elements into obejcts."""
        self.objects = BeautifulSoup(self.response.text, 'html.parser')

    def saveResponse(self, r):
        """Save response into object attributes."""
        self.response = r
        self.parsePage()

    def responseContains(self, content):
        """Check to see if the response contains the entered text."""
        try:
            if content in self.response.text:
                return True
            else:
                return False
        except AttributeError:
            return False

    def retrieveInputs(self):
        """Retrieve input locations."""
        inputs = self.objects.find_all('input')
        inputList = []
        for i in inputs:
            if i.get('type') != 'submit':
                inputList.append(i)
        return inputList
