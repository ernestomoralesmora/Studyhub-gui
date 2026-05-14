from storage import load_tasks, save_tasks


class TaskManager:

    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, text, priority):
        task = {
            "text": text,
            "priority": priority,
            "completed": False
        }
        self.tasks.append(task)
        save_tasks(self.tasks)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            save_tasks(self.tasks)

    def toggle_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            save_tasks(self.tasks)

    def get_tasks(self):
        return self.tasks