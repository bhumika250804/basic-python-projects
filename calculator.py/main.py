try:    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    # o = input("Enter operation :")
    print("we can perform the operation\n + for addition\n- for substraction\n*for multiplication\n/ for the division..")
    print("q for quit")
    # o = input("Enter operation :")
    while True:
        o = input("Enter operation :")
        # a = int(input("Enter first number: "))
        # b = int(input("Enter second number: "))
        # o = input("Enter operation :")
        match o:
            case "+":
                print(f"the addition is: {a + b}")
            case "-":
                print(f"the addition is: {a - b}")
            case "*":
                print(f"the addition is: {a * b}")
            case "/":
                print(f"the addition is: {a / b}")
            case "q":
                print("Existing the calcultor . Goodbye")
except Exception as e:
    print("invalid choices....!",e)

