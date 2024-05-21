#!/usr/bin/python3
"""
a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""
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
    completed_todos = list(filter(lambda x: x.get("completed"), todos))
    first_line = str.format("Employee {} is done" +
                            " with tasks({}/" +
                            "{}):", user.get("name"),
                            len(completed_todos), len(todos))
    print(first_line)
    for todo in completed_todos:
        print(str.format("\t {}", todo.get("title")))


if __name__ == "__main__":
    id = int(sys.argv[1])
    get_employee(id)
