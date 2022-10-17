#!/usr/bin/python3
'''exports all employee data to json file'''
import json
import requests


def all_employee_data_json():
    '''fetches all employee data converted to json'''
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    # format:
    # {
    #   user_id: [
    #     {
    #         "username": "USERNAME",
    #         "task": "TASK_TITLE",
    #         "completed": TASK_COMPLETED_STATUS
    #     },...
    #   ], user_id: [],...
    # }
    data = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        todo_l = []
        for todo in todos:
            if todo.get('userId') == user_id:
                task = todo.get('title')
                completed = todo.get('completed')
                todo_l.append(
                    {
                        'username': username,
                        'task': task,
                        'completed': completed
                    }
                )
        data[str(user_id)] = todo_l

    return data


if __name__ == '__main__':
    data = all_employee_data_json()
    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)
