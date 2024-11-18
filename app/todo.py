class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task:
            raise ValueError("Task cannot be empty")
        self.tasks.append(task)
        return f"Task '{task}' added"

    def list_tasks(self):
        return self.tasks

    def remove_task(self, task):
        if task not in self.tasks:
            raise ValueError(f"Task '{task}' not found")
        self.tasks.remove(task)
        return f"Task '{task}' removed"

    def mark_task_done(self, task):
        if task not in self.tasks:
            raise ValueError(f"Task '{task}' not found")
        self.tasks[self.tasks.index(task)] = f"{task} (done)"
        return f"Task '{task}' marked as done"