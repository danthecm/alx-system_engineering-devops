#!/usr/bin/python3
"""
A simple module that makes request to an api
to retrieve user information and todos from
the api and prints the user name and completed/total tasks
exports the result to a csv file

Args:
employee_id: The id of the employee to retrieve
"""
import requests
import sys
import csv

if __name__ == '__main__':
    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com/"

    employee_request = requests.get(f"{base_url}users/{employee_id}")

    employee = employee_request.json()

    name = employee.get("name")

    tasks_request = requests.get(f"{base_url}todos?userId={employee_id}")

    all_tasks = tasks_request.json()

    data = []

    for task in all_tasks:
        is_completed = task.get('completed')
        title = task.get('title')
        data.append([employee_id,
                     name, is_completed, title])

    with open("{}.csv".format(employee_id), "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
