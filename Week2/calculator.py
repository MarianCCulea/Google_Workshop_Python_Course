# define a function to validate input
def validate_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")


# get input from user and validate
num1 = validate_input("Enter first number: ")
num2 = validate_input("Enter second number: ")

# get operator from user and validate
valid_operators = ["+", "-", "*", "/"]
while True:
    operator = input("Enter operator (+, -, /, *): ")
    if operator not in valid_operators:
        print("Invalid operator. Please enter a valid operator.")
    else:
        break

# perform calculation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "/":
    result = num1 / num2
elif operator == "*":
    result = num1 * num2

# print result
print("Result: ", result)
