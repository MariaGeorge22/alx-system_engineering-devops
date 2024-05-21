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


def get_employee(id):
    """
    returns information about his/her TODO list progress
    """
    if not isinstance(id, int):
        raise ValueError("id must be an integer")
    if id is None:
        raise ValueError("id must be supplied")
    user_url = str.format("users/{}", id)
    user = requests.get(API_URL+user_url).json()
    todos_url = str.format(
        "users/{}/todos", id)
    todos = requests.get(API_URL+todos_url).json()
    dict = {}
    dict[id] = []
    username = user.get("username")
    for todo in todos:
        dict[id].append(
            {"task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username, }
        )
    with open(str.format("{}.json", id), 'w') as json_file:
        json.dump(dict, json_file)

    
if __name__ == "__main__":
    id = int(sys.argv[1])
    get_employee(id)
