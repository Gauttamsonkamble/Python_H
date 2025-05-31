
def is_greater_18(x):
    if (x>18):
        return True
    else:
        return False
    
a = [2, 7, 25, 56, 34, 17, 1, 5]

new = list(filter(is_greater_18,a))

print(new)