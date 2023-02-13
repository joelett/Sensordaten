from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from datetime import date

def test():
    print("test")

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
today = date.today()
cal = Calendar(frm,font="Arial 14", selectmode='day', maxdate=today).grid(column=0,row=2)
ttk.Label(frm, text="Test").grid(column=0, row=0)
ttk.Button(frm, text="Test", command=test).grid(column=0, row=1)

root.mainloop()
