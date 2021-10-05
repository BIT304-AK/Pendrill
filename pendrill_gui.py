from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import xss

def run_function():
    url = url_entry.get()
    if c1.get() == 1:
        if url == "":
            messagebox.showerror('Error', 'No url entered')
        else:
            result_box.configure(state='normal')
            result_box.insert(END, print(xss.run_XSS(url)))
            result_box.configure(state='disabled')

def save_results():
    filename = filedialog.asksaveasfilename(defaultextension='.txt',
    title="Save your file")
    if filename == "":
        return
    else:
        file = open(filename, 'w')
        file.write(result_box.get('1.0', 'end-1c'))
        file.close()


root = Tk()
root.geometry('530x800')

top_frame = Frame(root, padx=10, pady=10)
top_frame.grid(row=0, sticky='ew')

mid_frame = Frame(root, padx=10, pady=10)
mid_frame.grid(row=1, sticky='nsew')

bottom_frame = Frame(root, padx=10)
bottom_frame.grid(row=1, sticky='ew', pady=80)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

#top
url_lbl = Label(top_frame, text='Target website:')
url_lbl.grid(row=0, column=0)

url_entry = Entry(top_frame, width=40)
url_entry.grid(row=0, column=1)

#middle
c1 = IntVar()
c2 = IntVar()
c3 = IntVar()
c4 = IntVar()
xss_btn = Checkbutton(mid_frame, text='XSS', variable=c1)
xss_btn.grid(row=0, column=0)

ci_btn = Checkbutton(mid_frame, text='Code Injection', variable=c2)
ci_btn.grid(row=0, column=1)

port_scan_btn = Checkbutton(mid_frame, text='Port scanning', variable=c3)
port_scan_btn.grid(row=0, column=2)

session_scan_btn = Checkbutton(mid_frame, text='Session scan', variable=c4)
session_scan_btn.grid(row=0, column=3)
#bottom
result_label  = Label(bottom_frame, text='Results')
result_label.grid(row=0, column=0)
result_box = Text(bottom_frame, state='disabled', width=50)
result_box.grid(row=1, column=0)

start_btn = Button(top_frame, text='Run', width=5, command = run_function)
start_btn.grid(row=0, column=2, padx=2)

save_btn = Button(bottom_frame, text='Save', width=5, command=save_results)
save_btn.grid(row=2, column=0, pady=5)

root.mainloop()