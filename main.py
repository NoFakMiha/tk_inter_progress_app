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

        # Adding new project label
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

    def projecting_label_and_entry_for_tasks(self,column):
        # Adding new project lable
        self.label_for_new_task = Label(self.label_frame, text="ADD NEW TASK")
        self.label_for_new_task.grid(column=column, row=0)

        # Adding new entry for project label
        self.entry_task_for_lable_str = StringVar()
        self.entry_task_for_lable = Entry(self.label_frame, textvariable=self.entry_task_for_lable_str)

        # Biding
        self.label_for_new_task.bind("<Enter>", self.hiding_add_new_task_lable)
        self.entry_task_for_lable.bind("<Leave>", self.displaying_add_new_task_lable)
        self.entry_task_for_lable.bind("<Return>", self.adding_and_saving_new_task)


        # Biding fire scritps
    def hiding_add_project_label(self, event):
        self.label_add_new_project.grid_forget()
        self.entry_new_project.grid(column=0, row=0, ipadx=10)

    def displaying_add_project_label(self, event):
        self.entry_new_project.grid_forget()
        self.label_add_new_project.grid(column=0, row=0)



    # Adding new projects
    def saving_new_project(self,event):
        self.title_new_project = self.entry_new_project.get()
        self.entry_new_project.delete(0,END)
        self.data.save_new_project(self.title_new_project.capitalize())
        self.projecting_projects()

    # Fire scritps Label frame | hiding label for task and entry

    def hiding_add_new_task_lable(self,event):
        self.label_for_new_task.grid_forget()
        self.entry_task_for_lable.grid(column=len(self.how_many_columns) + 1, row=0)

    def displaying_add_new_task_lable(self,event):
        self.entry_task_for_lable.grid_forget()
        self.label_for_new_task.grid(column=len(self.how_many_columns) + 1, row=0)

    def displaying_delete_todo_task(self, event, column,row):
        self.label_delite.grid(column=column,row=row, sticky ="en")

    # Adding ad saving lables
    def adding_and_saving_new_task(self,event):
        self.new_label_data = self.entry_task_for_lable.get()
        self.entry_task_for_lable.delete(0,END)
        self.data.save_new_label_to_project(key=self.project_key, data=self.new_label_data.upper())
        self.projecting_labels_and_task(self.project_key)

    # Adding and saving new todos
    def adding_and_saving_new_todos(self, event,one_of_the_entry_to_do,label_key,postion):
        self.todo_data = one_of_the_entry_to_do.get()
        one_of_the_entry_to_do.delete(0,END)
        #print(label_key)
        self.todo_keys = []
        for key in self.data.projects[label_key]:
            self.todo_keys.append(key)


        self.data.save_new_todo_task(data=self.todo_data,project=label_key,
                                     to_do_key=self.todo_keys[postion])

        self.projecting_labels_and_task(label_key)





    # projecting the UI
    def projecting_projects(self):
        for count,value in enumerate(self.data.projects):
          self.buton_project = Button(self.main_frame, text=value, width=20, command=partial(self.projecting_labels_and_task, value))
          self.buton_project.grid(column=0,row=count+1)



    def projecting_labels_and_task(self, key):
        self.children = self.label_frame.winfo_children()
        self.staring_positon_separator= 100

        try:
            print("TRY")
            for children in self.children:
                children.destroy()
            self.how_many_columns = []
            self.how_many_rows = []
            self.all_todos_entrys = []
            self.project_key = key
            for count_1,value in enumerate(self.data.projects[key]):
                self.label_task = Label(self.label_frame, text=value)
                self.label_task.grid(column=count_1 + 1, row=0, padx=10 )
                self.how_many_columns.append(count_1)
                self.how_many_rows_objects=[]
                for count_2, value in enumerate(self.data.projects[key][value]):
                    self.label_todo = Label(self.label_frame,text=value)
                    self.label_todo.bind("<Enter>", partial(self.displaying_delete_todo_task, column=count_1+1,
                                                            row=count_2+1))
                    self.label_todo.bind("<Button-1>", )
                    self.label_todo.grid(column=count_1+1,row=count_2+1, padx=10)
                    self.label_delite = Label(self.label_frame, text="-", bg="#bc951a")
                    self.how_many_rows_objects.append(count_2)
                self.how_many_rows.append(self.how_many_rows_objects)

                    # Eding entry fot todos
                self.entry_adding_todos = Entry(self.label_frame)
                self.all_todos_entrys.append(self.entry_adding_todos)

                # displaying entryies for todos
            for i in range(len(self.all_todos_entrys)):
                self.one_of_the_entry_to_do = self.all_todos_entrys[i]
                self.one_of_the_entry_to_do.grid(column=i+1, row=len(self.how_many_rows[i])+1)
                self.one_of_the_entry_to_do.bind("<Return>", partial(self.adding_and_saving_new_todos, one_of_the_entry_to_do=self.one_of_the_entry_to_do,label_key=key, postion=i ))


            # Cheking if they are  alredy any lables if not than puting in in first column and row
            self.children = self.label_frame.winfo_children()
            if len(self.children) <= 1:
               self.projecting_label_and_entry_for_tasks(column=len(self.how_many_columns) + 1)
            else:
                self.projecting_label_and_entry_for_tasks(column=len(self.how_many_columns) + 1)

        except EXCEPTION as e:
            print(e)
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

