from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("750x250")

frm = ttk.Frame(root, padding=10)
frm.grid()

btn_1 = PhotoImage(file='Assets/BerndDoppler.png', width=100, height=100)
btn_2 = PhotoImage(file='Assets/JonasKahnwald.png', width=100, height=100)
ttk.Button(frm, image=btn_1).grid(column=1, row=0)
ttk.Button(frm, image=btn_2).grid(column=2, row=0)
root.mainloop()