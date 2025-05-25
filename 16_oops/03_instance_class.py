
class Employee:

    company = "DeveloperCorners"

    def __init__(self,salary,name,age):
        self.salary = salary
        self.name = name
        self.age = age

    def getinfo(self):
        print(self.salary)

    def getname(self):
        return self.name


e = Employee(40000, "Gauttam", 29)
e.getinfo()
print(e.getname())

print(e.company)
print(Employee.company) # class attribute can call by direct class name

print(dir(e)) # object introspection