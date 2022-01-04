#!/usr/bin/python3
"""gathers data and saves to json"""
from sys import argv
import requests
import json


if __name__ == "__main__":
    userId = argv[1]
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.
        format(userId)).json()
    username = user.get('username')
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.
        format(userId)).json()

    t_tasks = {userId: []}

    for task in tasks:
        t_tasks[userId].append({"task": task.get('title'),
                                "completed": task.get('completed'),
                                "username": username})

    with open('{}.json'.format(userId), 'w') as jsonfile:
        json.dump(t_tasks, jsonfile)
