# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose an operation (1/2/3/4): ")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = multiply(num1, num2)
    elif choice == "4":
        result = divide(num1, num2)
    else:
        print("Invalid operation choice")
        return

    print(f"Result: {num1} {get_operator(choice)} {num2} = {result}")

def get_operator(choice):
    if choice == "1":
        return "+"
    elif choice == "2":
        return "-"
    elif choice == "3":
        return "*"
    elif choice == "4":
        return "/"

if __name__ == "__main__":
    calculator()