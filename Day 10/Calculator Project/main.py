from art import logo

def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def print_operations():
    for key in operations:
        print(key)

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
print(logo)
number1 = float(input("What's the first number? "))
print_operations()
user_operation = input("Pick an operation: ")
number2 = float(input("What's the next number? "))
continue_ = True
while continue_:
    result = operations[user_operation](number1, number2)
    print(f"{number1} {user_operation} {number2} = {result}")
    user_choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    if user_choice == "y":
        number1 = result
        print_operations()
        user_operation = input("Pick an operation: ")
        number2 = float(input("What's the next number? "))
    else:
        print("\n" * 20)
        print(logo)
        number1 = float(input("What's the first number? "))
        print_operations()
        user_operation = input("Pick an operation: ")
        number2 = float(input("What's the next number? "))