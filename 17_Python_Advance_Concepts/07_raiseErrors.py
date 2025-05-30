
a = int(input("Enter First Number = "))
b = int(input("Enter 2nd Number = "))


if b==0:
    raise ValueError("Don't Divide by zero")

print (f"Th addition of this Number is {a / b}")