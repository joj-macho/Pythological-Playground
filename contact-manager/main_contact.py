import os
from contact_manager import ContactManager

def main():
    '''Main function to run the Contact Management System.'''
    # Change the current working directory to the script's directory
    path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(path)
    contact_manager = ContactManager()

    while True:
        print('\nContact Management System\n')
        print('1. Add Contact')
        print('2. Update Contact')
        print('3. Search Contact')
        print('4. Delete Contact')
        print('5. Display All Contacts')
        print('6. Save Contacts to File')
        print('7. Load Contacts from File')
        print('8. Exit')

        choice = input('Enter your choice (1-8):> ')

        if choice == '1':
            try:
                name = input('Enter name:> ').title()
                phone = input('Enter phone:> ')
                email = input('Enter email:> ')
                contact_manager.add_contact(name, phone, email)
                print(f'Contact for {name} successfully added.')
            except Exception as e:
                print(f'Error: {e}')
            
        elif choice == '2':
            try:
                name = input('Enter name to update:> ')
                new_phone = input('Enter new phone:> ')
                new_email = input('Enter new email:> ')
                contact_manager.update_contact(name, new_phone, new_email)
            except Exception as e:
                print(f'Error: {e}')

        elif choice == '3':
            name = input('Enter name to search:> ')
            result = contact_manager.search_contact(name)
            if result:
                contact_manager.display_contact(name)
            else:
                print('Contact not found.')

        elif choice == '4':
            try:
                name = input('Enter name to delete:> ')
                contact_manager.delete_contact(name)
            except Exception as e:
                print(f'Error: {e}')

        elif choice == '5':
            contact_manager.display_all_contacts()

        elif choice == '6':
            try:
                filename = input('Enter filename to save contacts:> ')
                contact_manager.save_to_file(filename)
            except Exception as e:
                print(f'Error: {e}')

        elif choice == '7':
            try:
                filename = input('Enter filename to load contacts from:> ')
                if os.path.exists(filename):
                    contact_manager.load_from_file(filename)
                else:
                    print(f'File {filename} does not exist.')
            except Exception as e:
                print(f'Error: {e}')

        elif choice == '8':
            print('Exiting program.')
            break

        else:
            print('Invalid choice. Please enter a number between 1 and 8.')

if __name__ == '__main__':
    main()