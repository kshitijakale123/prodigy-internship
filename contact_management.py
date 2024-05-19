import json
import os

# Define the path for the contacts file
contacts_file = "contacts.json"

# Load contacts from the file
def load_contacts():
    if os.path.exists(contacts_file):
        with open(contacts_file, 'r') as file:
            return json.load(file)
    return []

# Save contacts to the file
def save_contacts(contacts):
    with open(contacts_file, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if contacts:
        for idx, contact in enumerate(contacts):
            print(f"{idx + 1}. {contact['name']} - {contact['phone']} - {contact['email']}")
    else:
        print("No contacts found.")

# Edit an existing contact
def edit_contact(contacts):
    view_contacts(contacts)
    try:
        contact_index = int(input("Enter the number of the contact to edit: ")) - 1
        if 0 <= contact_index < len(contacts):
            contact = contacts[contact_index]
            print("Leave the field blank to keep the current value.")
            name = input(f"Enter new name (current: {contact['name']}): ") or contact['name']
            phone = input(f"Enter new phone number (current: {contact['phone']}): ") or contact['phone']
            email = input(f"Enter new email address (current: {contact['email']}): ") or contact['email']
            contacts[contact_index] = {"name": name, "phone": phone, "email": email}
            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        contact_index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= contact_index < len(contacts):
            contacts.pop(contact_index)
            save_contacts(contacts)
            print("Contact deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Display the menu
def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

# Main function to run the contact management system
def main():
    contacts = load_contacts()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
