from hrms.exceptions.customExceptions import DuplicateEmployeeException, InvalidInputException
from hrms.models.employ import Employee
from hrms.utils.fileHandler import *
from hrms.models.permanentEmploy import PermanentEmployee

class EmployService:
   @staticmethod
   def add_employee():
        try:
            emp_id=int(input("enter employee Id::"))
            name=input("enter name::")
            department=input("enter department::")
            doj=input("Enter Date of Join(DD-MM-YYYY)::")
            employees=read_employees()
            for emp in employees:
                if emp["emp_id"] == emp_id:
                    raise DuplicateEmployeeException("Employee Id Already Exists")
            

            print("Employee Type")
            print(f"1. Permanent Employee Type\n2.Contract EMployee")
            emp_type=input("Enter your Choice::")
            if emp_type=="1":
                salary=float(input("Enter the Salary::"))
                experience=int(input("enter the experience::"))

                employee=PermanentEmployee(emp_id,name,department,doj,salary,experience)
            else:
                raise InvalidInputException("Invalid Input")
            employees.append(employee.to_dict())
            #call file method to save 
            save_employees(employees)
            print("Employee Added Successfully")
        except ValueError:
            raise InvalidInputException("Id salary values must be proper")
        

# def get_employee_objetcs():
#        employee_data=read_employees()
#        employee_objects=[]
#        for emp in employee_data:
#            emp_type=emp["employee_type"]
#            if emp_type=="Permanent":
#                employee_objects.append(PermanentEmployee(
#                    emp["emp_id"],
#                    emp["name"],
#                    emp["department"],
#                    emp["salary"],
#                ))
#                return employee_objects
           
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # @staticmethod
    # def add_employee():
    #     try:
    #         emp_id=int(input("enter employee Id::"))
    #         name=input("enter name::")
    #         department=input("enter department::")
    #         #Zsalary=float(input("Enter salary::"))
    #         doj=("Enter Date of Join(DD-MM-YYYY)::")
    #         #reading from file (json)
    #         employees=read_employees()
    #         # duplicate Employee
    #         for emp in employees:
    #             if emp["emp_id"]==emp_id:
    #                 raise DuplicateEmployeeException("Employee Id Already Exists")
    #         #creating Employee Object
    #         employee=Employee(
    #             emp_id,name,department,salary,doj
    #         )
    #         #adding Employee to the existing list
    #         employees.append(employee.to_dict())
    #         #call the file method to save the data
    #         save_employees(employees)
    #         print("Employee Added Successfully")
    #     except ValueError:
    #         raise InvalidInputException("Id salary values must be proper")
        
   