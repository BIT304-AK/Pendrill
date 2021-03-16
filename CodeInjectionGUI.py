"""GUI for code injections."""
import tkinter
from tkinter import ttk
# import PanedWindow
from Pendrill import Pendrill

pen = Pendrill("temp")


def main():
    """GUI design."""
    top = tkinter.Tk()
    top.geometry('300x200')

    # Notebook(tabs).
    notebook = ttk.Notebook(top)
    notebook.pack(pady=10, expand=True)
    f1 = ttk.Frame(notebook)
    f1.pack(fill='both', expand=True)
    f1.columnconfigure(0, weight=1)
    f1.columnconfigure(1, weight=3)
    notebook.add(f1, text='Page 1')
    f2 = ttk.Frame(notebook)
    f2.pack(fill='both', expand=True)
    notebook.add(f2, text='Page 2')

    # Code to add widgets will go here...
    # Frame 1
    title = tkinter.Label(f1, text="Code Injection", font="bold")
    title.grid(row=0, column=0)
    urlLabel = tkinter.Label(f1, text="URL: ")
    urlLabel.grid(row=1, column=0)
    urlEntry = ttk.Entry(f1, textvariable='url')
    urlEntry.grid(row=1, column=1, padx=5, pady=5)
    submitBtn = tkinter.Button(f1, text="Submit")
    submitBtn.grid(row=2, column=3)
    top.mainloop()


main()


def submitReq(url, data):
    """Submit request."""
    pen.singleAtk()
