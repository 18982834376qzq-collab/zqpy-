from typing import List
from dataclasses import dataclass, asdict
import json
@dataclass
class Todo:
    name:str
    done:bool=False

def load_todos() -> List[Todo]:
    todo_list: List[Todo] = []
    try:
        with open("todos.json","r",encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                todo_list.append(Todo(**item))
    except FileNotFoundError:
        print("提示：todos.json不存在，使用空白任务清单")
    return todo_list

def add_todo(name:str) -> Todo:
    pass

def complete_todo(todo_list:List[Todo], num:int) -> None:
    pass

def delete_todo(todo_list:List[Todo], num:int) -> None:
    pass

def show_todo(todo_list:List[Todo]) -> None:
    pass