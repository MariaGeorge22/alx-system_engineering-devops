#!/usr/bin/python3
"""
a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""
import json
import requests
import sys
API_URL = "https://jsonplaceholder.typicode.com/"


def get_all_employees():
    """
    returns information about all TODO list progress
    """
    users_url = "users"
    users = requests.get(API_URL+users_url).json()
    todos_url = "todos"
    todos = requests.get(API_URL+todos_url).json()
    dict = {}
    for user in users:
        id = user.get("id")
        dict[id] = []
        username = user.get("username")
        user_todos = list(
            filter(
                lambda x: x.get("userId") == id,
                todos
            )
        )
        for todo in user_todos:
            dict[id].append({
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username, 
            })
    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(dict, json_file)


if __name__ == "__main__":
    get_all_employees()
