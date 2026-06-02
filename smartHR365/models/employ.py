class Employee:
    def __init__(self,emp_id,name,department,salary,dateOfJoin):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.salary=salary
        self.dateOfJoin=dateOfJoin

    def to_dict(self):
        return{
            "emp_id":self.emp_id,
            "name":self.name,
            "department":self.department,
            "salary":self.salary,
            "DateOfJoin":self.dateOfJoin
        }
    


    def display_employee(self):
        print(f"Emp Id::{self.emp_id}\nname::{self.name}department::{self.department}\nsalary::{self.salary}\nDOJ::{self.dateOfJoin}")
