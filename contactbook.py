# Contact Management System

# Dictionary to store contacts
contacts = {}

# Function to add a contact
def add_contact():
    name = input("Enter name: ").strip().title()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    if name in contacts:
        print("Contact already exists. Use update option to modify the contact.")
    else:
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact for {name} added successfully.")

# Function to view all contacts
def view_contacts():
    if contacts:
        print("\n--- Contact List ---")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")
    else:
        print("No contacts found.")

# Function to search for a contact
def search_contact():
    search_term = input("Enter name or phone number to search: ").strip().title()
    found_contacts = [name for name in contacts if search_term in name or search_term in contacts[name]['phone']]

    if found_contacts:
        print("\n--- Search Results ---")
        for name in found_contacts:
            details = contacts[name]
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
    else:
        print("No contact found.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ").strip().title()
    
    if name in contacts:
        print("Updating contact for:", name)
        phone = input("Enter new phone number: ").strip()
        email = input("Enter new email: ").strip()
        address = input("Enter new address: ").strip()

        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact for {name} updated successfully.")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip().title()
    
    if name in contacts:
        confirm = input(f"Are you sure you want to delete the contact for {name}? (yes/no): ").strip().lower()
        if confirm == 'yes':
            del contacts[name]
            print(f"Contact for {name} deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("Contact not found.")

# Main function to interact with the user
def contact_manager():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "main":
    contact_manager()