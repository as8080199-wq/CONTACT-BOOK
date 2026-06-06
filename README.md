# 📱 Contact Book Application (Python)

A simple, interactive, and terminal-based **Contact Book Application** built using Python. This project demonstrates core programming concepts including dictionaries, loops, conditional logic, and user input handling.

## 🚀 Features
- **Add Contact**: Save a new contact with a name and phone number.
- **View Contacts**: Display all saved contacts in a clean format.
- **Search Contact**: Instantly find a contact's phone number by searching for their name.
- **Interactive Menu**: Easy-to-use CLI (Command Line Interface) menu that runs continuously until you exit.

## 🛠️ Code Snippet Preview
```python
# Core logic used for storing and searching contacts
if choice == "1":
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    contacts[name] = phone
    print("Contact Added!")
