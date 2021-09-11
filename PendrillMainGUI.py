import tkinter
# import itertools
# from tkinter import IntVar
from tkinter import ttk
# from tkinter import StringVar
# # from tkinter import OptionMenu
# from tkinter import messagebox
# # import PanedWindow
# from Pendrill import Pendrill
from CodeInjectionGUI import CodeInGUI

class PendrillMainGUI:

    def __init__(self, pen):
        self.pen = pen
        self.top = tkinter.Tk()
        self.top.geometry('1000x600')

        notebook = ttk.Notebook(self.top)
        notebook.pack(pady=10, expand=True)
        self.f1 = ttk.Frame(notebook)
        self.f1.pack(fill='both', expand=True)
        urlLabel = tkinter.Label(self.f1, text="URL: ")
        urlLabel.grid(row=1, column=0)
        self.urlEntry = ttk.Entry(self.f1, textvariable='url', background="Red")
        self.urlEntry.grid(row=1, column=1, padx=5, pady=5)

        # Frame for Code Injection section
        notebook2 = ttk.Notebook(self.top)
        notebook2.pack(pady=10, expand=True)
        self.codeInFrame = ttk.Frame(notebook2)
        self.codeInFrame.pack(fill='both', expand=True)
        notebook2.add(self.codeInFrame, text='Code Injections')
        CodeInGUI(pen, self.codeInFrame, self.urlEntry)

        self.top.mainloop()