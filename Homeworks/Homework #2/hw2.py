
# Brandon Jun
# Homework #2

import math

"""
Calculate the minimum number of packages needed.

Args:
    total_items (int): Total number of items needed
    items_per_package (int): Number of items per package

Returns:
    int: Minimum number of packages needed

"""


def calculate_packages_needed(total_items, items_per_package):
    return math.ceil(total_items / items_per_package)


"""
Calculate the number of items that will be left over.

Args:
    total_items (int): Total number of items needed
    items_per_package (int): Number of items per package

Returns:
    int: Number of leftover items

"""


def calculate_leftovers(total_items, items_per_package):
    packages_needed = calculate_packages_needed(total_items, items_per_package)
    total_items_purchased = packages_needed * items_per_package
    leftovers = total_items_purchased - total_items
    return leftovers


"""
Get the number of people and hot dogs per person from the user.

Args:
    None

Returns:
    tuple: (number_of_people, hotdogs_per_person)
"""


def get_user_input():
    while True:
        try:
            people = int(input("Enter the number of people attending the cookout: "))
            if people > 0:
                break
            else:
                print("Please enter a positive number of people.")
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        try:
            dogs_per_person = int(input("Enter the number of hot dogs each person will eat: "))
            if dogs_per_person > 0:
                break
            else:
                print("Please enter a positive number of hot dogs.")
        except ValueError:
            print("Please enter a valid integer.")

    return people, dogs_per_person


"""
Display the cookout calculation results.

Args:
    people (int): Number of people attending
    dogs_per_person (int): Hot dogs per person
    total_dogs (int): Total hot dogs needed
    dog_packages (int): Hot dog packages needed
    bun_packages (int): Bun packages needed
    dog_leftovers (int): Leftover hot dogs
    bun_leftovers (int): Leftover buns

Returns:
    None

"""


def display_results(people, dogs_per_person, total_dogs, dog_packages, bun_packages,
                    dog_leftovers, bun_leftovers):
    print("\n" + "=" * 50)
    print("        HOT DOG COOKOUT CALCULATOR")
    print("=" * 50)
    print(f"People attending:                    {people}")
    print(f"Hot dogs per person:                 {dogs_per_person}")
    print(f"Total hot dogs needed:               {total_dogs}")
    print()
    print("PACKAGE REQUIREMENTS:")
    print(f"Hot dog packages needed:             {dog_packages}")
    print(f"Hot dog bun packages needed:         {bun_packages}")
    print()
    print("LEFTOVERS:")
    print(f"Hot dogs left over:                  {dog_leftovers}")
    print(f"Hot dog buns left over:              {bun_leftovers}")
    print("=" * 50)


# Program's User Interface
try:

    # Constants
    HOTDOGS_PER_PACKAGE = 10
    BUNS_PER_PACKAGE = 8

    print("=== HOT DOG COOKOUT CALCULATOR ===")
    print("Hot dogs come in packages of 10")
    print("Hot dog buns come in packages of 8")
    print()

    # Get user input
    people, dogs_per_person = get_user_input()

    # Calculate total hot dogs needed
    total_hotdogs = people * dogs_per_person

    # Calculate packages needed
    hotdog_packages = calculate_packages_needed(total_hotdogs, HOTDOGS_PER_PACKAGE)
    bun_packages = calculate_packages_needed(total_hotdogs, BUNS_PER_PACKAGE)

    # Calculate leftovers
    hotdog_leftovers = calculate_leftovers(total_hotdogs, HOTDOGS_PER_PACKAGE)
    bun_leftovers = calculate_leftovers(total_hotdogs, BUNS_PER_PACKAGE)

    # Display results
    display_results(people, dogs_per_person, total_hotdogs, hotdog_packages,
                    bun_packages, hotdog_leftovers, bun_leftovers)

except Exception as e:
    print(f"An error occurred: {e}")
    print("Please try again.")