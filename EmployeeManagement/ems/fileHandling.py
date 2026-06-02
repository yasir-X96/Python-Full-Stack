from ems.data import employees
# save employee to the file
def save_employee_to_file():
    with open("employees.txt", "a") as f:
       for emp_id, details in employees.items():
           f.write(f"{emp_id}\n{details["name"]}\n{details["department"]}")

def read_employees_from_file():
    with open("employees.txt") as f:
        print(f.read())