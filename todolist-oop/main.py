from todolist import Todolist
from project import Project
from menu import Menu

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