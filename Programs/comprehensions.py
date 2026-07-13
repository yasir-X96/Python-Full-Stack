employees=[
    {"id":101,"name": "samhita", "salary": 50000},
    {"id":102,  "name": "shashank", "salary": 45000},
    {"id":103,"name": "Bharat", "salary": 60000}
]

#get employees
# names=[]
# for emp in employees:
#     names.append(emp["name"])

#List Comprehension
# [expression for item in iterable]
# [expression for item in iterable if condition]
names=[emp["name"] for emp in employees]
print(names)

# get employees whose salary is more than 45000
# normal loop
high_salary=[]
# for emp in employees:
#     if emp["salary"]>45000:
#         high_salary.append(emp)

# with comprehension
high_salary = [
    emp for emp in employees
    if emp["salary"] >45000
]
print(high_salary)

#Dict Comprehension
# {Key:value for item in iterable}
# map id with name
emp_dict={}
# for emp in employees:
#     emp_dict[emp["id"]]=emp["name"]

# print(emp_dict)

#comprehension
emp_dict={
    emp["id"]:emp["name"]
    for emp in employees
}
print(emp_dict)

#set comprehension
salaries={
    emp["salary"] for emp in employees
}
print(salaries)