import json
import os

FILENAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return json.load(file)

# Save contacts to file
def save_contacts(contacts):
    with open(FILENAME, "w") as file:
        json.dump(contacts, file, indent=4)
    print("💾 Contacts saved successfully!")

# Add a new contact
def add_contact(contacts):
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print(f"✅ Contact '{name}' added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("📭 No contacts found.")
        return
    print("\n📇 Contact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} | {contact['phone']}")
    print()

# Search contact by name or phone
def search_contact(contacts):
    query = input("Enter name or phone number to search: ").strip().lower()
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    
    if not results:
        print("❌ No matching contacts found.")
        return
    
    print("\n🔍 Search Results:")
    for idx, contact in enumerate(results, start=1):
        print(f"{idx}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")
    print()

# Update a contact
def update_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    
    try:
        idx = int(input("Enter the number of the contact to update: ")) - 1
        if idx < 0 or idx >= len(contacts):
            print("❌ Invalid selection.")
            return
    except ValueError:
        print("❌ Please enter a valid number.")
        return
    
    contact = contacts[idx]
    print(f"Updating '{contact['name']}' (leave blank to keep current value)")
    contact['name'] = input(f"Name [{contact['name']}]: ").strip() or contact['name']
    contact['phone'] = input(f"Phone [{contact['phone']}]: ").strip() or contact['phone']
    contact['email'] = input(f"Email [{contact['email']}]: ").strip() or contact['email']
    contact['address'] = input(f"Address [{contact['address']}]: ").strip() or contact['address']
    
    save_contacts(contacts)
    print(f"✅ Contact '{contact['name']}' updated successfully!")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        idx = int(input("Enter the number of the contact to delete: ")) - 1
        if idx < 0 or idx >= len(contacts):
            print("❌ Invalid selection.")
            return
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    removed = contacts.pop(idx)
    save_contacts(contacts)
    print(f"🗑️ Contact '{removed['name']}' deleted successfully!")

# Main menu
def main():
    contacts = load_contacts()
    while True:
        print("\n📌 Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1-6.")

if __name__ == "__main__":
    main()
