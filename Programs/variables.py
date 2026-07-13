# Variables and DataTypes
# inetger
emp_id=100
# string
emp_name="shree"
# float
emp_salary=59806.67
print(id(emp_salary))
emp_salary=emp_salary+2000
print(id(emp_salary))
# booleanmc
is_permanent_emp=True
# None Type
manager_name=None
# print(emp_id)
# print(emp_name)
# print(emp_salary)
# print(is_permanent_emp)

#GST_AMOUNT=0.18 # for constant values

# print("employee Id::",emp_id)
# print("employee Name::",emp_name)
# print("employee Salary::",emp_salary)

#print(f"employee Id::{emp_id}\nemployeeName::{emp_name}\nsalary::{emp_salary}\nemploymentPermanentType::{is_permanent_emp}")
print(f"employee Id::{emp_id}\temployeeName::{emp_name}\tsalary::{emp_salary}\temploymentPermanentType::{is_permanent_emp}\tManager::{manager_name}")

print(type(emp_id))
print(type(emp_salary))
print(type(is_permanent_emp))
print(type(emp_name))
print(type(manager_name))

# same values will be pointing to the same memory location
# name="shree"
# name1=name
# print(id(name))
# print(id(name1))
# # print(name)
# # name=123
# # print(name)

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
# creating list
employees=["Shree","Shashank","Darshan","Darshan"]
#Access entire list
print(employees)
print(id(employees))
# Accessing With index
employees[0]="Arun"
print(employees)
print(id(employees))

# Add an employee
employees.append("Yasir");
print(employees)

# Remove an Employee
employees.remove("Arun")
#this line gives Error
#employees.remove(1)

# # insert at Specific index
# employees.insert(2,"Bharat")
# print(employees)

employees.sort()
print(employees)
ages=[45,20,30]
print(max(ages))
print(len(ages))

#tuple
employee_record=(2345,"Shree","Trainer","Shree")
#To change need to convert to other mutable type
#employee_list=list(employee_record)
print(employee_record)

#employee_record[0]=123

print(employee_record[1])

#set Datatype
departments={"AI","Testing","AI","Agile"}
print(departments)

departments.add("Development")
print(departments)

# Dictionary
employee={
    "id":200,
    "name":"shree",
    "department":"IT",
    "salary":50000,
    "salary":9000
}
print(employee)
# access Employee Name
print(employee["name"])

# changing values
employee["salary"]=60000
print(employee)
print(employee.get("name"))

employee_scores={
    123:"345",
    345:"000",
}

print(employee_scores)
print(employee_scores.get(123))
