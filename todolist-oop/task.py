import uuid

class Task:
    def __init__(self, title):
        self.id = str(uuid.uuid4())
        self.title = title  
        self.isComplete = False
    
    def get_id_(self):
        """Return the task id"""
        return self.id

    def get_title(self) -> str:
        """Return the task title"""
        return self.title
