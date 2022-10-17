'''exports employee data to json file'''
import requests
from sys import argv
import json


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
    with open('{}.json'.format(employee_id), 'w') as f:
        id_str = '{}'.format(employee_id)
        user_data = {
            id_str: []
        }

        todos = data[3]
        username = data[4]

        for todo in todos:
            user_data[id_str].append(
                {
                    'task': todo.get('title'),
                    'completed': todo.get('completed'),
                    'username': username
                }
            )
        json.dump(user_data, f)
