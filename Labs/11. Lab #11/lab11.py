
# Brandon Jun
# Lab #11

from Contact import Contact
import pickle

"""
To load contacts from a file

Args:
    None
    
Return:
    dict: Dictionary of Contact objects loaded from the file, or an empty dictionary if the file does not exist 
"""

def load_contacts():
   try:
      with open("mydata.dat", 'rb') as file:
         return pickle.load(file)
   except FileNotFoundError:
      return {}

"""
To save the contacts to a file

Args:
    contacts (dict): Dictionary of Contact objects to save
    
Return:
    None
"""

def save_contacts(contacts):
   with open("mydata.dat", 'wb') as file:
      pickle.dump(contacts, file)

"""
To add a contact

Args:
    contacts (dict): Dictionary to modify with Contact objects
    
Return:
    None
"""

def add(contacts):
   name = input("Name: ")
   if name in contacts:
      print("An entry already exists for that contact!")
      return

   email = input("Email: ")
   entry = Contact(name, email)

   while True:
      next_num = input("Enter a phone number (or -1 to stop): ")
      if next_num == "-1":
         break
      entry.add_number(next_num)

   contacts[name] = entry

"""
To look up a contact

Args:
    contacts (dict): Dictionary of Contact objects to search
    
Return:
    None
"""

def look_up(contacts):
   name = input("Enter a name: ")
   if name in contacts:
      print(contacts[name])
   else:
      print("There is no contact with that name")

"""
To delete a contact

Args:
    contacts (dict): Dictionary of Contact objects to modify
    
Return:
    None
"""

def delete(contacts):
   name = input("Enter a name to remove from your list of contacts: ")
   if name in contacts:
      print("Are you sure you want to delete the following contact? ")
      print(contacts[name])
      choice = input("'y' or 'n': ")
      if choice == 'y':
         del contacts[name]
      else:
         print("Contact saved in dictionary")
   else:
      print("There is no contact with that name")

"""
To edit a pre-existing contact

Args:
    contacts (dict): Dictionary of Contact objects to modify
    
Return:
    None
"""

def edit_contact(contacts):

    name = input("Enter the name of the contact you want to edit: ")

    if name not in contacts:
        print("There is no contact with that name")
        return

    contact = contacts[name]

    while True:
        print("\nWhat would you like to do?")
        print("1) Remove a phone number")
        print("2) Add a phone number")
        print("3) Change email address")
        print("4) Change name")
        print("5) Stop editing")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":

            if not contact.phone_numbers:
                print("This contact has no phone numbers to remove.")
            else:
                print("Current phone numbers:")
                for i, num in enumerate(contact.phone_numbers, 1):
                    print(f"{i}) {num}")

                phone_to_remove = input("Enter the phone number to remove: ")
                if phone_to_remove in contact.phone_numbers:
                    contact.remove_number(phone_to_remove)
                    print("Phone number removed.")
                else:
                    print("That phone number is not in the contact.")

        elif choice == "2":

            new_phone = input("Enter the phone number to add: ")
            contact.add_number(new_phone)
            if new_phone not in contact.phone_numbers:
                print("Phone number added.")

        elif choice == "3":

            new_email = input("Enter the new email address: ")
            contact.email = new_email
            print("Email address updated.")

        elif choice == "4":

            new_name = input("Enter the new name: ")
            if new_name in contacts and new_name != name:
                print("A contact with that name already exists!")

            else:
                contact.name = new_name
                contacts[new_name] = contacts.pop(name)
                name = new_name
                print("Name updated.")

        elif choice == "5":
            print("Finished editing contact.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

try:
   contacts = load_contacts()

   while True:
      choice = int(input("\nEnter 1) to add a contact, 2) to lookup a contact, "
                  "3) to delete a contact, 4) to edit a contact, 5) to quit: "))
      if choice == 1:
         add(contacts)
      elif choice == 2:
         look_up(contacts)
      elif choice == 3:
         delete(contacts)
      elif choice == 5:
         break

   save_contacts(contacts)

except Exception as e:
    print(f"An error occurred: {e}")