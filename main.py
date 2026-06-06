contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
        print("Contact Added!")

    elif choice == "2":
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "3":
        name = input("Enter Name to Search: ")
        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact Not Found")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")