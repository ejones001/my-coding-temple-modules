# main.py

import contacts_manager

# Function to interact with the contact manager
def contact_manager():
    while True:
        print("\nContact List Manager")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            contacts_manager.add_contact(name, phone_number)
        elif choice == '2':
            name = input("Enter contact name to remove: ")
            contacts_manager.remove_contact(name)
        elif choice == '3':
            contacts_manager.display_contacts()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    contact_manager()
