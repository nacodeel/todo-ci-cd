import pytest
from app.todo import ToDoApp

def test_add_task():
    app = ToDoApp()
    result = app.add_task("Buy milk")
    assert result == "Task 'Buy milk' added"
    assert app.list_tasks() == ["Buy milk"]

def test_add_empty_task():
    app = ToDoApp()
    with pytest.raises(ValueError):
        app.add_task("")

def test_remove_task():
    app = ToDoApp()
    app.add_task("Buy milk")
    result = app.remove_task("Buy milk")
    assert result == "Task 'Buy milk' removed"
    assert app.list_tasks() == []

def test_remove_nonexistent_task():
    app = ToDoApp()
    with pytest.raises(ValueError):
        app.remove_task("Go running")
