
# Brandon Jun
# Exam 2 Question 1

"""
Load inventory data

Args:
    None

Returns:
    None
"""

def load_inventory():
    try:
        inventory = {}
        with open("inventory.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    title, copies = line.rsplit(": ", 1)
                    inventory[title] = int(copies)
        print("Inventory loaded from file.")
        return inventory
    except FileNotFoundError:
        print("No existing inventory file found. Starting with empty inventory.")
        return {}
    except Exception as e:
        print(f"Error loading inventory: {e}")
        return {}

"""
Save inventory data

Args:
    inventory (dict): The inventory to save

Returns:
    None
"""

def save_inventory(inventory):
    try:
        with open("inventory.txt", "w") as file:
            for title, copies in inventory.items():
                file.write(f"{title}: {copies}\n")
        print("Inventory saved to file.")
    except Exception as e:
        print(f"Error saving inventory: {e}")

"""
Add a book to the inventory

Args:
    inventory (dict): The inventory to add the book to
    
Returns:
    None
"""

def add_book(inventory):
    title = input("Enter the book title: ")

    while True:
        try:
            copies = int(input("How many copies are you adding? "))
            if copies < 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    if title in inventory:
        inventory[title] += copies
        print(f"Added {copies} copies of '{title}'. Total copies now: {inventory[title]}")
    else:
        inventory[title] = copies
        print(f"Added '{title}' to inventory with {copies} copies.")

"""
Find a book in the inventory

Args:
    inventory (dict): The inventory to search in
    
Returns:
    None
"""

def find_book(inventory):
    title = input("Enter the book title to search for: ")

    if title in inventory:
        copies = inventory[title]
        if copies > 0:
            print(f"'{title}' has {copies} copies in stock.")
        else:
            print(f"'{title}' is in the system but has 0 copies in stock.")
    else:
        print("No copies are in stock.")

"""
Remove a book from the inventory

Args:
    inventory (dict): The inventory to remove the book from
    
Returns:
    None
"""

def remove_book(inventory):
    title = input("Enter the book title to remove: ")

    if title not in inventory:
        print("That book is not in the inventory.")
        return

    if inventory[title] == 0:
        print("Cannot remove a copy - there are 0 copies in stock.")
        return

    inventory[title] -= 1
    print(f"Removed 1 copy of '{title}'. Remaining copies: {inventory[title]}")

    if inventory[title] == 0:
        choice = input("No copies remain. Keep book in system with 0 copies (k) or remove from inventory (r)? ")
        if choice.lower() == 'r':
            del inventory[title]
            print(f"'{title}' has been removed from the inventory system.")
        else:
            print(f"'{title}' will remain in the system with 0 copies.")

"""
Display the main menu

Args:
    None
    
Returns:
    None
"""

def display_menu():
    print("\n--- Library Inventory System ---")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Find a book")
    print("4. Display all books")
    print("5. Quit")

"""
Display the current inventory

Args:
    inventory (dict): The inventory to display
    
Returns:
    None
"""

def display_inventory(inventory):
    if not inventory:
        print("No books in inventory.")
        return

    print("\n--- Current Inventory ---")
    for title, copies in sorted(inventory.items()):
        print(f"'{title}': {copies} copies")


def main():
    inventory = load_inventory()

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Please enter a valid number between 1 and 5.")
            continue

        if choice == 1:
            add_book(inventory)
        elif choice == 2:
            remove_book(inventory)
        elif choice == 3:
            find_book(inventory)
        elif choice == 4:
            display_inventory(inventory)
        elif choice == 5:
            save_inventory(inventory)
            print("Thank you for using the Library Inventory System!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()