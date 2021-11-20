from tkinter import IntVar, ttk
import tkinter


class PendrillAllAttacks:

    def __init__(self, pen, top):
        self.pen = pen
        self.top = top

        self.createTable()

        responseLabelFrame = ttk.LabelFrame(self.top, text="View Responses")
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

    def refreshTable(self):
        self.allAtkTable.destroy()
        self.createTable()

    def showResponse(self, event):
        """Shows Selected Response"""
        index = self.allAtkTable.item(self.allAtkTable.selection())['values'][0] - 1
        attack = self.pen.allAttacks[index]
        response = attack['response']
        if self.respVar.get() == 2:
            respArea = self.responseArea2
        else:
            respArea = self.responseArea1
        respArea.configure(state='normal')
        respArea.delete(1.0, 'end')
        respArea.insert(1.0, response)
        respArea.configure(state='disabled')
    
    def createTable(self):
        self.allAtkTable = ttk.Treeview(self.top, columns=('Attack No.', 'URL',
                                        'Type'),
                                        show='headings')
        self.allAtkTable.grid(column=0,row=0)
        self.allAtkTable.heading('Attack No.', text='Attack No.')
        self.allAtkTable.heading('URL', text='URL')
        self.allAtkTable.heading('Type', text='Type')
        
        self.allAtkTable.column('Attack No.', width=60)
        self.allAtkTable.column('URL', width=400)
        self.allAtkTable.column('Type', width=350)

        scrollbar = ttk.Scrollbar(self.top, orient='vertical', command=self.allAtkTable.yview)
        scrollbar.grid(column=1,row=0, ipady=90)
        self.allAtkTable.configure(yscrollcommand=scrollbar.set)
        self.allAtkTable.bind("<<TreeviewSelect>>", self.showResponse)
        i = 0
        for attack in self.pen.allAttacks:
            i+=1
            self.allAtkTable.insert("", index="end", values=(str(i), attack['url'], attack['type']))