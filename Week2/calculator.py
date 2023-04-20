# Calculator using functions

valid_operators = ["+", "-", "*", "/"]


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def main():
    # First number input
    num1 = float(input("Enter first number: "))

    while True:
        # Input the operator with constant check if it's valid
        while True:
            operator = input("Enter operator (+, -, /, *): ")
            if operator == "x":
                break
            if operator not in valid_operators:
                print("Invalid operator. Please enter a valid operator.")
            else:
                break

        # Input the second number with constant check if it's valid using try except
        while True:
            num2 = input("Enter second number: ")
            try:
                num2 = float(num2)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        if operator == "+":
            num1 = add(num1, num2)
            print("Result: ", num1)
        elif operator == "-":
            num1 = subtract(num1, num2)
            print("Result: ", num1)
        elif operator == "*":
            num1 = multiply(num1, num2)
            print("Result: ", num1)
        elif operator == "/":
            num1 = divide(num1, num2)
            print("Result: ", num1)
        else:
            print("Invalid operator")


if __name__ == "__main__":
    main()
