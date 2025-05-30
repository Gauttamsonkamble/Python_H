while True:
    try:
        a = int(input("Enter First Number = "))
        b = int(input("Enter 2nd Number = "))

        print (f"Th addition of this Number is {a / b}")

    except ValueError:
        print("please don't perform bad typecast")

    except ZeroDivisionError:
        print("Hey don't divide by zero")

    except Exception as e:
        print("Some error accured..!",e)