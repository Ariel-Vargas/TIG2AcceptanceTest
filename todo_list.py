# todo_list.py

class Task:
    def __init__(self, description, priority="Medium", due_date=None, category="General"):
        self.description = description
        self.completed = False
        self.priority = priority
        self.due_date = due_date
        self.category = category

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.description} | Priority: {self.priority} | Due: {self.due_date} | Category: {self.category}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority="Medium", due_date=None, category="General"):
        self.tasks.append(Task(description, priority, due_date, category))

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def mark_completed(self, index):
        try:
            self.tasks[index - 1].completed = True
        except IndexError:
            print("Invalid task index.")

    def clear_tasks(self):
        self.tasks.clear()

    def delete_task(self, index):
        try:
            del self.tasks[index - 1]
        except IndexError:
            print("Invalid task index.")

    def edit_task(self, index, description=None, priority=None, due_date=None, category=None):
        try:
            task = self.tasks[index - 1]
            if description:
                task.description = description
            if priority:
                task.priority = priority
            if due_date:
                task.due_date = due_date
            if category:
                task.category = category
        except IndexError:
            print("Invalid task index.")
