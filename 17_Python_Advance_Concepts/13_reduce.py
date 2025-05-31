from functools import reduce

numbers = [2, 5, 8, 4, 9]
#         [7, 8, 4, 9]
#         [15, 4, 9]
#         [19, 9]
#         [28]


def sum(a,b):
    return a+b

c = reduce(sum,numbers)

print(c)
