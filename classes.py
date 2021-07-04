# Simple Class

class car :

    def __init__(self, name, gears, miles):
        self.name = name
        self.gears = gears
        self.miles = miles

    def drive(self,miles):
        self.miles = self.miles + miles
    def shift_gear(self, gears):
        self.gears = gears

car = car ("Tesla",4,100)
print(car.name)
car.name = "Ferrari"
print(car.name)

# Inherited Class

class Employee:
    def __init__(self, name, age, dob, job_description):
        self.name = name
        self.age = age
        self.dob = dob
        self.job_description = job_description

class Manager(Employee):
    def __init__(self,  name, age, dob, job_description, department, employees):
        super().__init__(name, age, dob, job_description)
        self.department = department
        self.employees = employees

class Assistant(Employee):
    def __init__(self, name, age, dob, job_description, managers, working_hours):
        Employee.__init__(self, name, age, dob, job_description)
        self.managers = managers
        self.working_hours = working_hours

tanveer = Manager("Tanveer Ahmed", 23, "03-11-1998",
                  "manages every thing", "Development", 2)
tuqeer = Assistant("Tuqeer Ahmed", 20, "01-05-2002", "Follow manager instruction", "Tanveer Ahmed", 9)

print(tuqeer.managers)
print(tanveer.department)


