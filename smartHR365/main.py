from hrms.exceptions.customExceptions import DuplicateEmployeeException
from hrms.services.employeeService import EmployService


if __name__ == "__main__":
    print("Application Started")

while True:
    print("-----Welcome to SmartHR365-------")
    print("1.AddEmployee")
    choice =input("enter yoyr choice::")
    #try:
    match choice:
            case "1":
                EmployService.add_employee()
            case _:
                print("invalid")
    #except DuplicateEmployeeException as e:
     #   print(e)

