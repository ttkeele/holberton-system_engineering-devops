#!/usr/bin/python3
"""saves user todo info"""
import requests
import json


if __name__ == "__main__":
    t_tasks = {}
    users = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_info = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.
            format(user_id)).json()
        username = user_info.get('username')
        tasks = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.
            format(user_id)).json()

        t_tasks[user_id] = []

        for task in tasks:
            t_tasks[user_id].append({"username": username,
                                    "task": task.get('title'),
                                     "completed": task.get('completed')})

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(t_tasks, jsonfile)
