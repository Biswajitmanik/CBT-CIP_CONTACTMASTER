class ContactMaster:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number, email=None):
        if len(name) > 50:
            print("Error: Name cannot exceed 50 characters.")
            return
        if len(number) < 10:
            print("Error: Number must be at least 10 characters long.")
            return
        if email and len(email) < 20:
            print("Error: Email must be at least 20 characters long if provided.")
            return

        contact_key = name if name else "Unnamed Contact"
        if contact_key in self.contacts:
            print(f"Contact '{contact_key}' already exists.")
        else:
            self.contacts[contact_key] = {'number': number, 'email': email}
            print(f"Contact '{contact_key}' added successfully.")

    def delete_contact(self, name):
        contact_key = name if name else "Unnamed Contact"
        if contact_key in self.contacts:
            del self.contacts[contact_key]
            print(f"Contact '{contact_key}' deleted successfully.")
        else:
            print(f"Contact '{contact_key}' not found.")

    def search_contact(self, search_term):
        results = {name: info for name, info in self.contacts.items() if search_term.lower() in name.lower()}

        if results:
            print(f"\nFound {len(results)} contact(s) matching '{search_term}':")
            for name, info in results.items():
                print(f"Name: {name}\nNumber: {info['number']}\nEmail: {info['email'] or 'N/A'}\n")
        else:
            print(f"No contacts found matching '{search_term}'.")

    def show_all_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("All Contacts:")
            for name, info in self.contacts.items():
                print(f"Name: {name}\nNumber: {info['number']}\nEmail: {info['email'] or 'N/A'}\n")


def main():
    cm = ContactMaster()

    while True:
        print("\nContactMaster Menu")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Show All Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter full name (max 50 characters, optional): ")
            number = input("Enter contact number (minimum 10 characters): ")
            email = input("Enter contact email (optional, minimum 20 characters if provided): ")
            email = email if email.strip() else None
            cm.add_contact(name, number, email)
        elif choice == '2':
            name = input("Enter exact contact name to delete: ")
            cm.delete_contact(name)
        elif choice == '3':
            search_term = input("Enter full or partial name to search: ")
            cm.search_contact(search_term)
        elif choice == '4':
            cm.show_all_contacts()
        elif choice == '5':
            print("Exiting ContactMaster. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
