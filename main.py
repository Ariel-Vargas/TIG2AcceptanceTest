# main.py

from todo_list import ToDoList

if __name__ == "__main__":
    todo = ToDoList()
    todo.add_task("Buy groceries", priority="High", due_date="2025-07-11", category="Personal")
    todo.add_task("Pay bills", priority="Low", due_date="2025-07-15", category="Finance")
    print("Initial task list:")
    todo.list_tasks()

    todo.mark_completed(1)
    print("\nAfter marking first task completed:")
    todo.list_tasks()

    todo.edit_task(2, description="Pay electricity bill", priority="Medium")
    print("\nAfter editing second task:")
    todo.list_tasks()

    todo.delete_task(1)
    print("\nAfter deleting first task:")
    todo.list_tasks()
