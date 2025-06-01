
def sum(*args): # "args" collect all the values in "tuple". and pass to sum function
    total = 0
    for item in args:
        total += item
    return total

print(sum(4, 6, 8, 10))