def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_operation():
    while True:
        op = input("Enter operation (+, -, *, /): ")
        if op in ["+", "-", "*", "/"]:
            return op
        print("Invalid operation! Please enter one of (+, -, *, /).")
