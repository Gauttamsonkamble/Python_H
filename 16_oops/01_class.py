
# class: class is blueprint or template eg: form for an exam that contains name , age, subject like this.

# object : object is a specific instance that create from class (template). eg: class c:

class Employee:
    company = "DeveloperCorners"

    def get_salary(self): # self is important & mandatory inside the class function parameter because self is a way to reference the object of class being created
        return 32000
    
e = Employee() # e is an object of class Employee is created here.

print(e.get_salary())

print(e.company)

e2 = Employee()

print(e2.get_salary())