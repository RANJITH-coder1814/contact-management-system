import json
import os

FILE_NAME = "contacts.json"

# Load contacts
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts
def save_contacts(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add contact
def add_contact():
    contacts = load_contacts()
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("✅ Contact added successfully!\n")

# View contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.\n")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print("Name :", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
    print()

# Search contact
def search_contact():
    contacts = load_contacts()
    name = input("Enter name to search: ").lower()

    found = False
    for contact in contacts:
        if contact["name"].lower() == name:
            print("\nContact Found:")
            print(contact)
            found = True
            break

    if not found:
        print("❌ Contact not found.\n")

# Update contact
def update_contact():
    contacts = load_contacts()
    name = input("Enter name to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contact["phone"] = input("Enter new phone: ")
            contact["email"] = input("Enter new email: ")
            save_contacts(contacts)
            print("✅ Contact updated successfully!\n")
            return

    print("❌ Contact not found.\n")

# Delete contact
def delete_contact():
    contacts = load_contacts()
    name = input("Enter name to delete: ").lower()

    new_contacts = [c for c in contacts if c["name"].lower() != name]

    if len(new_contacts) == len(contacts):
        print("❌ Contact not found.\n")
    else:
        save_contacts(new_contacts)
        print("✅ Contact deleted successfully!\n")

# Main menu
def main():
    while True:
        print("===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()
