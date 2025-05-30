
try:
    a = 44/0

    print(" A = ",a)

except Exception as e:
    print(e)

# It's Excecuted when there is no error in try block
else:
    print("This is a Good")