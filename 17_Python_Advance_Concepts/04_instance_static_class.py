
class Employee:
    company = "DeveloperCorners"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    #**** This is instance method (default) ****
    def getdetails(self):
        empDetails = f"The name is {self.name} and salary is {self.salary}"
        print(empDetails)

    # *** This is static method ***
    @staticmethod
    def sum(a, b):
        return a+b
    

    # *** This is class method ***
    @classmethod
    def getCompanyName(cls):
        print(cls.company)

    @classmethod
    def changeCompany(cls,NewCompany):
        cls.company= NewCompany


e1 = Employee("Gauttam",40000)
e2 = Employee("Robert",30000)

print(Employee.company)

e1.getdetails()
e2.getdetails()

print(e1.sum(10,20))
e1.getCompanyName()

e1.changeCompany("Apple")

print(Employee.company)

