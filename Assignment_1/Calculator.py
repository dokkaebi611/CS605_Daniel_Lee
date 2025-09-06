# Author: Daniel Lee
# CSCI605 Assignment #1: Calculator
# Date: 09/05/2025

# Addition
def add(x, y):
    return x + y

# Subtraction
def sub(x, y):
    return x - y

# Multiplication
def mul(x, y):
    return x * y

# Division
def div(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

# Calculate numbers
def calculator():
    while True:
        try:
            num1 = float(input("\nEnter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("\nEnter the operation number: ")

        if choice == "1":
            result = add(num1, num2)
            print("Result: {} + {} = {}\n".format(num1, num2, result))
            break
        elif choice == "2":
            result = sub(num1, num2)
            print("Result: {} - {} = {}\n".format(num1, num2, result))
            break
        elif choice == "3":
            result = mul(num1, num2)
            print("Result: {} * {} = {}\n".format(num1, num2, result))
            break
        elif choice == "4":
            result = div(num1, num2)
            print("Result: {} / {} = {}\n".format(num1, num2, result))
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")

# Calculate again depending on the user's answer
def again():
    while True:
        choice = input("Do you want to perform another calculation? (yes/no): ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            print("\nGoodbye!\n")
            return False
        else:
            print("\nInvalid input. Please type 'yes' or 'no'.")

def main():
    print("\nWelcome to the Simple Calculator!")

    while True:
        calculator()
        if not again():
            break

if __name__ == "__main__":
    main()
