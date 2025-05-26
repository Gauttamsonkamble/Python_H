
# Decorator is function that takes a function, it creates a new function inside it's body (wrapper) . Then it returns the new function

def decorator(func):
    def wrapper():
        print("I am ready to execute function...")
        func()
        print("I have executed this function")
    return wrapper

@decorator
def welcome():
    print("DeveloperCorners...!")

welcome()
# f = decorator(welcome)

# f()