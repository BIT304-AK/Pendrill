import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin


def retrieveForms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")


def get_form_details(form):

    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()

    inputs = []
    for tag in form.find_all("input"):
        inputType = tag.attrs.get("type", "text")
        inputName = tag.attrs.get("name")
        inputs.append({"type": inputType, "name": inputName})

    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


def submitForm(form_details, url, value):

    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:

        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        inputName = input.get("name")
        inputValue = input.get("value")
        if inputName and inputValue:

            data[inputName] = inputValue

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)


def findXSS(url):
    forms = retrieveForms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    script = "<Script>alert('hi')</scripT>"

    is_vulnerable = False

    for form in forms:
        details = get_form_details(form)
        content = submitForm(details, url, script).content.decode()
        if script in content:
            print(f"[+]XSS Detected on {url}")
            print(f"[*]Form details:")
            print(details)
            is_vulnerable = True

    return is_vulnerable


if __name__ == "__main__":
    url = ""
    print(findXSS(url))
