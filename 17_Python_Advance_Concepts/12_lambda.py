
# def is_greater_18(x):
#     if (x>18):
#         return True
#     else:
#         return False

# *** Instead of above function we are using Lambda function here----->
    
a = [2, 7, 25, 56, 34, 17, 1, 5]

# new = list(filter(is_greater_18,a))

new = list(filter(lambda x: (x>18),a))

print(new)