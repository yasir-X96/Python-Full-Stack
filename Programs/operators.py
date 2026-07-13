# region arithmatic operators
# calculate total salary of an employee
extrahrs_work = 5
payment_perhr = 400
over_time_pay = extrahrs_work * payment_perhr

basic_salary = 35000
bonus = 2000
tax = 1500
net_salary = basic_salary+bonus+over_time_pay-tax
print(f"NetSalary::{net_salary}")
# endregion
# region Assignment Operators(=,+=,-=)
num_leaves = 10
num_leaves -= 2  # num_leaves=num_leaves-2
print(num_leaves)
# endregion
# region Logical Operators(And, or,not)
# check employee eligibility for promotion
# experience , Rating
experience = 2
performance_rating = 4.3
is_elgible_promotion = experience == 3 or performance_rating >= 4
# print(is_elgible_promotion)
# conditional Statements
if is_elgible_promotion:
    print("Employee can be promoted")
else:
    print("employee cannot be promoted")

# endregion
# Membership Operators(in, not in)
# employees=["shree","yasir","Darshan"]
# print("samhita" not in employees)

# # identity operators(is, is not)
# employees=["shree","yasir","Darshan"]
# employees_list=["shree","yasir","Darshan"]
# emp_names=employees

# print(employees is emp_names) # true

# print(employees is employees_list)# false

# print(employees == employees_list)# true

# region if elif else
rating = 3
if rating == 5:
    print("Excellent")
elif rating == 4:
    print("Good")
elif rating == 3:
    print("Average")
else:
    print("improve")
# endregion
# loops
employees = ["shree", "yasir", "Darshan"]
for employee in employees:
    print(employee)

# while loop
score = 1
# basic Syntax
# while score<5:
#     print(score)
#     score+=1

# take user Input for entering the password
# validate password with existing password
# if password is wrong allow him Three chances to enter
# if condition fails print account blocked else print welcome msg
# chances= 3
# while chances>0:
#     password=input("Enter the password:")
#     if(password=="password"):
#         print("Login Success !! welcome")
#         break
#     else:
#         print("wrong password")

#     chances-=1
# print("Account is blocked")

employee_id = int(input("enter the id:"))
if employee_id == 1:
    print(employee_id)
