# Practice Task Day 5:
# Using Functions
# Create a Contact Book
#
# Create an empty dictionary named contacts ={}
# Take user input about name and Phone Number
# Add user input into the dictionary
# Give them a menu to : Add contact, Search contact, Delete contact, Show all and Exit
# Let the loop run till user doesn't Exit
# During Search if contact is not found print "Contact not found"
# For every Operation create an Operation
    #add_contact(book, name, phone)
    #search_contact(book, name)
    #delete_contact(book, name)
    #show_contacts(book)

def add_contact(book, name, phone):
    book[name] = phone

def search_contact(book ,name):
    return book.get(name)

def delete_contact(book , name):
    if name in book:
        del book[name]
        return True
    else:
        return False

def show_contact(book):
    if not book:
        print("Contact Book is empty")
        return
    for name, phone in book.items():
        print(f"{name}, {phone}")

def main():
    book = {

    }
    while True:
        user_input = int( input("Enter 1. add contact, 2. search contact, 3.delete contact 4. show contact and 5. Exit: ") )
        if user_input == 1:
            name = input("Enter the Name to add in the Contact: ")
            phone = input(f"Enter the Number of {name}: ")
            add_contact(book, name, phone)
        elif user_input == 2:
            name = input("Enter the Name to search in the Contact: ")
            phone = search_contact(book, name)
            print(f"{name}:{phone}"if phone else "Contact not found")
        elif user_input == 3:
            name = input("Enter the Name of the Contact to delete: ")
            print("Deleted" if delete_contact(book, name) else "Contact Not found")
        elif user_input == 4:
            show_contact(book)
        elif user_input == 5:
            print("Bye")
            break
        else:
            print("Please Enter a valid number")


main()