
# Brandon Jun
# Lab #5

import random

"""
Asks for the account name.

Returns:
        str: The user's name
        
"""
def get_name():

    name = input("Enter your name: ")
    return name

"""
Asks for account email address.

Returns:
    str: The user's email address
        
"""
def get_email():

    email = input("Enter your Email: ")
    return email

"""
Calculates a random company ID

Args:
    None
    
Returns:
    int: A random 4-digit company ID (1000-9999)
    
"""
def calculate_id():

    company_id = random.randint(1000, 9999)
    return company_id

"""
Gets the account name, email, and generates a company ID

Args:
    None

Returns:
    tuple: (name, email, company_id)

    """
def get_account():
    # Call the three functions and store their return values
    user_name = get_name().capitalize()
    user_email = get_email()
    user_id = calculate_id()

    # Return all three values
    return user_name, user_email, user_id

# Program's User Interface
try:
    print()
    name, email, company_id = get_account()

    print()
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Company ID: {company_id}")

except Exception as e:
    print(f"An error occurred: {e}")