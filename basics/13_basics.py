# Day-6 Practice Task:
#
# Lets make Day-4th Contact Book Persistent
#
# When the program starts, load the data from contacts.json. If the file is not found, start with an empty dictionary using try/except FileNotFoundError
# Keep all the existing options: Add, Search, Delete, and Show.
# Save the data to the file after every add or delete operation.
# Bonus: Validate the phone number using int() and handle any ValueError that occurs.


import json

def save_contacts():
    with open("contacts.json","w") as f:
        json.dump(contacts, f, indent=4)

try:
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = {}

while True:
    try:
        choice = int(input("Enter 1. add contact, 2. search contact, 3.delete contact 4. show contact and 5. Exit: "))
    except ValueError:
        print("Enter Number in Range of 1-5")
        continue
    if choice == 1:
        contact_name = input("Enter your Contact's name: ")

        if contact_name in contacts:
            print(f"{contact_name}: {contacts[contact_name]}")
            user_input = input("Do you want to Update the contact (y/n): ").lower()
            if user_input == "n":
                print("Contact Not Updated")
                continue
            elif user_input != "y":
                print("Enter a valid choice")
                continue
            print("Updating the contact")

        try:
            contact_num = int(input(f"Enter contact number for {contact_name}: "))
        except ValueError:
            print("Enter integer in Contact Number")
        else:
            contacts[contact_name] = contact_num
            save_contacts()
            print("Contact Saved")

    elif choice == 2:
        contact_name = input("Enter the Contact name to search: ")
        if contact_name in contacts:
            print(f"{contact_name}: {contacts[contact_name]}")
        else:
            print(f"Contact name {contact_name} not found")

    elif choice == 3:
        contact_name = input("Enter the contact name to delete: ")
        if contact_name in contacts:
            del contacts[contact_name]
            save_contacts()
            print(f"contact {contact_name} deleted")
        else:
            print(f"Contact name {contact_name} not found")
    elif choice == 4:
        for contact_name,contact_num in contacts.items():
            print(f"{contact_name}  {contact_num}")
    elif choice == 5:
        print("Exiting")
        break
    else:
        print("Please enter a valid choice")
