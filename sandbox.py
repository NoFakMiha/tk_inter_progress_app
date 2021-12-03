from tkinter import *
from tkinter import ttk

root = Tk()

button1_style = ttk.Style() # style for button1
# Configure the style of the button here (foreground, background, font, ..)
button1_style.configure('B1.TButton', foreground='red', background='blue')
button1 = ttk.Button(text='Deletar', style='B1.TButton')
button1.pack()

button2_style = ttk.Style() # style for button2
# Configure the style of the button here (foreground, background, font, ..)
button2_style.configure('B2.TButton', foreground='blue', background='red')
button2 = ttk.Button(text='Editar', style='B2.TButton')
button2.pack()

root.mainloop()