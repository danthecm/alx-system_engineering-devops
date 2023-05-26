#!/usr/bin/python3
"""
A simple module that makes request to an api
to all user information and todos from
the api and prints the user name and completed/total tasks
exports the result to a json file

Args:
employee_id: The id of the employee to retrieve
"""
import json
import requests

if __name__ == '__main__':

    base_url = "https://jsonplaceholder.typicode.com/"

    users_req = requests.get(f"{base_url}users")

    users = users_req.json()

    all_users = {}

    for user in users:

        username = user.get("username")

        user_id = user.get("id")

        tasks_request = requests.get(f"{base_url}todos?userId={user_id}")

        all_tasks = tasks_request.json()

        data = []

        for task in all_tasks:
            completed = task.get('completed')
            title = task.get('title')
            data.append(
                {"task": title, "completed": completed, "username": username})

        all_users[str(user_id)] = data

    with open("todo_all_employees.json", "w") as file:

        json_dump = json.dumps(all_users)

        file.write(json_dump)
