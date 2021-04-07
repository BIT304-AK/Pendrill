from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import requests


def get_forms(url):
    page = bs(requests.get(url).content, 'html.parser')
    return page.find_all('form')

def get_form_details(form):

    formDetails = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for tags in form.find_all("input"):
        inputTypes = tags.attrs.get("type", "text")
        inputNames = tags.attrs.get("name")
        inputs.append({"type": inputTypes, "name": inputNames})

    formDetails["action"] = action
    formDetails["method"] = method
    formDetails["inputs"] = inputs
    return formDetails

def form_submission(formDetails, url, js):

    fullUrl = urljoin(url, formDetails["action"])
    inputs = formDetails["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = js
        name = input.get("name")
        js = input.get("value")
        if name and js:
            data[name] = js

    if formDetails["method"] == "post":
        return requests.post(fullUrl, data=data)
    else:
        return requests.get(fullUrl, params=data)

def run_XSS(url):

    forms = get_forms(url)
    js = "<script>alert('test')</script>"
    result = ""
    print(f"Number of forms found: {len(forms)}")
    for form in forms:
        formDetails = get_form_details(form)
        content = form_submission(formDetails, url, js).content.decode('utf-8')
        if js in content:
            result = "XSS vulnerability detected"
            return result


if __name__ == "__main__":
    url = "https://xss-game.appspot.com/level1/frame"
    print(run_XSS(url))