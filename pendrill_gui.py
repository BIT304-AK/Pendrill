from tkinter import StringVar, Text, filedialog
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter.constants import BOTH, COMMAND, END, W
import requests
import xss
import session_scan as ss


def run_XSS(url):
    forms = xss.get_forms(url)
    js = "<script>alert('test')</script>"   
    numOfForms = f"Number of forms found: {len(forms)}"
    result = "" + numOfForms
    for form in forms:
        formDetails = xss.get_form_details(form)
        content = xss.form_submission(formDetails, url, js).content.decode('utf-8')
        if js in content:
            result += "\nXSS vulnerability detected"
        else:
            result += "\nXSS vulnerability not detected"

        return result

def clearTextInput(result):
    result.delete("1.0","end")


#https://xss-game.appspot.com/level1/frame
def XSS_function(pen, result, urlEntry):
    clearTextInput(result)
    print(urlEntry)
    ex = run_XSS(urlEntry)
    result.insert(END, ex)
    pen.savetoAllAttacks(urlEntry, "XSS", ex)
    print(ex)



def xss_gui(pen, root, urlEntry):
    # root = tk.Tk()
    # root.geometry("800x600")

    tab_main = ttk.Notebook(root)
    urlEntry = urlEntry

    result = tk.Text(tab_main, height=10, width=80)
    xssButton = tk.Button(tab_main, text="XSS", command=lambda:XSS_function(pen, result, urlEntry.get()))
    tab_main.pack(expand=1, fill="both")
    xssButton.grid(row=1, column=0)
    result.grid(row=0, column=0, pady=30)
    
