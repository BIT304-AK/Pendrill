from tkinter import *
import webbrowser
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin



def openUrl():
    url = url_name.get()
    print("Url entered: " + url)
    webbrowser.open(url,new=web)
    return

def retrieveForms(url):
    url = url_name.get()
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
    url = url_name.get()
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
    url = url_name.get()
    forms = retrieveForms(url)
    print(f"Detected {len(forms)} forms on {url}.")
    script = "<Script>alert('hi')</scripT>"

    is_vulnerable = False

    for form in forms:
        details = get_form_details(form)
        content = submitForm(details, url, script).content.decode()
        if script in content:
            print(f"XSS Detected on {url}")
            print("Form details:")
            print(details)
            is_vulnerable = True

    return is_vulnerable

root = Tk()
root.geometry("1000x800+400+50")
root.title("Pendrill")

url_name = StringVar()
checked_var = IntVar()
web = 1

url_lbl = Label(root, text="Enter URL:", width=10)
url_lbl.grid(row=1, column=0)

url_entry = Entry(root, textvariable = url_name)
url_entry.grid(row=1, column=1, columnspan=5)


search_button = Button(root, text="Search", width=10, command=openUrl)
search_button.grid(row=1, column=6)

xss_option = Checkbutton(root, text="XSS payload", variable=checked_var)
xss_option.grid(row=3, column=0)


payload_btn = Button(root, text="Run")
payload_btn.grid(row=6, column=0)

root.mainloop()