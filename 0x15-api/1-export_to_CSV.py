#!/usr/bin/python3
"""
a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""
import csv
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
    rows = []
    username = user.get("username")
    for todo in todos:
        rows.append([
            id,
            username,
            todo.get("completed"),
            todo.get("title")
        ])
    with open(str.format("{}.csv", id), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for row in rows:
            writer.writerow(row)


if __name__ == "__main__":
    id = int(sys.argv[1])
    get_employee(id)
