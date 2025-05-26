
def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(6)
def welcome(a):
    print(f"DeveloperCorners...! {a}")

welcome("Gauttam SK")