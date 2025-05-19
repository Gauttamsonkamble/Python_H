
def add(a,b):
    return a+b

c = add(5,4)

print(c)

def sub(a,b): # a,b are parameter
    c = a-b
    return c

x = sub(5,2) # 5, 2 are arguments
print(x)

# Keyword Argument

def mult(a,b):
    d = a*b
    return d

y = mult(b=9,a=3) # keyword arguments
print(y)