class Task:
    def __init__(self, title, description="", completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{status} {self.title}: {self.description}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        self.tasks.append(Task(title, description))

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()

    def list_tasks(self):
        return [str(task) for task in self.tasks]