#import data
#from data import * 
from ems.fileHandling import read_employees_from_file
from ems.data import employees,departments
from ems.decorators import require_admin
from ems.customExceptions import EmployeeNotFoundException

# from customException import DuplicateEmployeeException,EmployeeNotFoundException
@require_admin
def add_employee(emp_id,name,department):
    #duplicate Key
    # if emp_id in employees:
    #     raise DuplicateEmployeeException(f"{emp_id} Already Exists")

    employees[emp_id]={
        "emp_id":emp_id,
        "name": name,
        "department":department,
        "role": "",
        "salary":0,
        "contact":(),# tuple
        "Skills":set(),
        "projects":[]
       

    }
    departments.add(department);
    print(f"Employee added-->Id:{emp_id}\tName::{name}\tDepartment::{department}\t")


def set_employee_role(emp_id,role="Trainee",salary=40000):
    
    employees[emp_id][role]=role
    employees[emp_id][salary]=salary
    print(f"Employee salary updated-->Id:{emp_id}\tRole::{role}\tSalary::{salary}")

def update_employee_contact(emp_id,email,phone,city):
    if emp_id not in employees:
        raise EmployeeNotFoundException(f"{emp_id} Not Found")

        #return
        #  print("Employee Not found!!")
      
    employees[emp_id]["contact"]=(email,phone,city)
    print(f"Employee updated::{emp_id}")
    print(f"Employee Contact updated::emali::{email}\tphone::{phone}\tcity::{city}")

def add_skills(emp_id, *skills):
    if emp_id not in employees:
        print("Employee Not found!!")
        return
    for skill in skills:
        employees[emp_id]["Skills"].add(skill)
    print(f"skill added::{employees[emp_id]["Skills"]}")

def create_emp_profile(emp_id, **extra_info):

    # store extra info into employees dictionary
    employees[emp_id].update(extra_info)

    for key,value in extra_info.items():
        print(f"{key}:{value}")

# @require_admin
def delete_all_employees():
    employees.clear()
    print("all records deleted")


# def getAllEmployees():
#     allEmployees = {
#     emp["emp_id"]: emp["name"]
#     for emp in employees.values()
# }
#     print(allEmployees)

def getEmployees():
    read_employees_from_file()
