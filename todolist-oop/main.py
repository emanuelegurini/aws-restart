from todolist import Todolist
from project import Project
from menu import Menu
from task import Task

def get_project_list(todolist: Todolist) -> list:
    """Returns the project list"""
    print("="*20)
    print("Lista dei progetti:")
    print("="*20)
    todolist.get_projects()

def update_project_name(todolist: Todolist):
    """
    This function contains al the logic related to the update project name process
    """
    get_project_list(todolist)

    id_progetto = input("Inserisci l'id del progetto da aggiornare: ")

    while True:

        new_name = input("Iserisci il nuovo nome del progetto: ")

        if todolist.is_project_name_already_exists(new_name):
            print(f"Un oggetto con il nome {new_name} esiste già")
            continue

        todolist.update_project_name(id_progetto, new_name)
        print(f"Update eseguito con successo per l'oggetto {id_progetto}")
        break
    
def add_new_project(todolist: Todolist):
    """
    This functions executes the full process to add a new projects.
    If a project with the same name already exists, it doesn't add the project to the list.
    """ 
    print("Hai scelto aggiungi progetto")
    print("="*30)
    project_name = input("Inserisci nome del progetto: ")
    
    if todolist.is_project_name_already_exists(project_name):
        print(f"Un oggetto con il nome {project_name} esiste già")
        return

    new_project = Project(project_name)
    todolist.add_project(new_project)
    print(f"il numero di progetti è: {todolist.get_projects_lenght()}")

def add_new_task(todolist: Todolist):
    print("Aggiungi task")

    get_project_list(todolist) 

    id_progetto = input("Inserisci l'id del progetto al quale aggiungere la task: ") 

    project = todolist.get_project_by_id(id_progetto)

    if project is None:
        print("Il pogetto non esiste!")
        return
    
    task_title = input("Inserisci il title della task: ")
    new_task = Task(task_title)
    project.add_task(new_task)

def get_task_list(todolist: Todolist):
    print("Lista i task")

    get_project_list(todolist)
    
    id_progetto = input("Inserisci l'id del progetto del quale vuoi conoscere il numero di task: ") 

    project = todolist.get_project_by_id(id_progetto)

    if project is None:
        print("Il pogetto non esiste!")
        return

    print(f"Numero di task: {project.get_tasks_lenght()}")

def main():
    todolist = Todolist()

    menu = Menu()

    while True: 

        menu.printMenu()

        i = input("Seleziona l'operazione da eseguire: ")

        match i:
            case "1": 
                add_new_project(todolist)

            case "2": 
                add_new_task(todolist)

            case "3":
                print("Aggiungi tag")
                continue

            case "4":
                get_project_list(todolist)

            case "5": 
                get_task_list(todolist)

            case "6":
                print("Lista i tags")
                continue

            case "7": 
                update_project_name(todolist)

            case "8":
                break
            case _: 
                print("Inserisci il valore corretto")
                continue



if __name__ == "__main__":
    main()