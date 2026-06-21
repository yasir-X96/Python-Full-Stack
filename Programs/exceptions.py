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
    bonus=2000
    emp_id=int(input("Enter your Id::"))
    print("EmployeeId::",emp_id)
    print(f"Salary::{employees[emp_id]["salary"]}")
    # print(f"Salary::{employees[emp_id]["salary"]}"+{bonus})
    print("salary::",employees[emp_id]["salary"]+ bonus)
except ValueError:
    print("Employee Id Must be Numeric")

# except KeyError:
#     print("Employee Id is not present!!")

except TypeError:
    print("Cannot add string to int")

except Exception as e:
    print("somethimg went wrong",e)

finally:
    print("Employee added")

# num=2000
# result=num/0

#Custom Exceptions

class EmployeeNotFoundException(Exception):
    pass


try:
    emp_id=int(input("Enter your ID"))
    if emp_id not in employees:
        raise EmployeeNotFoundException("Employee not exists")
    print("employee Id ",emp_id)
except EmployeeNotFoundException as e:
    print(e)