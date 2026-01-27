import requests

def get_projects():
    data = requests.get("http://127.0.0.1:8000/projects")
    print(data.json())
    
def get_task_by_project_id(project_id: str):
    data = requests.get(f"http://127.0.0.1:8000/tasks/{project_id}")
    print(data.json())


def main():
    # Assumiamo che il main lanci un menu con varie opzioni. Tra queste la lista dei progetti 
    
    #get_projects()
    get_task_by_project_id('3e40b2779ac84025bd77768b19f6b0c3')
    


main()