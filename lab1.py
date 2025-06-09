
# Brandon Jun
# Lab #1

"""
Definition of the math_operation function

Args:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform ('add' or 'multiply').

Returns:
    float: The result of the operation, or None if the operation is invalid.

"""
def math_operation(num1, num2, operation):

    if operation == 'add':
        return num1 + num2
    elif operation == 'multiply':
        return num1 * num2
    else:
        print(f"Error: '{operation}' is not a valid operation. Please use add or mulitply.")
        return None

"""
Definition of the program's user interface

Args:

Returns:
    float: The result of the operation, or None if the operation is invalid.
    
"""
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add or multiply): ").strip().lower()

    result = math_operation(num1, num2, operation)

    if result is not None:
        print()
        print(f"Result: {result}")

except ValueError:
    print("Error: Please enter valid numbers.")