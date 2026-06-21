import json
import os


FILE_PATH = "hrms/data/employees.json"

def read_employees():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH,"r")as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_employees(employee_list):
    with open(FILE_PATH,"w") as file:
        json.dump(employee_list,file,indent=4)