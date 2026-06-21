#region class and objects basic
# class Employee:
#     #Attributes
#     employee_id = ""
#     name = ""
#     department= ""

#     # employee_id = "Emp500"
#     # name = "Siddhartha"
#     # department= "HR"
#     #method
#     # def greet(defaultarg,name):
#     #     print("Hello::"+name)

#     def greet(self,name):
#         print("Hello::"+name)

#     def getUserDetail(self):
#         print("these are details")

# employee1= Employee()
# employee1.employee_id="Emp101"
# employee1.name="shree"
# employee1.department="Training"
# print(f"employee Id is::{employee1.employee_id}\t Name::{employee1.name}\tDept::{employee1.department}")

# employee2 = Employee()
# employee2.employee_id = "Emp102"
# employee2.name = "Yasir"
# employee2.department = "IT"
# print(
#     f"employee Id is::{employee2.employee_id}\t Name::{employee2.name}\tDept::{employee2.department}")

# employee3= Employee()
# print(f"EmpId::{employee3.employee_id}")

# employee1.greet("shree")
# employee1.getUserDetail()
#endregion
#region different method types
# class Employee:
#     # #name=""
#     #Attribute
#     company_Name="Abc Pvt Ltd"
#     #constructor
#     # gets called automatically  when an object is created 
#     def __init__(self,emp_id,emp_name):
#         self.emp_id=emp_id
#         self.emp_name=emp_name
#     # Instance methods
#     def getEmployeeDetails(self):
#         print(f"Emp Id::{self.emp_id}\tEmpName::{self.emp_name}")
#     # @classmethod
#     # def change_companyTitile(cls,newCompany):
#     #    cls.company_Name=newCompany
#     @staticmethod
#     def calculate_YearlyBonus(salary):
#         return salary*0.10


# employee1=Employee("Emp100","shree")
# employee1.getEmployeeDetails()
# #employee1.company_Name="SmartHr Systems"
# print(employee1.company_Name)#

# employee2=Employee("Emp101","Rohan")
# employee2.getEmployeeDetails()

# #employee2.change_companyTitile("SmartHr Systems")
# # Employee.change_companyTitile("SmartHR Systems")
# # print(f"Changed Name is::{Employee.company_Name}")
# #bonus=employee2.calculate_YearlyBonus(50000)
# bonus=Employee.calculate_YearlyBonus(55000)
# bonus1 =employee2.calculate_YearlyBonus(55000)
# print(f"bonus is::{bonus1}")
# #employee1.name="shree"
#endregion

# class Employee:
#     #constructor
#     def __init__(self, emp_id, emp_name,salary):
#                 self.emp_id=emp_id
#                 self.emp_name=emp_name
#                 self.salary=salary

# #     def display_info(self):
# #            print(f"Name::{self.emp_name}Salary::{self.salary}")


# # Child class or derived Class
# class Manager(Employee):
#        def __init__(self,emp_id,emp_name,salary,department):
#               #Call the Base Class Constructor
#               super().__init__(emp_id,emp_name,salary)
#               self.department=department
        
# def display_info(self):
#     super().display_info()
#     print(f"Department::{self.department}")

# manager=Manager(101,"Shree",50000,"IT")
# print(manager.emp_name)
    
from abc import ABC, abstractmethod
import array
    # String Representation of an object
#     def __str__(self):
#             return f"Id::{self.emp_id}\tName::{self.emp_name}"

#     def __len__(self):
#             return len(self.emp_name)
    
#     def __add__(self,other):
#             return self.salary+other.salary
    
    

# employee1=Employee("Emp101","Shree",50000)
# employee2=Employee("Emp102","Darshan",60000)
# print(employee1+employee2)
# print(employee2)
# print(len(employee2))

# class Calculator:
#     def __call__(self, n1, n2):
#         return n1+n2
    
# #object of Calculator class
# calc=Calculator()
# #__call__  will allow object to behave like function
# print(calc(10,20))

# #__getitem__

