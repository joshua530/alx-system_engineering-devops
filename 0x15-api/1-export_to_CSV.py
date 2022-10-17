#!/usr/bin/python3
'''exports employee data in csv format'''
import csv
import requests
from sys import argv


def fetch_data(id):
    '''fetches employee data using id

    format: [name, id, [done_tasks], [all_tasks], username]
    '''
    data = ['', 0, [], [], '']
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        id)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    data[0] = user.get('name')
    data[1] = id
    data[4] = user.get('username')
    for todo in todos:
        if todo.get('userId') == user.get('id'):
            data[3].append(todo)
            if todo.get('completed') is True:
                data[2].append(todo)
    return data


if __name__ == '__main__':
    employee_id = argv[1]
    data = fetch_data(employee_id)
    with open('{}.csv'.format(employee_id), 'w') as file:
        fields = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(file, fields, quoting=csv.QUOTE_ALL)
        todos = data[3]
        user_id = data[1]
        username = data[4]
        for todo in todos:
            writer.writerow(
                {
                    'USER_ID': user_id,
                    'USERNAME': username,
                    'TASK_COMPLETED_STATUS': todo.get('completed'),
                    'TASK_TITLE': todo.get('title')
                }
            )
