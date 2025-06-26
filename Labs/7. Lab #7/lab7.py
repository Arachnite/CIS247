
# Brandon Jun
# Lab #7

import sys

def load_employees():
    """Load employee data from file and return dictionaries for lookups"""
    id_to_name = {}
    name_to_id = {}

    try:
        with open('employees.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(' ', 1)  # Split into ID and full name
                    emp_id = int(parts[0])
                    full_name = parts[1]

                    # Store in both dictionaries for efficient lookup
                    id_to_name[emp_id] = full_name
                    name_to_id[full_name] = emp_id

    except FileNotFoundError:
        print("Error: employees.txt file not found!")
        return {}, {}
    except Exception as e:
        print(f"Error reading employee data: {e}")
        return {}, {}

    return id_to_name, name_to_id


def lookup_employee(emp_id, id_to_name):
    """Look up employee name by ID number"""
    if emp_id in id_to_name:
        return id_to_name[emp_id]
    else:
        return "Employee not found"


def lookup_id(first_name, last_name, name_to_id):
    """Look up employee ID by first and last name"""
    # Check for exact match with first and last name
    for full_name in name_to_id:
        name_parts = full_name.split()
        if len(name_parts) >= 2:
            # Compare first and last names (ignoring middle names)
            if (name_parts[0].lower() == first_name.lower() and
                    name_parts[-1].lower() == last_name.lower()):
                return name_to_id[full_name]

    return "ID not found"

def lookup_id_two(full_name, name_to_id):
    """Look up employee ID by full name"""
    # Check for exact match with full name (case-insensitive)
    for name in name_to_id:
        if name.lower() == full_name.lower():
            return name_to_id[name]

    return "ID not found"

try:
    print("Employee Lookup System by Brandon Jun")
    print("=" * 30)

    # Load employee data
    id_to_name, name_to_id = load_employees()

    if not id_to_name:
        print("No employee data loaded. Exiting.")
        sys.exit()

    while True:
        print("\nOptions:")
        print("1. Look up name by ID number")
        print("2. Look up ID by name")
        print("3. Quit")

        choice = input("\nEnter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            try:
                emp_id = int(input("Enter employee ID number: "))
                result = lookup_employee(emp_id, id_to_name)
                print(result)
            except ValueError:
                print("Error: Please enter a valid integer for the ID number.")

        elif choice == '2':
            first_name = input("Enter first name: ").strip()
            last_name = input("Enter last name: ").strip()
            result = lookup_id(first_name, last_name, name_to_id)
            print(result)

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

        while True:
            print("\nOptions:")
            print("1. Look up name by ID number")
            print("2. Look up ID by full name")
            print("3. Quit")

            choice = input("\nEnter your choice (1, 2, or 3): ").strip()

            if choice == '1':
                try:
                    emp_id = int(input("Enter employee ID number: "))
                    result = lookup_employee(emp_id, id_to_name)
                    print(result)
                except ValueError:
                    print("Error: Please enter a valid integer for the ID number.")

            elif choice == '2':
                try:
                    full_name = input("Enter full name (first, middle, and last name): ").strip()
                    result = lookup_id_two(full_name, name_to_id)
                    print(result)
                except ValueError:
                    print("Error: Please enter a valid name format.")

            elif choice == '3':
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")