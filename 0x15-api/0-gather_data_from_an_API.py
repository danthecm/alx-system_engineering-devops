#!/usr/bin/python3
"""A simple module that makes request to an api"""
import requests
import sys

employee_id = sys.argv[1]

base_url = "https://jsonplaceholder.typicode.com/"

employee_request = requests.get(f"{base_url}users/{employee_id}")

employee = employee_request.json()

tasks_request = requests.get(f"{base_url}todos?userId={employee_id}")

all_tasks = tasks_request.json()

completed = list(filter(lambda x: x.get("completed") == True, all_tasks))

print(
    f"Employee {employee.get('name')} \
is done with tasks({len(completed)}/{len(all_tasks)}):")
for todo in completed:
    print(f"\t {todo.get('title')}")
