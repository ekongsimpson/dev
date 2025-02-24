import streamlit as sl
import todo_funcz

sl.title('My Todo App')
sl.subheader('This is a simple todo web app')

# Initialize session state
if "todos" not in sl.session_state:
    sl.session_state.todos = [todo.strip("\n") for todo in todo_funcz.get_todos()]
if "edit_index" not in sl.session_state:
    sl.session_state.edit_index = None  # Track which todo is being edited

def add_todo():
    todo = sl.session_state["new_todo"]
    if todo.strip():  # Ensure the todo is not empty
        sl.session_state.todos.append(todo.strip())
        todo_funcz.write_todos(sl.session_state.todos)

def delete_todo(index):
    sl.session_state.todos.pop(index)
    todo_funcz.write_todos(sl.session_state.todos)

def edit_todo(index):
    # Update the todo with the new value from the input field
    new_todo = sl.session_state[f"edit-input-{index}"]
    if new_todo.strip():  # Ensure the edited todo is not empty
        sl.session_state.todos[index] = new_todo.strip()
        todo_funcz.write_todos(sl.session_state.todos)
        sl.session_state.edit_index = None  # Exit edit mode

# Display todos with checkboxes, todo text, and edit buttons
for index, todo in enumerate(sl.session_state.todos):
    # Create columns for checkbox, todo text, and edit button
    col1, col2, col3 = sl.columns([1, 4, 1])  # Adjust column widths as needed
    with col1:
        checkbox = sl.checkbox(
            "", 
            key=f"checkbox-{index}", 
            help="Check this box to delete the todo"  # Add a delete tooltip
        )
    with col2:
        if sl.session_state.edit_index == index:
            # Initialize the session state key for the edit input
            if f"edit-input-{index}" not in sl.session_state:
                sl.session_state[f"edit-input-{index}"] = todo
            
            # Show an input field for editing
            sl.text_input(
                "Edit todo",
                value=sl.session_state[f"edit-input-{index}"],
                key=f"edit-input-{index}",
                on_change=edit_todo,
                args=(index,)
            )
        else:
            sl.write(todo)
    with col3:
        if sl.button("Edit", key=f"edit-button-{index}"):
            sl.session_state.edit_index = index  # Enter edit mode for this todo
    
    # Delete todo if checkbox is checked
    if checkbox:
        delete_todo(index)

# Add a new todo
sl.text_input(label="Todo", placeholder="Enter a new todo...", 
              on_change=add_todo, key="new_todo")

## Debugging: Print session state
#sl.write("Session State:")
#sl.write(sl.session_state)