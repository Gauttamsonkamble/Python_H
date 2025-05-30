


def divide(a,b):
    try:
        c = a/b
        print("C = ",c)
        return c

    except Exception as e:
        print(e)
        return None
    

    # This always executed
    finally:
        print("This always executed")

a = int(input("Enter first Number = "))
b = int(input("Enter 2nd Number = "))

divide(a,b)