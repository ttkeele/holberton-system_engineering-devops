#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

from sys import argv
import requests


if __name__ == "__main__":

    userId = argv[1]
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.
        format(userId)).json()
    name = user.get('name')
    tasks_completed = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos?completed=true'.
        format(userId)).json()
    total_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.
        format(userId)).json()

    print('Employee {} is done with tasks\
          ({}/{})'.
          format(name, len(tasks_completed), len(total_tasks)))
    for item in tasks_completed:
        print('\t {}'.format(item.get('title')))
