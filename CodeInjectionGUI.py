"""GUI for code injections."""
import tkinter
import itertools
from tkinter import Checkbutton, IntVar
from tkinter import ttk
from tkinter import StringVar
# from tkinter import OptionMenu
from tkinter import messagebox
# import PanedWindow
from Pendrill import Pendrill


class CodeInGUI:
    """GUI class."""

    # pen = Pendrill("temp")

    def __init__(self, pen, top, urlEntry):
        """GUI design."""
        self.pen = pen
        self.top = top
        # top = tkinter.Tk()
        # top.geometry('1000x600')

        # Notebook(tabs).
        notebook = ttk.Notebook(top)
        notebook.pack(pady=10, expand=True)
        # self.f1 = ttk.Frame(notebook)
        # self.f1.pack(fill='both', expand=True)
        # self.f1.columnconfigure(0, weight=1)
        # self.f1.columnconfigure(1, weight=1)
        # notebook.add(self.f1, text='Page 1')

        f2 = ttk.Frame(notebook)
        f2.pack(fill='both', expand=True)
        notebook.add(f2, text='Attack List')

        self.f3 = ttk.Frame(notebook)
        self.f3.pack(fill='both', expand=True)
        self.f3.columnconfigure(0, weight=1)
        self.f3.columnconfigure(1, weight=1)
        notebook.add(self.f3, text='Make Attack')

        self.urlEntry = urlEntry
        # Code to add widgets will go here...
        # Frame 1
        # self.attackTable = ttk.Treeview(f2, columns=('Attack No.', 'URL',
        #                                 'Code', 'Data'), show='headings')
        # title = tkinter.Label(self.f1, text="Code Injection", font="bold")
        # title.grid(row=0, column=0)
        # labelFrame = ttk.LabelFrame(self.f1)
        # labelFrame.grid(row=1, column=0)
        # urlLabel = tkinter.Label(labelFrame, text="URL: ")
        # urlLabel.grid(row=1, column=0)
        # self.urlEntry = ttk.Entry(labelFrame, textvariable='url', background="Red")
        # self.urlEntry.grid(row=1, column=1, padx=5, pady=5)

        # dataLabel = tkinter.Label(labelFrame, text="Data: ")
        # dataLabel.grid(row=2, column=0)
        # self.dataEntry = ttk.Entry(labelFrame, textvariable='data')
        # self.dataEntry.grid(row=2, column=1, padx=5, pady=5)

        # authUsernameLabel = tkinter.Label(labelFrame, text="Username: ")
        # authUsernameLabel.grid(row=3, column=0)
        # self.authUsernameEntry = ttk.Entry(labelFrame, textvariable='authUsername')
        # self.authUsernameEntry.grid(row=3, column=1, padx=5, pady=5)

        # authPasswordLabel = tkinter.Label(labelFrame, text="Password: ")
        # authPasswordLabel.grid(row=4, column=0)
        # self.authPasswordEntry = ttk.Entry(labelFrame, textvariable='authPassword')
        # self.authPasswordEntry.grid(row=4, column=1, padx=5, pady=5)

        # containsLabel = tkinter.Label(labelFrame, text="Contains: ")
        # containsLabel.grid(row=5, column=0)
        # self.containsEntry = ttk.Entry(labelFrame, textvariable='contains')
        # self.containsEntry.grid(row=5, column=1, padx=5, pady=5)

        # self.submitBtn = tkinter.Button(labelFrame, text="Submit",
        #                                 command=lambda: self.submitReq())
        # self.submitBtn.grid(row=6, column=3)
        # Table
        self.attackTable = ttk.Treeview(f2, columns=('Attack No.', 'URL',
                                        'Code', 'Data', 'Query', 'Contains'),
                                        show='headings')
        self.attackTable.grid(column=0,row=0)
        self.attackTable.heading('Attack No.', text='Attack No.')
        self.attackTable.heading('URL', text='URL')
        self.attackTable.heading('Code', text='Code')
        self.attackTable.heading('Data', text='Data')
        self.attackTable.heading('Query', text='Query')
        self.attackTable.heading('Contains', text='Contains')
        self.attackTable.column('Attack No.', width=60)
        self.attackTable.column('URL', width=400)
        self.attackTable.column('Data', width=350)
        self.attackTable.column('Query', width=200)
        self.attackTable.column('Code', width=60)
        self.attackTable.column('Contains', width=100)

        scrollbar = ttk.Scrollbar(f2, orient='vertical', command=self.attackTable.yview)
        scrollbar.grid(column=1,row=0, ipady=90)
        self.attackTable.configure(yscrollcommand=scrollbar.set)
        self.attackTable.bind("<<TreeviewSelect>>", self.showResponse)

        responseLabelFrame = ttk.LabelFrame(f2, text="View Responses")
        responseLabelFrame.grid(column=0,row=1, columnspan=2)
        self.responseArea1 = tkinter.Text(responseLabelFrame, state='disabled')
        self.responseArea1.grid(row=0, column=0)
        self.responseArea2 = tkinter.Text(responseLabelFrame, state='disabled')
        self.responseArea2.grid(row=0, column=1)

        self.respVar = IntVar()
        self.response1rdbtn = tkinter.Radiobutton(responseLabelFrame, variable=self.respVar, value=1, text="Show response here")
        self.response1rdbtn.grid(row=1,column=0)
        self.response2rdbtn = tkinter.Radiobutton(responseLabelFrame, variable=self.respVar, value=2, text="Show response here")
        self.response2rdbtn.grid(row=1,column=1)
        # Frame3
        title = tkinter.Label(self.f3, text="Brute Force", font="bold")
        title.grid(row=0, column=0)
        labelFrame = ttk.LabelFrame(self.f3)
        labelFrame.grid(row=1, column=0)
        # urlLabel = tkinter.Label(labelFrame, text="URL: ")
        # urlLabel.grid(row=1, column=0)
        # self.urlEntry = ttk.Entry(labelFrame, textvariable='url')
        # self.urlEntry.grid(row=1, column=1, padx=5, pady=5)

        containsLabel = tkinter.Label(labelFrame, text="Contains: ")
        containsLabel.grid(row=0, column=0)
        self.bfContainsEntry = ttk.Entry(labelFrame, textvariable='contains')
        self.bfContainsEntry.grid(row=0, column=1, padx=5, pady=5)

        self.allowRedirectVar = IntVar(labelFrame, value=1)
        self.allowRedirectCheck = Checkbutton(labelFrame, text="Block Redirects", variable=self.allowRedirectVar, onvalue=0, offvalue=1)
        self.allowRedirectCheck.grid(row=1,column=0)

        labelFrame2 = ttk.LabelFrame(labelFrame, text="Auth Headers")
        labelFrame2.grid(row=2, column=0,columnspan=2)

        authUsernameLabel = tkinter.Label(labelFrame2, text="Username: ")
        authUsernameLabel.grid(row=1, column=0)
        self.bfAuthUsernameEntry = ttk.Entry(labelFrame2, textvariable='authUsername')
        self.bfAuthUsernameEntry.grid(row=1, column=1, padx=5, pady=5)

        authPasswordLabel = tkinter.Label(labelFrame2, text="Password: ")
        authPasswordLabel.grid(row=2, column=0)
        self.bfAuthPasswordEntry = ttk.Entry(labelFrame2, textvariable='authPassword')
        self.bfAuthPasswordEntry.grid(row=2, column=1, padx=5, pady=5)

        self.bfSubmitBtn = tkinter.Button(labelFrame, text="Submit",
                                          command=lambda: self.submitReqBF())
        self.bfSubmitBtn.grid(row=7, column=3)

        url = "http://natas14.natas.labs.overthewire.org"
        password = "Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1"
        # url = "http://natas15.natas.labs.overthewire.org"
        # password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
        self.urlEntry.insert(0, url)
        self.bfAuthUsernameEntry.insert(0, "natas14")
        self.bfAuthPasswordEntry.insert(0, password)

        # top.mainloop()

    def submitReq(self):
        """Submit request."""
        allowRedirects = bool(self.allowRedirectVar.get())
        print("red", allowRedirects)
        attack = self.pen.singleAtk(self.urlEntry.get(),
                                    data=self.dataEntry.get(),
                                    username=self.authUsernameEntry.get(),
                                    password=self.authPasswordEntry.get(),
                                    allow_redirects=allowRedirects)
        if attack.response == '404':
            messagebox.showerror("404 Error", "Url not resolved")
        else:
            if attack.response.status_code == 401:
                messagebox.showinfo("401 Error", "Authentication headers required!")
            if attack.response.status_code == 405:
                messagebox.showinfo("405 Error", "This method not allowed!")
            query = self.containsEntry.get()
            contains = attack.responseContains(query)
            self.addToTable(attack, query, contains, self.attackTable)
            if attack.response.status_code != 401:
                self.getFormInputs(attack)

    def submitReqBF(self):
        """Submit request."""
        allowRedirects = bool(self.allowRedirectVar.get())
        print("red", allowRedirects)
        attack = self.pen.singleAtk(self.urlEntry.get(),
                                    username=self.bfAuthUsernameEntry.get(),
                                    password=self.bfAuthPasswordEntry.get(),
                                    allow_redirects=allowRedirects)
        
        
        query = self.bfContainsEntry.get()
        contains = attack.responseContains(query)
        
        # print("SubmitReqBF")
        self.addToTable(attack, query, contains, self.attackTable)
        if attack.response == '404':
            messagebox.showerror("404 Error", "Url not resolved")
        elif attack.response.status_code == 401:
            messagebox.showinfo("401 Error", "Correct Authentication headers required!")
        elif attack.response.status_code == 405:
                messagebox.showinfo("405 Error", "This method not allowed!")
        else:
            self.getFormInputsBF(attack)

    def addToTable(self, attack, query, contains, attackTable):
        """Add attack to table."""
        num = len(self.pen.attackList) - 1
        url = attack.url
        try:
            code = attack.response.status_code
        except AttributeError:
            code = attack.response
        data = attack.data
        # print("addToTable before insert")
        attackTable.insert("", index="end", values=(str(num), url, code, data,
                           query, str(contains)))
        # print("addToTable after insert")

    def callback(self, sv):
        """Return StringVar."""
        return sv.get()

    def dataEntrys(self, prefix, text):
        """Affect the data entry."""
        self.inputList[prefix] = text
        self.dataEntry.delete(0, 'end')
        i = 0
        n = 0
        for k, v in self.inputList.items():
            self.dataEntry.insert(i, k + "=" + v)
            if n + 1 != len(self.inputList):
                self.dataEntry.insert('end', "&")
            i = i + len(k + "=" + v + "&")
            n = n + 1

    def getFormInputs(self, attack):
        """Return textbox value."""
        for pos in self.f1.grid_slaves():
            print('pos')
            print(pos, pos.grid_info()['row'], pos.grid_info()['column'])
            if int(pos.grid_info()['row']) == 5:
                for child in pos.grid_slaves():
                    child.destroy()
                pos.destroy()
        inputs = attack.retrieveInputs()
        labelFrame = ttk.LabelFrame(self.f1, text='forms')
        labelFrame.grid(row=5, column=0)
        n = 2
        stringVarList = []
        self.inputList = {}
        for i in inputs:
            inputLabel = tkinter.Label(labelFrame, text=i['name'])
            inputLabel.grid(row=n, column=0)
            sv = StringVar(labelFrame, name=i['name'])
            stringVarList.append(sv)
            sv.trace("w", lambda index, mode, name=i['name'], sv=sv, x=i: self.dataEntrys(x['name'],
            sv.get()))
            inputEntry = ttk.Entry(labelFrame, textvariable=sv)
            self.inputList[i['name']] = ""
            inputEntry.grid(row=n, column=1, padx=5, pady=5)
            n = n + 1

    def getFormInputsBF(self, attack):
        """Return textbox value."""
        for pos in self.f3.grid_slaves():
            print('pos')
            print(pos, pos.grid_info()['row'], pos.grid_info()['column'])
            if int(pos.grid_info()['row']) == 6:
                # print(len(pos.winfo_children()))
                for child in pos.grid_slaves():
                    # pos.forget()
                    child.destroy()
                pos.destroy()
        inputs = attack.retrieveInputs()
        self.currentAttack = attack
        # inputNames = []
        # for i in inputs:
        #     inputNames.append(i['name'])
        labelFrame = ttk.LabelFrame(self.f3, text='forms', name='bfLabelFrame')
        labelFrame.grid(row=6, column=0)
        # dropdown = StringVar()
        # dropdown.set(inputNames[0])
        # dropdownList = OptionMenu(labelFrame, dropdown, *inputNames)
        # dropdownList.grid(row=1, column=0)
        c = 0
        self.intvars = {}
        self.bfTable = ttk.Treeview(labelFrame, show='headings')
        for i in inputs:
            n = 0
            inputLabel = tkinter.Label(labelFrame, text=i['name'])
            inputLabel.grid(row=n, column=c)

            prefixLabel = tkinter.Label(labelFrame, text="prefix")
            prefixLabel.grid(row=n+1, column=c)

            # sv = StringVar()
            # sv.trace("w", lambda name, index, mode)
            self.prefixEntry = ttk.Entry(labelFrame, name=i['name']+'prefix')
            self.prefixEntry.grid(row=n+1, column=c+1, padx=5, pady=5)

            suffixLabel = tkinter.Label(labelFrame, text="suffix")
            suffixLabel.grid(row=n+2, column=c)
            # sv = StringVar()
            # sv.trace("w", lambda name, index, mode, sv=sv: self.dataEntrys(i['name'],
            # inputEntry.get()))
            self.suffixEntry = ttk.Entry(labelFrame, name=i['name']+'suffix')
            self.suffixEntry.grid(row=n+2, column=c+1, padx=5, pady=5)

            inputLabel = tkinter.Label(labelFrame, text='charset')
            inputLabel.grid(row=n+3, column=c)
            self.bfDataEntry = ttk.Entry(labelFrame, name=i['name']+'data')
            self.bfDataEntry.grid(row=n+3, column=c+1, padx=5, pady=5)

            inputLabel = tkinter.Label(labelFrame, text='Min Data Len')
            inputLabel.grid(row=n+4, column=c)
            self.minEntry = ttk.Entry(labelFrame, name=i['name']+'min')
            # self.minEntry.place(width=2)
            self.minEntry.grid(row=n+4, column=c+1, padx=5, pady=2)

            inputLabel = tkinter.Label(labelFrame, text='Max Data Len')
            inputLabel.grid(row=n+5, column=c)
            self.maxEntry = ttk.Entry(labelFrame, name=i['name']+'max')
            # self.maxEntry.place(width=2)
            self.maxEntry.grid(row=n+5, column=c+1, padx=5, pady=2)


            # self.intvars[i['name']+'saveDict'] = self.saveDictChkState
            # self.saveDictCheckbox.deselect()
            # self.dictLabel = tkinter.Label(labelFrame, text='True chars')
            # self.dictLabel.grid(row=n+6, column=c+1)

            self.saveBfChkState = IntVar(labelFrame)
            self.saveBfCheckbox = ttk.Checkbutton(labelFrame,
                                                  text='Bruteforce',
                                                  variable=self.saveBfChkState, name=i['name']+'tbf')
            self.saveBfCheckbox.grid(row=n+7, column=c, padx=5, pady=2)
            self.intvars[i['name']+'tbf'] = self.saveBfChkState
            n = n + 7
            c = c + 2
            self.addColumn(i['name'])
        # labelFrame.grid_rowconfigure(c, weight=8)
        self.saveDictChkState = IntVar(labelFrame)
        self.saveDictCheckbox = ttk.Checkbutton(labelFrame,
                                                text='Save True Payloads',
                                                variable=self.saveDictChkState)
        self.saveDictCheckbox.grid(row=n+1, column=1, padx=5, pady=2)
        self.bfTable.grid(row=1, column=c, rowspan=8)
        self.bfBtn = tkinter.Button(labelFrame, text="Attack",
                                    command=lambda: self.bruteForceData())
        self.bfBtn.grid(row=n+2, column=1)

    def bruteForceData(self):
        """Brute force attack."""
        lf = self.f3.nametowidget('bfLabelFrame')
        inputs = self.currentAttack.retrieveInputs()
        url = self.urlEntry.get()
        username = self.bfAuthUsernameEntry.get()
        password = self.bfAuthPasswordEntry.get()
        allowRedirects = self.allowRedirectVar
        inputData = []
        for i in inputs:
            x = {}
            if lf.nametowidget(i['name']+'min').get().strip() == '':
                x['min'] = 1
            elif lf.nametowidget(i['name']+'min').get().isdigit() is False:
                messagebox.showerror("Invalid Data", i['name'] + " min must be number")
                return False
            else:
                x['min'] = int(lf.nametowidget(i['name']+'min').get())

            if lf.nametowidget(i['name']+'max').get().strip() == '':
                x['max'] = 1
            elif lf.nametowidget(i['name']+'max').get().isdigit() is False:
                messagebox.showerror("Invalid Data", i['name'] + " max must be number")
                return False
            else:
                x['max'] = int(lf.nametowidget(i['name']+'max').get())
            x['name'] = i['name']
            x['prefix'] = lf.nametowidget(i['name']+'prefix').get()
            x['suffix'] = lf.nametowidget(i['name']+'suffix').get()
            x['data'] = lf.nametowidget(i['name']+'data').get()
            x['bf'] = int(self.intvars[i['name'] + 'tbf'].get())
            inputData.append(x)
        self.bruteForce(url, inputData, datatype='charset',
                        username=username, password=password, allow_redirects=allowRedirects)

    def bruteForce(self, url, inputData, min=1, length=1, datatype=None,
                   contains=None, action=None, username=None, password=None, allow_redirects=True):
        """Brute Force attack."""
        if datatype == 'charset':
            i = 1
            listList = []
            for i in inputData:
                templist = []
                if int(i['bf']) == int(1):
                    for a in range(i['min']-1, i['max']):
                        for d in itertools.product(i['data'], repeat=a+1):
                            x = ""
                            for n in d:
                                x = x + n
                            templist.append(x)
                else:
                    templist.append(i['data'])
                listList.append(templist)
            payload = {}
            for i in list(itertools.product(*listList)):
                tempDict = []
                for x in inputData:
                    payload[x['name']] = x['prefix'] + i[inputData.index(x)] + x['suffix']
                    tempDict.append(i[inputData.index(x)])
                attack = self.pen.createAttack(url, payload)
                attack.postReq(data=payload, username=username,
                               password=password)
                query = self.bfContainsEntry.get()
                contains = attack.responseContains(query)
                if self.saveDictChkState.get() == 1:
                    if contains is True:
                        self.addToBfTable(tempDict)
                self.pen.saveAttack(attack)
                self.addToTable(attack, query, contains, self.attackTable)
                self.top.update()

    def addColumn(self, newCol):
        """Add a col."""
        currentCols = list(self.bfTable['columns'])
        # print(currentCols)
        currentCols.append(newCol)
        currentCols = tuple(currentCols)
        print(currentCols)
        self.bfTable['columns'] = currentCols
        # for key in newCol:
        self.bfTable.heading(newCol, text=newCol)
        i = 0
        for key in currentCols:
            # state = currentCols[i].pop('state')
            self.bfTable.heading(key, text=key)
            i = i + 1

    def addToBfTable(self, data):
        """Add to Brute Force Table."""
        tempList = []
        for val in data:
            tempList.append(val)
        val = tuple(tempList)
        self.bfTable.insert("", index="end", values=val)

    def showResponse(self, event):
        """Shows Selected Response"""
        index = self.attackTable.item(self.attackTable.selection())['values'][0]
        attack = self.pen.attackList[index]
        response = attack.response.text
        if self.respVar.get() == 2:
            respArea = self.responseArea2
        else:
            respArea = self.responseArea1
        respArea.configure(state='normal')
        respArea.delete(1.0, 'end')
        respArea.insert(1.0, response)
        self.highlight_pattern(respArea, self.attackTable.item(self.attackTable.selection())['values'][4])
        respArea.configure(state='disabled')
    
    def highlight_pattern(self, text, pattern, start="1.0", end="end",
                          regexp=False):
        '''Apply the given tag to all text that matches the given pattern

        If 'regexp' is set to True, pattern will be treated as a regular
        expression according to Tcl's regular expression syntax.
        '''

        start = text.index(start)
        end = text.index(end)
        text.mark_set("matchStart", start)
        text.mark_set("matchEnd", start)
        text.mark_set("searchLimit", end)

        count = IntVar()
        while True:
            index = text.search(pattern, "matchEnd","searchLimit",
                                count=count, regexp=regexp)
            if index == "": break
            if count.get() == 0: break # degenerate pattern which matches zero-length strings
            text.mark_set("matchStart", index)
            text.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            text.tag_add("start", "matchStart", "matchEnd")
            text.tag_config("start", background= "black", foreground= "white")
