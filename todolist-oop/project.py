import uuid

class Project:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4()) 
        self.name = name
        self.task_list = []

    def get_project_id(self):
        """Return the project id"""
        return self.id
    
    def get_tasks_lenght(self) -> int:
        """Return the lenght of the task list"""
        return len(self.task_list)

    def get_project_name(self) -> str:
        "Return the project name"
        return self.name

    def set_project_name(self, new_name:str) -> None:
        """Set the project name (usefull for update)"""
        self.name = new_name