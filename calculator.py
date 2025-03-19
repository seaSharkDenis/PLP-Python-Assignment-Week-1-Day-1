while True:
    try:
        print("Welcome to the calculator program!!")
        print("You can stop the application by simply entering 'stop'.")
        print()
        operationOption = input("Enter the operation you would like to perform: (+ - * / % or 'stop' to exit): ")
        if operationOption.lower() == "stop":
            print("Exiting calculator program. Goodbye!")
            break

        operandOne = int(input("Enter first number: "))
        operandTwo = int(input("Enter second number: "))

        if operationOption == "+":
            print(f"The sum of {operandOne} and {operandTwo} is {operandOne + operandTwo}")
        elif operationOption == "-":
            print(f"The difference between {operandOne} and {operandTwo} is {operandOne - operandTwo}")
        elif operationOption == "*":
            print(f"Multiplying {operandOne} and {operandTwo} gives us {operandOne * operandTwo}")
        elif operationOption == "/":
            print(f"Dividing {operandOne} with {operandTwo} gives us {operandOne / operandTwo}")
        elif operationOption == "%":
            print(f"The modulus of {operandOne} and {operandTwo} is {operandOne % operandTwo}")
        else:
            print("Wrong operation sign. Please try again.")
    except ZeroDivisionError:
        print("You cannot divide a number by 0. Please try again.")
    except ValueError:
        print("You have entered an invalid value. Please enter a number and try again.")
