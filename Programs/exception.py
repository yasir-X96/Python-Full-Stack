# error,Bug,Exception(Runtime Error)
# try--risky code, Except--Print the Exceptions
#region Basics
# try:
#     num= int(input("Enter Number::"))
#     print(num)
# except:
#     print("Invalid Input")
# print("Welcome")
#endregion

employees={
    101:{"name":"samhita","salary":50000},
    102:{"name":"shashank","salary":45000},
    103:{"name":"Bharat","salary":60000},
}
try:
    bonus="2000"
    emp_id=int(input("Enter your Id::"))
    print("EmployeeId::",emp_id)
    print(f"Salary::{employees[emp_id]["salary"]}")
    # print(f"Salary::{employees[emp_id]["salary"]}"+{bonus})
    print("salary::",employees[emp_id]["salary"]+ bonus)
except ValueError:
    print("Employee Id Must be Numeric")

except KeyError:
    print("Employee Id is not present!!")

except TypeError:
    print("Cannot add string to int")