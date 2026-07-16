import calculator_operations as cf

# Declaring a variable
first_num = input("Enter the first number: ")
second_num = 0
last_calculation = 0
flag = "Y"

# Defining a dictionary to map operations to their corresponding functions
operation = {
    "+": cf.addition,
    "-": cf.subtraction,
    "*": cf.multiplication,
    "/": cf.division,
}

# Taking user input for the operation and the second number
user_operation = input("Enter the operation (+/-/*/): ")
second_num = input("Enter the second number: ")

while flag == "Y" or flag == "y":
    # Performing the selected operation based on user input
    if user_operation == "+":
        result = operation["+"](int(first_num), int(second_num))
        print(f"{first_num} {user_operation} {second_num} = {result}")
    elif user_operation == "-":
        result = operation["-"](int(first_num), int(second_num))
        print(f"{first_num} {user_operation} {second_num} = {result}")
    elif user_operation == "*":
        result = operation["*"](int(first_num), int(second_num))
        print(f"{first_num} {user_operation} {second_num} = {result}")
    elif user_operation == "/":
        result = operation["/"](int(first_num), int(second_num))
        print(f"{first_num} {user_operation} {second_num} = {result}")
    else:
        print("Invalid operation. Please choose a valid operation (+/-/*/).")

    # Asking the user if they want to perform another calculation
    flag = input(f"Do you want to perform another calculation? with {result}  (Y/N): ")
    if flag == "Y" or flag == "y":
        first_num = result
        second_num = input("Enter the second number: ")
        user_operation = input("Enter the operation (+/-/*/): ")

print("Thank you for using the calculator. Goodbye!")
