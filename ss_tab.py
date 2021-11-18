from tkinter.constants import END
import session_scan as ss
from tkinter import ttk
import tkinter as tk

def session_scan(result, urlEntry):
    url = ss.ScanHeaders(urlEntry)
    text = "" 
    text = url.scan_xxss()

    result.insert(END, text)


def ss_gui(root, urlEntry):
    tab_main = ttk.Notebook(root)

    urlEntry = urlEntry

    result = tk.Text(tab_main, height=10, width=50)
    scanPage = tk.Button(tab_main, text="XSS", command=lambda:session_scan(result, urlEntry.get()))
    scanPage.grid(column=0, row=0)
    result.grid(row=1, column=1, pady=30)
    tab_main.pack(expand=1, fill='both')