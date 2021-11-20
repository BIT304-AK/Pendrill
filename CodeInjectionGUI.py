"""GUI for code injections."""
import tkinter
import itertools
from tkinter import Checkbutton, Frame, IntVar, Scrollbar
from tkinter import ttk
from tkinter import StringVar
# from tkinter import OptionMenu
from tkinter import messagebox
from tkinter.constants import END
from tkscrolledframe import ScrolledFrame
# import PanedWindow
from Pendrill import Pendrill


class CodeInGUI:
    """GUI class."""

    # pen = Pendrill("temp")

    def __init__(self, pen, top, urlEntry):
        """GUI design."""
        self.pen = pen
        self.top = top

        notebook = ttk.Notebook(top)
        notebook.pack(pady=10, expand=True)

        f2 = ttk.Frame(notebook)
        f2.pack(fill='both', expand=True)
        notebook.add(f2, text='Attack List')
        self.sf = ScrolledFrame(notebook)
        self.sf.pack(fill='both', expand=True)
        notebook.add(self.sf, text='Make Attack')
        self.f3 = self.sf.display_widget(ttk.Frame)
        self.f3.columnconfigure(0, weight=1)
        self.f3.columnconfigure(1, weight=1)
        
        self.urlEntry = urlEntry
        # Code to add widgets will go here...
        
        # Table
        self.attackTable = ttk.Treeview(f2, columns=('Attack No.', 'URL',
                                        'Code', 'Data','Cookies', 'Query', 'Contains'),
                                        show='headings')
        self.attackTable.grid(column=0,row=0)
        self.attackTable.heading('Attack No.', text='Attack No.')
        self.attackTable.heading('URL', text='URL')
        self.attackTable.heading('Code', text='Code')
        self.attackTable.heading('Data', text='Data')
        self.attackTable.heading('Cookies', text='Cookies')
        self.attackTable.heading('Query', text='Query')
        self.attackTable.heading('Contains', text='Contains')
        self.attackTable.column('Attack No.', width=60)
        self.attackTable.column('URL', width=400)
        self.attackTable.column('Data', width=350)
        self.attackTable.column('Cookies', width=350)
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
        
        containsLabel = tkinter.Label(labelFrame, text="Contains: ")
        containsLabel.grid(row=0, column=0)
        self.bfContainsEntry = ttk.Entry(labelFrame, textvariable='contains')
        self.bfContainsEntry.grid(row=0, column=1, padx=5, pady=5)

        self.allowRedirectVar = IntVar(labelFrame, value=1)
        self.allowRedirectCheck = Checkbutton(labelFrame, text="Block Redirects", variable=self.allowRedirectVar, onvalue=0, offvalue=1)
        self.allowRedirectCheck.grid(row=1,column=0)

        self.stopBfVar = IntVar(labelFrame, value=0)
        self.stopBfCheck = Checkbutton(labelFrame, text="Stop Brute Force when query in response", variable=self.stopBfVar, onvalue=1, offvalue=0)
        self.stopBfCheck.grid(row=1,column=1)

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

        self.bfSubmitBtn = tkinter.Button(labelFrame, text="Get Form Entries",
                                          command=lambda: self.submitReqBF())
        self.bfSubmitBtn.grid(row=7, column=2)
        self.bfBtn = tkinter.Button(labelFrame, text="Attack",
                                    command=lambda: self.bruteForceData())
        self.bfBtn.grid(row=7, column=3)

        # Cookie section
        self.cookieSection = ttk.LabelFrame(self.f3, text="Cookies", name="cookieLabelFrame")
        self.cookieSection.grid(row=1, column=1)
        
        # Add Cookie
        cookieNameLabel = tkinter.Label(self.cookieSection, text="Name: ")
        cookieNameLabel.grid(row=1, column=0)
        self.cookieNameEntry = ttk.Entry(self.cookieSection, textvariable='cookieName')
        self.cookieNameEntry.grid(row=1, column=1, padx=5, pady=5)

        self.cookieEntryRow = 5
        self.cookieIntvars = {}
        self.formIntvars = {}
        self.cookies = []
        self.cookieAddBtn = tkinter.Button(self.cookieSection, text="Add",
                                          command=lambda: self.addCookie())
        self.cookieAddBtn.grid(row=3, column=0)
        self.bindScroll(self.sf, self.f3)

    def bindScroll(self, sf, parent):
        for child in parent.winfo_children():
            self.bindScroll(sf, child)
            sf.bind_scroll_wheel(child)
            sf.bind_arrow_keys(child)
        sf.bind_scroll_wheel(parent)
        sf.bind_arrow_keys(parent)
    
    def submitReqBF(self):
        """Submit request."""
        allowRedirects = bool(self.allowRedirectVar.get())
        cookies = {}
        cookieData = self.getInputData(self.cookieSection, self.cookies, cookie=True)
        for child in cookieData:
            cookies[child['name']] = child['prefix'] + child['data'] + child['suffix']
        attack = self.pen.singleAtk(self.urlEntry.get(),
                                    username=self.bfAuthUsernameEntry.get(),
                                    password=self.bfAuthPasswordEntry.get(),
                                    allow_redirects=allowRedirects,
                                    cookies=cookies)
        
        
        query = self.bfContainsEntry.get()
        contains = attack.responseContains(query)
        
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
        num = len(self.pen.codeInjList) - 1
        url = attack.url
        try:
            code = attack.response.status_code
        except AttributeError:
            code = attack.response
        data = attack.data
        cookies = attack.cookies
        attackTable.insert("", index="end", values=(str(num), url, code, data, cookies,
                           query, str(contains)))

    def callback(self, sv):
        """Return StringVar."""
        return sv.get()

    def getFormInputsBF(self, attack):
        """Return textbox value."""
        for pos in self.f3.grid_slaves():
            print('pos')
            print(pos, pos.grid_info()['row'], pos.grid_info()['column'])
            if int(pos.grid_info()['row']) == 6:
                for child in pos.grid_slaves():
                    child.destroy()
                pos.destroy()
        inputs = attack.retrieveInputs()
        self.currentAttack = attack
        labelFrame = ttk.LabelFrame(self.f3, text='forms', name='bfLabelFrame')
        labelFrame.grid(row=6, column=0)
        c = 0
        self.formIntvars = {}
        self.bfTable = ttk.Treeview(labelFrame, show='headings')
        n = 0
        for i in inputs:
            n = 0
            self.addEntrySet(labelFrame, i['name'],n,c)
            self.formIntvars['tbf'+i['name']] = self.saveBfChkState
            n = n + 7
            c = c + 2
            self.addColumn(i['name'])
        if(len(inputs) > 0):
            self.saveDictChkState = IntVar(labelFrame)
            self.saveDictCheckbox = ttk.Checkbutton(labelFrame,
                                                    text='Save True Payloads',
                                                    variable=self.saveDictChkState)
            self.saveDictCheckbox.grid(row=n+1, column=1, padx=5, pady=2)
            self.bfTable.grid(row=1, column=c, rowspan=8)
        self.bindScroll(self.sf, labelFrame)

    def bruteForceData(self):
        """Brute force attack."""
        try:
            formDataLF = self.f3.nametowidget('bfLabelFrame')
            inputs = self.currentAttack.retrieveInputs()
            inputData = self.getInputData(formDataLF, inputs)
        except KeyError:
            inputData = []
        
        url = self.urlEntry.get()
        username = self.bfAuthUsernameEntry.get()
        password = self.bfAuthPasswordEntry.get()
        allowRedirects = bool(self.allowRedirectVar.get())
        cookieData = self.getInputData(self.cookieSection, self.cookies, cookie=True)
        
        self.bruteForce(url, inputData, datatype='charset',
                        username=username, password=password, allow_redirects=allowRedirects, cookieData=cookieData)

    # Gets the entered data of list of inputs in a section
    def getInputData(self, location, inputs, cookie=False):
        inputData = []
        for i in inputs:
            x = {}
            if location.nametowidget('min'+i['name']).get().strip() == '':
                x['min'] = 1
            elif location.nametowidget('min'+i['name']).get().isdigit() is False:
                messagebox.showerror("Invalid Data", i['name'] + " min must be number")
                return False
            else:
                x['min'] = int(location.nametowidget('min'+i['name']).get())

            if location.nametowidget('max'+i['name']).get().strip() == '':
                x['max'] = 1
            elif location.nametowidget('max'+i['name']).get().isdigit() is False:
                messagebox.showerror("Invalid Data", i['name'] + " max must be number")
                return False
            else:
                x['max'] = int(location.nametowidget('max'+i['name']).get())
            x['name'] = i['name']
            x['prefix'] = location.nametowidget('prefix'+i['name']).get()
            x['suffix'] = location.nametowidget('suffix'+i['name']).get()
            x['data'] = location.nametowidget('data'+i['name']).get()
            if cookie is False:
                x['bf'] = int(self.formIntvars['tbf'+ i['name'] ].get())
            else:
                x['bf'] = int(self.cookieIntvars['tbf'+ i['name'] ].get())
            inputData.append(x)
        return inputData

    # launches a bruteforce attack
    def bruteForce(self, url, inputData, datatype=None,
                   contains=None, action=None, username=None, password=None, allow_redirects=True, cookieData=None):
        """Brute Force attack."""
        if datatype == 'charset':
            # creates the form data payloads
            formListList = []
            for i in inputData:
                templist = []
                if int(i['bf']) == int(1): #if bf is selected, creates all the possible payloads for entry i
                    for a in range(i['min']-1, i['max']):
                        for d in itertools.product(i['data'], repeat=a+1):
                            x = ""
                            for n in d:
                                x = x + n
                            templist.append(x)
                else:
                    templist.append(i['data']) # if bf not selected, entry added as is
                formListList.append(templist) #adds the list of possible payloads for entry i
            # creates the cookie data payloads
            cookieListList = []
            for i in cookieData:
                templist = []
                if int(i['bf']) == int(1): #if bf is selected, creates all the possible payloads for entry i
                    for a in range(i['min']-1, i['max']):
                        for d in itertools.product(i['data'], repeat=a+1):
                            x = ""
                            for n in d:
                                x = x + n
                            templist.append(x)
                else:
                    templist.append(i['data']) # if bf not selected, entry added as is
                cookieListList.append(templist) #adds the list of possible payloads for entry i
            
            # the attacks
            payload = {}
            cookies = {}
            for i in list(itertools.product(*formListList)): #list contains all possible combinations for the payload
                tempDict = []
                for x in inputData: #adds each data entry to the payload
                    payload[x['name']] = x['prefix'] + i[inputData.index(x)] + x['suffix']
                    tempDict.append(i[inputData.index(x)])
                for c in list(itertools.product(*cookieListList)):
                    for cookie in cookieData:
                        cookies[cookie['name']] = cookie['prefix'] + c[cookieData.index(cookie)] + cookie['suffix']
                    attack = self.pen.singleAtk(url, data=payload, username=username,
                               password=password, cookies=cookies, allow_redirects=allow_redirects)
                    query = self.bfContainsEntry.get()
                    contains = attack.responseContains(query)
                    try:
                        if self.saveDictChkState.get() == 1:
                            if contains is True:
                                self.addToBfTable(tempDict)
                    except AttributeError:
                        pass
                    self.addToTable(attack, query, contains, self.attackTable)
                    self.top.update()
                    if contains is True:
                        if self.stopBfVar.get() == 1:
                            return
    
    # checks to see if an entry set exists 
    def checkEntryExists(self, location, entryName):
        try: 
            location.nametowidget('data'+entryName)
        except KeyError:
            return False
        return True
    
    # adds an entry set
    def addEntrySet(self, location, entryName, startRow, startCol, cookie=False):
        if self.checkEntryExists(location, entryName) == True:
            return
        inputLabel = tkinter.Label(location, text=entryName)
        inputLabel.grid(row=startRow, column=startCol)

        prefixLabel = tkinter.Label(location, text="prefix")
        prefixLabel.grid(row=startRow+1, column=startCol)

        self.prefixEntry = ttk.Entry(location, name='prefix'+entryName)
        self.prefixEntry.grid(row=startRow+1, column=startCol+1, padx=5, pady=5)

        suffixLabel = tkinter.Label(location, text="suffix")
        suffixLabel.grid(row=startRow+2, column=startCol)
        
        self.suffixEntry = ttk.Entry(location, name='suffix'+entryName)
        self.suffixEntry.grid(row=startRow+2, column=startCol+1, padx=5, pady=5)

        inputLabel = tkinter.Label(location, text='charset')
        inputLabel.grid(row=startRow+3, column=startCol)
        self.bfDataEntry = ttk.Entry(location, name='data'+entryName)
        self.bfDataEntry.grid(row=startRow+3, column=startCol+1, padx=5, pady=5)

        inputLabel = tkinter.Label(location, text='Min Data Len')
        inputLabel.grid(row=startRow+4, column=startCol)
        self.minEntry = ttk.Entry(location, name='min'+entryName)
        self.minEntry.grid(row=startRow+4, column=startCol+1, padx=5, pady=2)

        inputLabel = tkinter.Label(location, text='Max Data Len')
        inputLabel.grid(row=startRow+5, column=startCol)
        self.maxEntry = ttk.Entry(location, name='max'+entryName)
        self.maxEntry.grid(row=startRow+5, column=startCol+1, padx=5, pady=2)

        self.saveBfChkState = IntVar(location)
        self.saveBfCheckbox = ttk.Checkbutton(location,
                                                text='Bruteforce',
                                                variable=self.saveBfChkState, name='tbf'+entryName)
        self.saveBfCheckbox.grid(row=startRow+7, column=startCol, padx=5, pady=2)
        if cookie is True:
            deleteCookieBtn = tkinter.Button(location, text="Delete Cookie",name="del"+entryName, 
                                            command=lambda: self.deleteCookie(entryName))
            deleteCookieBtn.grid(row=startRow+7, column=startCol+2)
    
    # deletes a cookie entry set
    def deleteCookie(self, name):
        bfChk = self.cookieSection.nametowidget('tbf' + name)
        endRow = int(bfChk.grid_info()['row'])
        startRow = endRow - 7
        for pos in self.cookieSection.grid_slaves():
            if pos.grid_info()['row'] >= startRow and pos.grid_info()['row'] <= endRow:
                pos.destroy()
        self.cookieIntvars.pop('tbf'+name, None)
        self.cookies.remove({'name':name})
    
    # adds a column to the brute force table
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

    # Adds a cookie entry set
    def addCookie(self):
        name = self.cookieNameEntry.get()
        # value = self.cookieValueEntry.get()
        # self.cookieTable.insert("", index="end", values=(name, value))
        if self.checkEntryExists(self.cookieSection, name) == True:
            messagebox.showinfo("Cookie Entry already exists", "Cookie " + name + " already has entry set")
            return
        self.addEntrySet(self.cookieSection, name,self.cookieEntryRow,0,cookie=True)
        self.cookieIntvars['tbf'+name] = self.saveBfChkState
        self.cookies.append({'name':name})
        self.cookieEntryRow += 8
        self.cookieNameEntry.delete(0,END)
        # self.cookieValueEntry.delete(0,END)
        self.bindScroll(self.sf, self.cookieSection)
    
    def showResponse(self, event):
        """Shows Selected Response"""
        index = self.attackTable.item(self.attackTable.selection())['values'][0]
        attack = self.pen.codeInjList[index]
        response = attack.response.text
        if self.respVar.get() == 2:
            respArea = self.responseArea2
        else:
            respArea = self.responseArea1
        respArea.configure(state='normal')
        respArea.delete(1.0, 'end')
        respArea.insert(1.0, response)
        self.highlight_pattern(respArea, self.attackTable.item(self.attackTable.selection())['values'][5])
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
