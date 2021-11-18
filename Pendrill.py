"""Main class."""
from SQLinjections import Sql
import string


class Pendrill:
    """Pendrill Class."""

    def __init__(self, name):
        """Initialize class."""
        self.name = name
        self.allAttacks = []
        self.codeInjList = []

    def singleAtk(self, url, data=None, json=None, files=None,
                  allow_redirects=True, username=None, password=None,
                  cert=None, cookies=None, headers=None, proxies=None,
                  stream=False, timeout=None, verify=True):
        """Attack a website with code injection."""
        attack = Sql(url, data)
        attack.postReq(data, json, files, allow_redirects, username,
                       password, cert, cookies, headers, proxies, stream,
                       timeout, verify)
        if attack == '404':
            return attack
        else:
            self.saveAttack(attack, type="Code Injection")
            return attack

    def bruteForce(self, url, prefix, sufix, data, length=None, datatype=None,
                   contains=None, action=None, username=None, password=None, allow_redirects=True):
        """Brute Force attack."""
        if datatype == 'numbers':
            # print("Atk No", "Code", "data")
            for i in range(length):
                data = i
                attack = self.createAttack(url, data)
                payload = {'username': prefix+str(data)+sufix}
                attack.postReq(data=payload, username=username,
                               password=password, allow_redirects=allow_redirects)
                # print(i, attack.response, data)
                self.saveAttack(attack, type="Code Injection")

        if datatype == 'charset':
            i = 1
            # print("Atk No", "Code", "data", "Contains " + contains)
            if action == "Discover Contained Chars":
                savedDict = []
            for char in data:
                payload = {'username': prefix+str(char)+sufix}
                attack = self.createAttack(url, payload)
                attack.postReq(data=payload, username=username,
                               password=password)
                # print(i, attack.response, char,
                #       attack.responseContains(contains))
                i = i + 1
                if self.searchInResponse(attack, contains) is True:
                    if action == "Discover Contained Chars":
                        savedDict.append(char)
                self.saveAttack(attack, type="Code Injection")
                return savedDict
            # print("Dictionary: {0}".format(''.join(savedDict)))

    def createAttack(self, url, data):
        """Save attack."""
        return Sql(url, data)

    def saveAttack(self, attack, type=""):
        """Save attack to list."""
        self.codeInjList.append(attack)
        self.allAttacks.append({"url": attack.url, "type": type})

    def showAttacks(self, contains=""):
        """Show attacks."""
        attackString = ""
        for attack in self.codeInjList:
            search = self.searchInResponse(attack, contains)
            attackString += attack.url + " " + str(attack.response.status_code) \
                + " " + str(attack.data) + " " + str(search)
        return attackString

    def searchInResponse(self, attack, contains=""):
        """Find stated content in response."""
        return attack.responseContains(contains)
