
numbers = [1, 2, 4, 20, 35]

def square(x):
    return x*x

new = list(map(square,numbers))

print(new)