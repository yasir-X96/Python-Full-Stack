from exceptions.customExceptions import DuplicateEmployeeException
from services.employeeService import EmployService

while True:
    print("----- Welcome to SmartHR365 -----")
    print("1. Add Employee")
    print("0. Exit")

    choice = input("Enter your choice: ")

    try:
        match choice:
            case "1":
                EmployService.add_employee()

            case "0":
                print("Exiting...")
                break

            case _:
                print("Invalid Choice")

    except DuplicateEmployeeException as e:
        print(e)

    except Exception as e:
        print(f"Error: {e}")