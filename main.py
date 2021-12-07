import tkinter
from config import *
from tkinter import *
from ttkbootstrap import *
from tkinter import ttk
from data_base import *
from functools import partial


class App():
    def __init__(self):

        self.window = Tk()
        self.style = Style("solar")
        self.window.minsize(250,250)
        self.window.geometry("900x750")

        self.main_frame = Frame(self.window, width=150, height=300)
        self.main_frame.grid_propagate(False)
        self.main_frame.grid(column=0,row=0)

        self.label_frame = Frame(self.window,width=self.window.winfo_screenwidth(), height=300)
        self.label_frame.grid_propagate(False)
        self.label_frame.grid(column=1,row=0)

        # USER INTERFACE

        # Separating line horizontal ad new project
        self.seperator_style= ttk.Style()
        self.seperator_style.configure("Line.TSeparator",background="#bc951a")
        self.separator = ttk.Separator(self.window, orient='vertical',style="Line.TSeparator")
        self.separator.place(x=148, y=0, width=1, height=self.window.winfo_screenheight())

        # Separating line horizontal ad taks top one
        self.separator_horizontal = ttk.Separator(self.window,orient='horizontal', style="Line.TSeparator")
        self.separator_horizontal.place(x=0, y=23, width=self.window.winfo_screenwidth(), height=1)

        # Adding new project button
        self.label_add_new_project = Label(self.main_frame, text="NEW PROJECT", width=20, bg="#bc951a")
        self.label_add_new_project.grid(column=0, row=0)

        # Adding new project entry
        self.entry_new_project_str = StringVar()
        self.entry_new_project = Entry(self.main_frame, textvariable=self.entry_new_project_str, bg="#bc951a",
                                       fg="white", bd=1)

        # Biding the widgets
        self.label_add_new_project.bind("<Enter>", func=self.hiding_add_project_label)
        self.entry_new_project.bind("<Leave>", func=self.displaying_add_project_label)
        self.entry_new_project.bind("<Return>", func=self.saving_new_project)





        # Biding fire scritps
    def hiding_add_project_label(self, event):
        self.label_add_new_project.grid_forget()
        self.entry_new_project.grid(column=0, row=0, ipadx=10)

    def displaying_add_project_label(self, event):
        self.entry_new_project.grid_forget()
        self.label_add_new_project.grid(column=0, row=0)

    def saving_new_project(self,event):
        self.title_new_project = self.entry_new_project.get()
        self.entry_new_project.delete(0,END)
        self.data.save_new_project(self.title_new_project)
        self.projecting_projects()


    def projecting_projects(self):
        for count,value in enumerate(self.data.projects):
          self.buton_project = Button(self.main_frame, text=value, width=20, command=partial(self.projecting_labels_and_task, value))
          self.buton_project.grid(column=0,row=count+1)



    def projecting_labels_and_task(self, key):
        self.children = self.label_frame.winfo_children()
        self.staring_positon_separator= 100
        try:
            for children in self.children:
                children.destroy()

            for count_1,value in enumerate(self.data.projects[key]):
                self.label_task = Label(self.label_frame, text=value)
                self.label_task.grid(column=count_1 + 1, row=0, padx=10 )

                for count_2, value in enumerate(self.data.projects[key][value]):
                    self.label_todo = Label(self.label_frame,text=value)
                    self.label_todo.grid(column=count_1+1,row=count_2+1, padx=10)
        except:

            for count_1,value in enumerate(self.data.projects[key]):
                self.label_task = Label(self.label_frame, text=value)
                self.lables_tasks.append(self.label_task)
                self.label_task.grid(column=count_1 + 1, row=0, padx=10)

                self.staring_positon_separator += 30
                for count_2, value in enumerate(self.data.projects[key][value]):
                    self.label_todo = Label(self.label_frame,text=value)
                    self.label_todo.grid(column=count_1+1,row=count_2+1, padx=10)


    def runn(self):
        self.data = Database()
        self.projecting_projects()
        Database()
        self.window.mainloop()







if __name__ == "__main__":
    App().runn()

