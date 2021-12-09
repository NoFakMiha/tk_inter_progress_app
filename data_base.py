import json

PROJECTS = {
    "By car": {"TO DO 1": ["- make money", "-buy car"], "TODO 4": ["bla blablabababa"],
               "TODO 5": ["Kuj nekaj", "Theo gusi", "asdadadasdasdsdsadsad"]},
    "By second car": {"TO DO 2": ["- try out new", "-buy car third"]},
    "By thirdd car": {"TO DO 3": ["- dirb bake", "-blabla"]},
}


class Database:
    def __init__(self):
        with open("data.json") as file:
            self.projects = json.load(file)

    def save_new_project(self, name):
        self.projects[f"{name}"]={}
        with open("data.json", "w") as file:
            json.dump(self.projects,fp=file, indent=2)

    def save_new_label_to_project(self,data,key):
        self.projects[f"{key}"][f"{data}"]=[]
        with open("data.json", "w") as file:
            json.dump(self.projects,fp=file, indent=2)

    def save_new_todo_task(self, data,project, to_do_key):
        self.projects[f"{project}"][f"{to_do_key}"].append(f"{str(data)}")
        with open("data.json", "w") as file:
            json.dump(self.projects,fp=file, indent=2)