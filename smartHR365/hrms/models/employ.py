

from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self,emp_id,name,department,dateOfJoin):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.dateOfJoin=dateOfJoin
        
    @abstractmethod
    def calculate_salary(self):
        pass

    def to_dict(self):
        return{
            "emp_id":self.emp_id,
            "name":self.name,
            "department":self.department,
            
            "DateOfJoin":self.dateOfJoin
        }
    


    def display_employee(self):
        print(f"Emp Id::{self.emp_id}\nname::{self.name}department::{self.department}\nDOJ::{self.dateOfJoin}")
