contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print()

def search_contact():
    name = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"Found: {contact}")
            found = True
            break
    if not found:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter name to delete: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted!\n")
            return
    print("Contact not found.\n")

def update_contact():
    name = input("Enter name to update: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = input("Enter new phone: ")
            contact["email"] = input("Enter new email: ")
            print("Contact updated!\n")
            return
    print("Contact not found.\n")

def menu():
    while True:
        print("===== Contact Manager =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            update_contact()
        elif choice == '6':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run the Contact Manager
menu()
