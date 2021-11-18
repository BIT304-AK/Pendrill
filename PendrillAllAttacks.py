from tkinter import ttk


class PendrillAllAttacks:

    def __init__(self, pen, top):
        self.pen = pen
        self.top = top

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
        i = 0
        for attack in self.pen.allAttacks:
            i+=1
            self.allAtkTable.insert("", index="end", values=(str(i), attack['url'], attack['type']))

    def refreshTable(self):
        self.allAtkTable.destroy()
        PendrillAllAttacks(self.pen, self.top)