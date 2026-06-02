from exceptions.customExceptions import (
    DuplicateEmployeeException,
    InvalidInputException
)
from models.employ import Employee
from utils.fileHandler import read_employees, save_employees


class EmployService:

    @staticmethod
    def add_employee():
        try:
            emp_id = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            department = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            doj = input("Enter Date of Joining (DD-MM-YYYY): ")

            # Read employees from JSON file
            employees = read_employees()

            # Check for duplicate employee ID
            for emp in employees:
                if emp["emp_id"] == emp_id:
                    raise DuplicateEmployeeException(
                        "Employee ID already exists"
                    )

            # Create Employee object
            employee = Employee(
                emp_id,
                name,
                department,
                salary,
                doj
            )

            # Add employee to list
            employees.append(employee.to_dict())

            # Save updated list
            save_employees(employees)

            print("Employee added successfully.")

        except ValueError:
            raise InvalidInputException(
                "Employee ID must be an integer and Salary must be numeric."
            )