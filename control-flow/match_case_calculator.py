# Ask for first number
num1 = float(input("Enter the first number: "))

# Ask for second number
num2 = float(input("Enter the second number: "))

# Ask what operation to do
operation = input("Choose the operation (+, -, *, /): ")

# Use match case to choose what to do
match operation:
    case "+":
        print(f"The result is {num1 + num2}")
    case "-":
        print(f"The result is {num1 - num2}")
    case "*":
        print(f"The result is {num1 * num2}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"The result is {num1 / num2}")
    case _:
        print("Invalid operation.")
