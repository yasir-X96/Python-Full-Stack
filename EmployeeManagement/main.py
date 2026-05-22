from ems.employeeService import(
    add_employee,update_employee_contact,add_skills,create_emp_profile,delete_all_employees
)
from ems.customExceptions import EmployeeNotFoundException, UnauthorizedAccessException

while True:
    print("----Welcome to Employee Management-----")
    print("1.Add Employee\n2.Update Contact\n3.Add Skills\n4.Create Profile\n5.Delete Employees\n6.Exit")
    choice=int(input("Enter your Choice::"))

    if choice ==1:
        try:
            emp_id=input("Enter Employee Id:")
            name = input("Enter Name:")
            dept = input("enter department:")
            add_employee(emp_id,name,dept)
        except UnauthorizedAccessException as ue:
             print(ue)
          
    elif choice == 2:
        try:
            emp_id=input("Enter Employee Id:")
            email = input("Enter email:")
            phone = input("enter phone num:")
            city=input("Enter City:")
        except EmployeeNotFoundException as e:
             print(e)
        
        update_employee_contact(emp_id=emp_id,email=email,phone=phone,city=city)

        
    elif choice == 3:
        emp_id=input("Enter Employee Id:")
        skills=input("Enter skills seperated by comma:")
        skill_list=skills.split(",")

        add_skills(emp_id,*skill_list)

    elif choice==4:
           emp_id=input("Enter Employee Id:")
           create_emp_profile(emp_id,experience=3,certifications="AI,Python")

    elif choice == 5:
         delete_all_employees()

    # elif choice == 6:
    #      getAllEmployees()

    elif choice == 6:
         print("Thank you")
         break;
    else:
         print("Invalid Choice")

  

# Main Verfication
if __name__== "__main__":
     print("Application Started")



       