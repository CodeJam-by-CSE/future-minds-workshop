from operations import add, subtract, multiply, divide
from utils import get_number, get_operation

def main():
    print("Simple Calculator")
    
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    operation = get_operation()

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        print("Invalid operation")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
