# Practice Task for Day 5:
#
# Create a Contact Book
#
# Create an empty dictionary named contacts ={}
# Take user input about name and Phone Number
# Add user input into the dictionary
# Give them a menu to : Add contact, Search contact, Delete contact, Show all and Exit
# Let the loop run till user doesn't Exit
# During Search if contact is not found print "Contact not found"

contacts = {

}

while True :
    choice = int (input("Enter number as given for contact 1.Add 2.Search 3.Delete 4.Show all 5.Exit : "))
    if choice == 1:
        Contact_Name = input("Enter the contact name: ")
        Contact_Number = int (input("Enter the contact number: "))
        contacts[Contact_Name]= Contact_Number
    elif choice == 2:
        Search = input("Enter the name of the contact to search: ")
        if Search in contacts:
            print(contacts[Search])
        else:
            print("Contact Not found")

    elif choice == 3:
        Delete = input("Enter the contact name to delete: ")
        if Delete in contacts:
            del contacts[Delete]
            print(f"Contact Name {Delete} Successfully deleted")
        else:
            print("Contact Not found")

    elif choice ==4:
        for key , values in contacts.items() :
            print(key, "->" ,values)
    elif choice == 5:
        break
    else :
        print("Enter a Valid Number")
