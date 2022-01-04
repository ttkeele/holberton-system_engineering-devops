#!/usr/bin/python3
"""gathers info based on input id and saves to csv"""
from sys import argv
import requests
import csv


if __name__ == "__main__":
    userId = argv[1]
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.
        format(userId)).json()
    username = user.get('username')
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.
        format(userId)).json()

    with open('{}.csv'.format(userId), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([userId, username, task.get('completed'),
                             task.get('title')])
