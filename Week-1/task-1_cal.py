
def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid operation choice.")


calculator()
