import tkinter
from tkinter import *
from tkinter import ttk
from functools import partial

import math

from config import *

class ProgresAppInterface:
    def __init__(self):
        self.window = Tk()

        self.window.title("KanPROGRESSban")
        self.window.minsize(width=MIN_WIN_WIDTH, height=MINT_WIN_HEIGHT)
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"600x850+{math.floor(self.screen_width/2)-225}+{math.floor(self.screen_height/2)-425}")
        #self.window.wm_attributes("-transparentcolor", "red")
        self.window.config(padx=20, pady=20, bg=MAIN_BACK_COLOR)

        self.dict_of_projects = {}
        self.row_of_dict= 0

        self.p = ttk.Panedwindow(self.window, orient=HORIZONTAL)


        # frame for  projects


        self.frame_projects = ttk.Frame(self.window, borderwidth=1, style="FrameProjects.TFrame", width=300, height=self.screen_height)
        self.frame_projects.grid_propagate(False)
        self.frame_projects.grid(column=0, row=0)
        self.projects_entry_box = StringVar()

        self.projects_entry = ttk.Entry(self.frame_projects, textvariable=self.projects_entry_box, width=29)
        self.projects_entry.grid(column=0, row=0)

        self.project_add_button = ttk.Button(self.frame_projects, text="+", command=self.adding_project, style="AddProject.TButton")
        self.project_add_button.grid(column=1, row=0, padx=1)

        self.style_projects = ttk.Style()
        self.style_projects.configure("AddProject.TButton", background=PROJECT_FRAME_BACK_COLOR, width=10)
        self.style_projects.configure("FrameProjects.TFrame", background=MAIN_BACK_COLOR)  # config of the first frame
        self.style_projects.configure("Entry.TEntry", background=PROJECT_FRAME_BACK_COLOR, width=30)
        self.style_projects.configure("New.TLabelframe.Label", background=PROJECT_FRAME_BACK_COLOR, width=30)

        self.window.mainloop()


    def projecting_frame(self, name):
        print(name)
        for i in range(0,len(self.dict_of_projects[name]["frames"])):
            self.frame_label = self.dict_of_projects[name]["frames"][i]
            self.adding_frames_entry= ttk.Entry(self.frame_label)
            self.adding_frames_entry.grid(column=0,row=0)

            self.adding_frames_button = ttk.Button(self.frame_label)
            self.adding_frames_button.grid(column=1,row=0)


    def adding_project(self):
        self.dict_of_projects[f"{self.projects_entry.get()}"] = {
            'frames':[ttk.Frame(self.window,style="FrameProjects.TFrame", width=300, height=self.screen_height)],
            "labels":[],}
        self.projects_entry.delete(0, "end")

        self.key = []
        for key in self.dict_of_projects:
            self.key.append(key)

        for i in range(0,len(self.key)):
            self.projects_buttons = ttk.Button(self.frame_projects, text=f"{self.key[i]}", style="AddProject.TButton",
                                               width=29, command=partial(self.projecting_frame,name=self.key[i]))
            self.projects_buttons.grid(column=0, row=i+1)





