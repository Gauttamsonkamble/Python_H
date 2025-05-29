
class Employee():
    def __init__(self,name,salary):
        company = "DeveloperCorners"
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name} and salary is {self.salary}"
    
    def __repr__(self):
        return f"name: {self.name}\nSalary: {self.salary}"
    
    def __len__(self):
        return len(self.name)
    
e = Employee("Gauttam",50000)

print(e.name,e.salary)
print(str(e))

print(len(e))

print(repr(e))

