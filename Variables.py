# Variables and Datatypes
# integer
emp_id=100
# string    
emp_name="Yasir"
# float
emp_salary=59806.67
print(id(emp_salary))
emp_salary=emp_salary+2000
print(id(emp_salary));
# boolean
is_permenant_emp=True 
# None Type
manager_name=None
# print(emp_name)
# print(emp_id)
# print(emp_salary)
# print(is_permenant_emp)
#GST_AMOUNT=0.18 #for Constant Values

# print("employee Id::",emp_id)
# print("employee Name::",emp_name)
# print("employee Salary::",emp_salary)

# print(f"employee Id::{emp_id}\nemployee Name::{emp_name}\nSalary::{emp_salary}\nemploymentPermenantType::{is_permenant_emp}")
print(f"employee Id::{emp_id}\temployee Name::{emp_name}\tSalary::{emp_salary}\temploymentPermenantType::{is_permenant_emp}\tManager Name::None")

print(type(emp_id)) 
print(type(emp_salary))
print(type(is_permenant_emp))
print(type(emp_name))
print(type(manager_name))


# Same values will be pointing to the same memory location
# name="Yasir"
# name1=name
# print(id(name))
# print(id(name1))
# # print(name)
# # name=123
# # print(Name) 

# yearly_bonus=int(3400.54)
# print(yearly_bonus)
# emp_hra=200
# emp_code="1023"
# emp_converted=int(emp_code)
# print(emp_code)

# #bytes
# salary=54000
# salary_bytes=salary.to_bytes(4)
# print(salary_bytes);

# msg="hello"
# bytes_msg=msg.encode("utf-8")


# List Datatype
# Creating list
employees=["Yasir","Nadman","Shashank","Shashank"]
#Access entire list
print(employees)
print(id(employees))
# Accessing with index
employees[0]="Man"
print(employees)
print(id(employees))

# Add an employee
employees.append("Rohith");
print(employees);

# Remove an Employee
employees.remove("Man")
#this line gives error
#employees.remove("1")

# # insert at specific index
# employees.insert(2,"Bharat")
# print(employees)

employees.sort()
print(employees)
ages=[45,20,30]
print(max(ages))
print(len(ages))

#tuple
employee_record=(2345,"Yasir","Trainer",)
#To change need to convert to other mutable type
# employee_list=list(employee_record)
print(employee_record)

# employee_record[0]=123

print(employee_record[1])

#set Datatype
departments={"AI","Testing","AI","Agile"}
print(departments)

departments.add("Development")
print(departments)

# Dictionary
employee={
    "id":200,
    "name":"Yasir",
    "department":"IT",
    "Salary":50000,
    "Salary":9000
    
}
print(employee)
# access Employee Name
print(employee["name"])

# changing values 
employee["Salary"]=60000
print(employee)
print(employee.get("name"))

employee_scores={
    123:"345",
    345:"000",  
}

print(employee_scores)
print(employee_scores.get(123))