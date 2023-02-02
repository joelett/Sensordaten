from tkinter import *
from tkinter import ttk



def test():
    print("test")

root = Tk()
frm = ttk.Frame(root, pawdding=10)
frm.grid()
ttk.Label(frm, text="Test").grid(column=0, row=0)
ttk.Button(frm, text="Test", command=test).grid(column=0, row=1)
root.mainloop()
