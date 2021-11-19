from tkinter.constants import END
import session_scan as ss
from session_scan import ScanHeaders
from tkinter import ttk
import tkinter as tk

def session_scan(pen, result, urlEntry):
    clearTextInput(result)
    ss = ScanHeaders(urlEntry)
    text = ""
    text = ss.doAll()
    print(text)
    result.insert(END, text)
    pen.savetoAllAttacks(urlEntry, "Session scanning")

def clearTextInput(result):
    result.delete("1.0","end")


def ss_gui(pen, root, urlEntry):
    tab_main = ttk.Notebook(root)

    urlEntry = urlEntry

    result = tk.Text(tab_main, height=10, width=50)
    scanPage = tk.Button(tab_main, text="Scan webpage", command=lambda:session_scan(pen, result, urlEntry.get()))
    scanPage.grid(column=0, row=0)
    result.grid(row=1, column=1, pady=30)
    tab_main.pack(expand=1, fill='both')