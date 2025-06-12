
try:
    # Example operation, replace with your calculator logic
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    
    print("Select Operation you want to perform")
    print("Press + for addition\n press - for substraction \n press * for multiplication \n press / for division")

    op = input("Enter Operation: ")
    match op:
        case "+":
            print(f"The result is {a+b}")
        case "-":
            print(f"The result is {a-b}")
        case "*":
            print(f"The result is {a*b}")
        case "/":
            print(f"The result is {a/b}")
        case default:
            print("There is Error")
except Exception as e:
    print("Enter a valid value of a and b") 
