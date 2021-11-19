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
import pendrill_gui as pg
import ss_tab as ss
from PendrillAllAttacks import PendrillAllAttacks

class PendrillMainGUI:

    def __init__(self, pen):
        self.pen = pen
        self.top = tkinter.Tk()
        self.top.geometry('1000x600')

        notebook = ttk.Notebook(self.top)
        notebook.pack(pady=10, expand=True)
        self.f1 = ttk.Frame(notebook)
        self.f1.pack(expand=True)
        urlLabel = tkinter.Label(self.f1, text="URL: ")
        urlLabel.grid(row=1, column=0)
        self.urlEntry = ttk.Entry(self.f1, textvariable='url', background="Red")
        self.urlEntry.grid(row=1, column=1, padx=5, pady=5)

        
        notebook2 = ttk.Notebook(self.top)
        notebook2.pack(pady=10, expand=True)
        
        # Frame for Code Injection section
        self.codeInFrame = ttk.Frame(notebook2)
        self.codeInFrame.pack(fill='both', expand=True)
        notebook2.add(self.codeInFrame, text='Code Injections')
        CodeInGUI(pen, self.codeInFrame, self.urlEntry)


        self.xssFrame = ttk.Frame(notebook2)
        self.xssFrame.pack(fill='both', expand=True)
        notebook2.add(self.xssFrame, text='XSS')
        pg.xss_gui(self.xssFrame, self.urlEntry)

        self.ssFrame = ttk.Frame(notebook2)
        self.ssFrame.pack(fill='both', expand=True)
        notebook2.add(self.ssFrame, text='Session scanning')
        ss.ss_gui(self.ssFrame, self.urlEntry)

        # Frame for All attacks section
        self.allAtkFrame = ttk.Frame(notebook2)
        self.allAtkFrame.pack(fill='both', expand=True)
        notebook2.add(self.allAtkFrame, text='All Attacks')
        self.allAtks= PendrillAllAttacks(pen, self.allAtkFrame)
        self.allAtkFrame.bind('<Button-1>', lambda e:self.allAtks.refreshTable())
        self.top.mainloop()