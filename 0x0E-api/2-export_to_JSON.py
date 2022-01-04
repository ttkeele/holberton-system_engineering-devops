#!/usr/bin/python3
"""gathers data and saves to json"""
from sys import argv
import json
import requests


if __name__ == "__main__":
    user_id = argv[1]
    user_info = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.
        format(user_id)).json()
    username = user_info.get('username')
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.
        format(user_id)).json()

    t_tasks = {user_id: []}

    for task in tasks:
        t_tasks[user_id].append({"task": task.get('title'),
                                "completed": task.get('completed'),
                                 "username": username})

    with open('{}.json'.format(user_id), 'w') as jsonfile:
        json.dump(t_tasks, jsonfile)
