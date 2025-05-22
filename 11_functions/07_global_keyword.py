
def sum(a,b):
    print("Hey I'm adding number")
    c = a+b

    global x  # global keyword is use to change or modify global variable
    x = 11

    print(x)
    return c

x = 10
print(sum(5,7))

print(x)