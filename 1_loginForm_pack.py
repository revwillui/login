import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("310x300")
window.title("LOGIN ACCOUNT")

pane = tk.Frame(window)
pane.pack(fill= BOTH, expand = True)

lb1 = tk.Label(pane, text = "LOGIN", font = "Calibri 50 bold" )
lb1.pack(fill= BOTH, expand = False)

entry1 = tk.Entry(pane,  text = "Username", font = ("Calibri 10 bold") )
entry1.pack(pady=6,padx= 1 ,expand = False)

entry2 = tk.Entry(pane, font = "Calibri 10 bold", text = "Password" )
entry2.pack(pady=6,padx= 1 ,expand = False)

button1 = tk.Button(pane, text = "Login")
button1.pack()

check = tk.Checkbutton(pane, text = "Remember me")
check.pack(side = LEFT  ,expand = False ,fill= X)

lb2 = tk.Label(pane, text = "Forget Password?", font = "Ariel 10 bold", fg = "blue" )
lb2.pack(side = RIGHT ,expand = False)

button1 = tk.Button(pane, text = "Create Account",)
button1.pack(side = BOTTOM,expand = FALSE)

window.mainloop()