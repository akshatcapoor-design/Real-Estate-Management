from connect import create_table
from add import add_property
from view import view_properties
from update import update_property
from delete import delete_property
from search import search_properties


def main():
    create_table()

    while True:
        print("\n=== Real Estate Management System ===")
        print("1. Add Property")
        print("2. View All Properties")
        print("3. Update Property")
        print("4. Delete Property")
        print("5. Search Properties")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_property()
        elif choice == '2':
            view_properties()
        elif choice == '3':
            update_property()
        elif choice == '4':
            delete_property()
        elif choice == '5':
            search_properties()
        elif choice == '6':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
