
class Employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary = salary

    @property
    def firstName(self):
        name = self.name
        return name
    
    @firstName.setter
    def firstName(self,name):
        self.name = name
        

e = Employee("Gauttam",40000)


print(e.firstName)

e.firstName = "Jack"

print(e.firstName)
        