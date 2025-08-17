contacts = {}
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts saved.")
    else:
        for name, details in contacts.items():
            print("\nName:", name)
            print("Phone:", details["phone"])
            print("Email:", details["email"])
            print("Address:", details["address"])

def search_contact():
    search_name = input("Enter name to search: ")
    if search_name in contacts:
        print("Contact found:")
        print("Phone:", contacts[search_name]["phone"])
        print("Email:", contacts[search_name]["email"])
        print("Address:", contacts[search_name]["address"])
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name of contact to update: ")
    if name in contacts:
        print("What do you want to update?")
        print("1. Phone\n2. Email\n3. Address")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            contacts[name]["phone"] = input("Enter new phone number: ")
        elif choice == '2':
            contacts[name]["email"] = input("Enter new email: ")
        elif choice == '3':
            contacts[name]["address"] = input("Enter new address: ")
        else:
            print("Invalid option.")
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name of contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

while True:
    print("\n==== Contact Book Menu ====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    user_choice = input("Choose an option (1-6): ")

    if user_choice == '1':
        add_contact()
    elif user_choice == '2':
        view_contacts()
    elif user_choice == '3':
        search_contact()
    elif user_choice == '4':
        update_contact()
    elif user_choice == '5':
        delete_contact()
    elif user_choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
