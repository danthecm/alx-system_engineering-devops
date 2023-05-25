#!/usr/bin/python3
"""
A simple module that makes request to an api
to retrieve user information and todos from
the api and prints the user name and completed/total tasks

Args:
employee_id: The id of the employee to retrieve
"""
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com/"

    employee_request = requests.get(f"{base_url}users/{employee_id}")

    employee = employee_request.json()

    name = employee.get("name")

    tasks_request = requests.get(f"{base_url}todos?userId={employee_id}")

    all_tasks = tasks_request.json()

    completed = list(filter(lambda x: x.get("completed"), all_tasks))

    print("Employee {} is done with tasks({}/{}):".format(name,
          len(completed), len(all_tasks)))
    for todo in completed:
        print(f"\t {todo.get('title')}")
