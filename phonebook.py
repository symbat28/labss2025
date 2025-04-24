# phonebook.py
from insert_console import insert_from_console
from insert_csv import insert_from_csv
from search_data import search_data
from  update_data import update_data
from delete_data import delete_data

while True:
    print("\n Phonebook Menu")
    print("1. Add Contact (Console)")
    print("2. Import Contacts (CSV File)")
    print("3. Search Contacts")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Please select an option (1-6): ")

    if choice == '1':
        insert_from_console()
    elif choice == '2':
        filename = input("Enter CSV file name: ")
        insert_from_csv(filename)
    elif choice == '3':
        search_data()
    elif choice == '4':
        update_data()
    elif choice == '5':
        delete_data()
    elif choice == '6':
        print(" Goodbye!")
        break
    else:
        print(" Please enter a number between 1 and 6.")
