#region functions basic
# def add_num(num1,num2):
#     #print(num1+num2)
#     return num1+num2
  

# print(add_num(10,20))
#endregion

employees={} # dict
departments= set() #set
projects = [] # list

#region function to add Employee
#region positional Arguments

# def add_employee(emp_id,name,department):
#     employees[emp_id]={
#         "emp_id":emp_id,
#         "name": name,
#         "department":department,
#         "role": "Not added",
#         "salary":0,
#         "contact":(),# tuple
#         "Skills":set(),
#         "projects":[]

#     }
#     departments.add(department);
#     print(f"Employee added-->Id:{emp_id}\tName::{name}\tDepartment::{department}")

# add_employee("Emp101","shree","Training")   
# add_employee("Emp102","Darshan","Engineering")
# #position of arguments must be maintained
# add_employee("AI","EMP103","Samhita")
# print(f"Available Departments::{departments}")
# #endregion
# #region Default Arguments
# def set_employee_role(emp_id,role="Trainee",salary=40000):
#     if emp_id not in employees:
#         print("Employee Not found!!")
#         return
#     employees[emp_id][role]=role
#     employees[emp_id][salary]=salary
#     print(f"Employee salary updated-->Id:{emp_id}\tRole::{role}\tSalary::{salary}")


# set_employee_role("Emp101")
# set_employee_role("Emp101","Manager")
# #endregion

# #region Keyword Argument
# def update_employee_contact(emp_id,email,phone,city):
#     if emp_id not in employees:
#         print("Employee Not found!!")
#         return
    
#     employees[emp_id]["contact"]=(email,phone,city)
#     print(f"Employee updated::{emp_id}")
#     print(f"Employee Contact updated::emali::{email}\tphone::{phone}\tcity::{city}")

# update_employee_contact(
#     city="Bnagalore",
#     phone="123456",
#     emp_id="Emp101",
#     email="shree@gmail.com"
# )

# # Access  contact Tuple 
# print(f"employees Contact::{employees["Emp101"]["contact"]}")
# print("email:",employees["Emp101"]["contact"][0])
# #endregion
# # region*args---variable number of arguments
# def add_skills(emp_id, *skills):
#     if emp_id not in employees:
#         print("Employee Not found!!")
#         return
#     for skill in skills:
#         employees[emp_id]["Skills"].add(skill)
#     print(f"skill added::{employees[emp_id]["Skills"]}")

# # #function call
# add_skills("Emp101","python","Flask")
# add_skills("Emp101","python","Flask","AI")
# # create a list of skills and pass to function
# skills_list=["ML","SQL"]
# add_skills("Emp101",*skills_list)
# # #endregion
# # #region Variable number keyword Arguments ** Kwargs

# def create_emp_profile(emp_id, **extra_info):

#     # store extra info into employees dictionary
#     employees[emp_id].update(extra_info)

#     for key,value in extra_info.items():
#         print(f"{key}:{value}")


# create_emp_profile(
#     "Emp101",
#     experience=3,
#     certifications="AI,Cloud"
# )
# print(employees)

# def update_salary(emp_id,*,new_salary,approved):
#     pass

# update_salary("Emp101",new_salary=10000)

#region Global scope and local scope
# user_name="shree"
# def greet():
#     global user_name
#     # local space
#     user_city="Bangalore"

#     user_name="vidhya"
#     print(user_name)
#     print(id(user_name))
#     print(user_city)

# greet()
# print(id(user_name))
# print(user_name)
#endregion

#region decorators basics
# def greet_employee(name):
#     print(f"welcome::{name}")

#  store function in variable
# welcome_employee=greet_employee
# welcome_employee("Shree")

# # pass function as an argument to another
# def run_function(func,value):
#     print("run_func is running now")
#     func(value) #greet_employee(value)

# run_function(greet_employee,"shreeVidhya")
 #endregion
#region  decorators usecase
# session = {
#     "User": "yasir",
#     "role":"Admin"

# }
# create a decorator ---for checking role and giving access
# def require_admin(func):
#     def wrapper(*args,**kwargs):
#         # check role
#         if session["role"]!="Admin":
#             print("permission not allowed")
#             return
#         print(f"role is :sessiion{session["role"]}")

#         return func(*args,**kwargs)
#     return wrapper
 
# @require_admin
# def add_employee(emp_id,name,department):
#     employees[emp_id]={
#         "emp_id":emp_id,
#         "name": name,
#         "department":department,
#         "role": "Not added",
#         "salary":0,
#         "contact":(),# tuple
#         "Skills":set(),
#         "projects":[]

#     }
#     departments.add(department);
#     print(f"Employee added-->Id:{emp_id}\tName::{name}\tDepartment::{department}")

# add_employee("Emp101","shree","Training")   


# @require_admin
# def delete_all_employees():
#     employees.clear()
#     print("all records deleted")

# delete_all_employees()
#endregion

#region lambda functions bsics

# def square(num):
#     return num* num
# print(square(4))
#endregion
# region lambda with sorted---explore map(), filter()
# square= lambda num:num*num
# print(square(5))

employees={
    101:{"name":"samhita","salary":50000},
    102:{"name":"shashank","salary":45000},
    103:{"name":"Bharat","salary":60000},
}
# print(employees)

# sorted_employees=sorted(employees.items(),key= lambda emp:emp[1]["salary"] )
# print("sorted on salary",sorted_employees)
#endregion
# recursive functions
def function():
    function()# recursive call
    # base condition

def fibonacci(n):
    #base condition
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(6))

employee_ids=list(employees.keys())
# print dictionary of employees  recursively
def display_employees(index=0):
    #base condition
    if index>=len(employees):
        print("All employees displayed")
        return
    emp_id=employee_ids[index]
    #print(f" id::{emp_id}\tname::{[emp_id]["name"]}\t salary::{[emp_id]["salary"]}")
    print(
    f" id::{emp_id} |"
    f" Name::{[emp_id]['name']}"
    )
    display_employees(index+1)

display_employees()