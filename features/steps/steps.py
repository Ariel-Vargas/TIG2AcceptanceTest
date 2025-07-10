from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list is empty')
def step_impl(context):
    context.todo = ToDoList()

@given('the to-do list contains tasks')
def step_impl(context):
    context.todo = ToDoList()
    for row in context.table:
        task = row['Task']
        priority = row.get('Priority', 'Medium')
        due_date = row.get('Due Date', None)
        category = row.get('Category', 'General')
        context.todo.add_task(task, priority=priority, due_date=due_date, category=category)

        if row.get('Status', '').lower() == 'completed':
            context.todo.mark_completed(len(context.todo.tasks))

@when('the user adds a task "{task}"')
def step_impl(context, task):
    context.todo.add_task(task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    descriptions = [t.description for t in context.todo.tasks]
    assert task in descriptions, f"'{task}' not found in {descriptions}"

@when('the user lists all tasks')
def step_impl(context):
    context.listed_tasks = [t.description for t in context.todo.tasks]

@then('the output should contain')
def step_impl(context):
    expected = [row['Task'] for row in context.table]
    for task in expected:
        assert task in context.listed_tasks, f"'{task}' not found in listed tasks"

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    for i, t in enumerate(context.todo.tasks):
        if t.description == task:
            context.todo.mark_completed(i + 1)
            break

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    for t in context.todo.tasks:
        if t.description == task:
            assert t.completed is True
            return
    assert False, f"Task '{task}' not found or not completed"

@when('the user clears the to-do list')
def step_impl(context):
    context.todo.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo.tasks) == 0, "Task list is not empty"

@when('the user deletes task "{task}"')
def step_impl(context, task):
    for i, t in enumerate(context.todo.tasks):
        if t.description == task:
            context.todo.delete_task(i + 1)
            break

@then('the to-do list should not contain "{task}"')
def step_impl(context, task):
    descriptions = [t.description for t in context.todo.tasks]
    assert task not in descriptions, f"'{task}' was not deleted"

@when('the user edits task "{original}" with')
def step_impl(context, original):
    for i, t in enumerate(context.todo.tasks):
        if t.description == original:
            data = context.table[0]
            context.todo.edit_task(
                i + 1,
                description=data.get('Description'),
                priority=data.get('Priority'),
                due_date=data.get('Due Date'),
                category=data.get('Category')
            )
            break

@then('the task "{task}" should be updated in the list')
def step_impl(context, task):
    found = any(t.description == task for t in context.todo.tasks)
    assert found, f"'{task}' not found after editing"
