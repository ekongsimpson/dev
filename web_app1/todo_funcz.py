import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as todo_file:
        todo_file.write("")

FILENAME = "todos.txt"
#FILENAME = os.path.join(os.path.dirname(__file__), "todos.txt") # This is the path to the file  todos.txt   in the same directory as this file  todo_funcz.py   in the HACKERRANK/megacourse directory  .
#FILENAME = "todos.txt"
#ILENAME = "megacourse/todos.txt"


def get_todos():
    with open(FILENAME, "r") as todo_file:
        todos = todo_file.readlines()
    return todos


def write_todos(todos):
    with open(FILENAME, "w") as todo_file:
        #todo_file.writelines(todos)
        [todo_file.writelines(todo + '\n') for todo in todos]

#def edit_todos(todos):
#    with open(FILENAME, "w") as todo_file:
#        [todo_file.writelines(todo + '\n') for todo in todos]