# class User:
#        def __init__(self):
#               self.data={
#                      "name":"shree",
#                      "salary":5000
#                 }
#        def __getitem__(self, key):
#                return self.data[key]



# user1=User()
# print(user1["name"])
# class User:
#        def __init__(self,name):
#               self.name=name




# class Student(User):
#        def __init__(self,name,degree):
#               super().__init__(name)
#               self.degree=degree

# student1=Student("Shree","BE")

# print(f"Name::{student1.name}Degree::{student1.degree}")

# # MultiLevel inheritance
# class PremiumStudent(Student):
#        pass
# class Employee:
#        def login(self):
#               print("employee Loggedin")

# class Manager(Employee):
#        def manageProject():
#            print("Managing project")


# class HRManager(Manager):
#        def shortList_candidates():
#               print("Shortlist")

# hrManager=HRManager()
# hrManager.login()
# hrManager.manageProject()
# hrManager.shortList_candidates()

#Polymorphism
# poly ---many forms 



# num1=10
# num2=20
# print(num1+num2)

# firstName="shree"
# lastName="vidhya"
# print(firstName+lastName)

# #functions
# print(len(firstName))
# print(len(["item1","item2","item3"]))

# class Employee:
#     def getInfo(self):
#         print("This is Employee Class")
    

# class PermanentEmployee(Employee):
#     def getInfo(self):
#         print("This is Permanent Employee class")

# #Method OverRiding, Dynamic Polymorphism, RunTime Polymorphism
# pe=PermanentEmployee()
# pe.getInfo()
# emp=Employee()
# emp.getInfo()

# abstarction
# showing only necessary details and hiding the internal details

# class Employee(ABC):
#     #concrete methods
#     def getEmployee(self):
#         print("concrete Method")
    
#     #abstract Method
#     @abstractmethod
#     def calculate_salary(self):
#         pass

# # create An object of Employee
# emp=Employee()
# emp.getEmployee

# Encapsulation
# wrapping data(attributes) and methods in a single class
# to restrict access and to validate data before assigning values

# class Employee:
#     def __init__(self,salary):
#         self._salary=salary #private data
#     @property
#     def salary(self):
#         return self._salary
    
#     @salary.setter
#     def salary(self,value):
#         if value>0:
#             self._salary=value
#         else:
#             raise ValueError("salary must be positive")


# #region gettter and setter Methods
#     # def set_salary(self,salary):
#     #     if salary>0:
#     #         self.__salary=salary
#     #     else:
#     #         print("salary must be positive")

#     # def get_salary(self):
#     #     return self.__salary
#     #endregion

# #

# emp1=Employee(50000)
# emp1.salary=-40000
# print(emp1.salary)
# # emp1.__salary=-3000# invalid data
# emp1.set_salary(-2000)
# print(emp1.get_salary())
# # print(emp1.__salary)

# public ----salary
# private----->__salary
#protected---> _salary

# class Employee(ABC):
#     def __init__(self,empid,name,dept):
#         self.__empid=empid
#         self._name = name
#         self._dept=dept
        
        
#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self,value):
#         if len(value)<5:
#             raise ValueError("Name must be atleast 5 characters")
#         self._name=value
    
#     @abstractmethod
#     def calculate_salary(self):
#         pass



#     #Inheritance
# class PermananentEmployee(Employee):
#         def __init__(self,empid,name,dept,baseSalary,experience):
#             super().__init__(empid,name,dept)
#             self.baseSalary=baseSalary
#             self.experience=experience

#         def calculate_salary(self):
#             bonus=self.experience*2000
#             return self.baseSalary+bonus


# emp1=PermananentEmployee(100,"shree","IT",50000,5)
# print(emp1.calculate_salary())


# class Sample:
#     __age=10


# class Sample1:
#     pass
 

# sampleobj=Sample()
# # sampleobj.__age="100"
# print (sampleobj.__age)

# sample1Obj=Sample1()
# sample1Obj.age=100
# print(sample1Obj.age)

scores=array.array('i',[90,20,40])
scores.append(60)
print(scores)
print(scores[1])

