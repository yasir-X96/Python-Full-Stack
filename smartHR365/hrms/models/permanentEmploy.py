from hrms.models.employ import Employee


class PermanentEmployee(Employee):
    # inherit constructor
    def __init__(self, emp_id,name,department,dateOfJoin,baseSalary,experience):
        super().__init__(emp_id, name,department,dateOfJoin)
        self.baseSalary=baseSalary
        self.experience=experience

    # implement abstract method
    def calculate_salary(self):
        # call base class method
        base=super().calculate_salary()
        annual_bonus=self.baseSalary*0.15 if self.experience>3 else 0
        return base+annual_bonus
    
    def to_dict(self):
        data=super().to_dict()
        data.update({
            "salary":self.baseSalary,
            "experience":self.experience
        })
        return data