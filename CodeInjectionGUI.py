"""GUI for code injections."""
import tkinter
from tkinter import ttk
from tkinter import StringVar
# import PanedWindow
from Pendrill import Pendrill


class CodeInGUI:
    """GUI class."""

    # pen = Pendrill("temp")

    def __init__(self, pen):
        """GUI design."""
        self.pen = pen
        top = tkinter.Tk()
        top.geometry('800x600')

        # Notebook(tabs).
        notebook = ttk.Notebook(top)
        notebook.pack(pady=10, expand=True)
        self.f1 = ttk.Frame(notebook)
        self.f1.pack(fill='both', expand=True)
        self.f1.columnconfigure(0, weight=1)
        self.f1.columnconfigure(1, weight=3)
        notebook.add(self.f1, text='Page 1')
        f2 = ttk.Frame(notebook)
        f2.pack(fill='both', expand=True)
        notebook.add(f2, text='Page 2')

        # Code to add widgets will go here...
        # Frame 1
        self.attackTable = ttk.Treeview(f2, columns=('Attack No.', 'URL',
                                        'Code', 'Data'), show='headings')
        title = tkinter.Label(self.f1, text="Code Injection", font="bold")
        title.grid(row=0, column=0)
        urlLabel = tkinter.Label(self.f1, text="URL: ")
        urlLabel.grid(row=1, column=0)
        self.urlEntry = ttk.Entry(self.f1, textvariable='url')
        self.urlEntry.grid(row=1, column=1, padx=5, pady=5)

        dataLabel = tkinter.Label(self.f1, text="Data: ")
        dataLabel.grid(row=2, column=0)
        self.dataEntry = ttk.Entry(self.f1, textvariable='data')
        self.dataEntry.grid(row=2, column=1, padx=5, pady=5)

        authUsernameLabel = tkinter.Label(self.f1, text="Username: ")
        authUsernameLabel.grid(row=3, column=0)
        self.authUsernameEntry = ttk.Entry(self.f1, textvariable='authUsername')
        self.authUsernameEntry.grid(row=3, column=1, padx=5, pady=5)

        authPasswordLabel = tkinter.Label(self.f1, text="Password: ")
        authPasswordLabel.grid(row=4, column=0)
        self.authPasswordEntry = ttk.Entry(self.f1, textvariable='authPassword')
        self.authPasswordEntry.grid(row=4, column=1, padx=5, pady=5)

        self.submitBtn = tkinter.Button(self.f1, text="Submit",
                                        command=lambda: self.submitReq())
        self.submitBtn.grid(row=6, column=3)
        # Frame2
        # attackTable = ttk.Treeview(f2, columns=('Attack No.', 'URL', 'Code'),
        #                            show='headings')
        self.attackTable.pack()
        self.attackTable.heading('Attack No.', text='Attack No.')
        self.attackTable.heading('URL', text='URL')
        self.attackTable.heading('Code', text='Code')
        self.attackTable.heading('Data', text='Data')

        url = "http://natas15.natas.labs.overthewire.org"
        password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
        self.urlEntry.insert(0, url)
        self.authUsernameEntry.insert(0, "natas15")
        self.authPasswordEntry.insert(0, password)

        top.mainloop()

    def submitReq(self):
        """Submit request."""
        attack = self.pen.singleAtk(self.urlEntry.get(),
                                    data=self.dataEntry.get(),
                                    username=self.authUsernameEntry.get(),
                                    password=self.authPasswordEntry.get())
        self.addToTable(attack, self.attackTable)
        self.getFormInputs(attack)

    def addToTable(self, attack, attackTable):
        """Add attack to table."""
        num = len(self.pen.attackList) - 1
        url = attack.url
        code = attack.response.status_code
        data = attack.data
        attackTable.insert("", index="end", values=(str(num), url, code, data))

    def callback(self, sv):
        """Return StringVar."""
        return sv.get()

    def dataEntrys(self, prefix, text):
        """Affect the data entry."""
        self.dataEntry.delete(0, 'end')
        self.dataEntry.insert(0, prefix + "=" + text)

    def getFormInputs(self, attack):
        """Return textbox value."""
        inputs = attack.retrieveInputs()
        labelFrame = ttk.LabelFrame(self.f1, text='forms')
        labelFrame.grid(row=5, column=0)

        for i in inputs:
            n = 1
            inputLabel = tkinter.Label(labelFrame, text=i['name'])
            inputLabel.grid(row=n, column=0)
            sv = StringVar()
            sv.trace("w", lambda name, index, mode, sv=sv: self.dataEntrys(i['name'],
            inputEntry.get()))
            inputEntry = ttk.Entry(labelFrame, textvariable=sv)
            inputEntry.grid(row=n, column=1, padx=5, pady=5)
            n = n + 1
