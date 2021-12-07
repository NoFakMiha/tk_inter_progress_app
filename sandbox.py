import tkinter
from tkinter import *
import ttkbootstrap as ttk

root = Tk()

button1_style = ttk.Style("darkly") # style for button1
# Configure the style of the button here (foreground, background, font, ..)
root.minsize(600,800)
entry_str = StringVar()
new_entry = Entry(root, textvariable=entry_str)


def adding_new_project(event):
    print("enter")
    button1.grid_forget()
    new_entry.grid(column=0, row=0)

def leaving_new_project(event):
    print("leave")
    button1.grid(column=0,row=0)
    new_entry.grid_forget()


button1 = Button(text='Deletar')
button1.grid(column=0,row=0)

button1.bind('<Enter>', func=adding_new_project)
new_entry.bind('<Leave>', func=leaving_new_project)

button1.focus()
root.mainloop()