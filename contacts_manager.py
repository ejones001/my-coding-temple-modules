# contacts_manager.py

# Initialize an empty list to store contacts
contacts = []

# Function to add a contact
def add_contact(name, phone_number):
    contacts.append({'name': name, 'phone_number': phone_number})
    print(f"Contact '{name}' with phone number '{phone_number}' added successfully.")

# Function to remove a contact
def remove_contact(name):
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print(f"Contact '{name}' removed successfully.")
            return
    print(f"Contact '{name}' not found.")

# Function to display all contacts
def display_contacts():
    if contacts:
        print("Current contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone Number: {contact['phone_number']}")
    else:
        print("No contacts found.")
