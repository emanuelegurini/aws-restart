"""
- menu
- todolist
- project
- task
- tag
"""

class Menu:
    def printMenu(self) -> None:
        print(f"""
        1. Add Project
        2. Add Task
        3. Add Tag
        4. List Pojects
        5. List Task
        6. List Tags
        7. exit
    """)

class Todolist:
    def __init__(self):
        self.projects = []

    def add_project(self, project: Project) -> None:
        self.projects.append(project)
    
    def get_projects_lenght(self) -> int:
        return len(self.projects)

    def get_projects(self) -> list[Project]:
        for p in self.projects:
            return f"{p.id} - {p.name}"
        
    def update_project_name(self, id: str) -> None:
        target = next((project for project in self.projects if project.get_project_id() == id), None)
        target.set_project_name("pippo")


import uuid

class Project:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4()) 
        self.name = name
        self.task_list = []

    def get_project_id(self):
        return self.id
    
    def get_tasks_lenght(self) -> int:
        return len(self.task_list)

    def get_project_name(self) -> str:
        return self.name

    def set_project_name(self, new_name:str) -> None:
        self.name = new_name




def main():
    todolist = Todolist()

    menu = Menu()

    while True: 

        menu.printMenu()

        i = input("Seleziona l'operazione da eseguire: ")

        match i:
            case "1": 
                print("Hai scelto aggiungi progetto")
                print("="*20)
                project_name = input("Inserisci nome del progetto: ")
                new_project = Project(project_name)
                todolist.add_project(new_project)
                print(todolist.get_projects_lenght())
                continue
            case "2": 
                print("Aggiungi task")
                continue
            case "4": 
                id_progetto = input("Inserisci l'id del progetto da aggiornare: ")
                print(todolist.update_project_name(id_progetto))
            case "5": 
                print(todolist.get_projects())
            case "7":
                break
            case _: 
                print("Inserisci il valore corretto")
                continue



if __name__ == "__main__":
    main()