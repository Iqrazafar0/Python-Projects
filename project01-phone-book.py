                                    # phone-book

# define the phone-book dictionary
phone_book = {}

# function to add in contact
def add_contact(name, number):
    if name in phone_book:
        print(f"Contact {name} already exit.")
    else:
        phone_book[name] = number
        print(f"{name} is succesfully added.")

# function to view the contact
def view_contact(name):
    if name in phone_book:
        print(f"{name} : {phone_book[name]}")
    else:
        print(f"Contact {name} does't exist.")

#function to update a contact
def update_contact(name, number):
    if name in phone_book:
        phone_book[name] = number
        print(f"Contact {name} updated succesfully!")
    else:
        print(f"Contact {name} is not exist.")

#function to delete contact

def del_contact(name):
    if name in phone_book:
        del phone_book[name]
        print(f"Contact {name} deleted succesfully!")
    else:
        print(f"Contact {name} is not exist.")

#function to display all contacts
def display_contacts():
    if phone_book:
        print("phone-book:")
        for name, number  in phone_book.items():
            print(f"{name} : {number}")
    else:
        print("phone-book is empty!")

#function to show the menu
def show_menu():
    print("\nphone-book menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All ContactS")
    print("Exit Phone-Book")

#Main program loop

while True:
    show_menu()
    choice = input("Enter your choice(1-6): ")

    if choice == '1':
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        add_contact(name, number)
    elif choice == '2':
        name = input("Enter name to view: ")
        view_contact(name)
    elif choice == '3':
        name = input("Enter name to update: ")
        number = input("Enter phone number to update: ")
        update_contact(name, number)
    elif choice == '4':
        name = input("Enter name to delete: ")
        del_contact(name)
    elif choice == '5':
        display_contacts()
    elif choice == '6':
        print("Exit phone-book")
        break
    else:
        print("Invalid choice, please enter a number between 1 and 6")