from contact_manager import ContactManager


def main():
    '''Run the Contact Management System.'''
    contact_manager = ContactManager('test_contacts.json')

    while True:
        choice = display_menu()
        if choice is None:
            print('Exiting Contacts... Bye!')
            break

        if choice == '1':
            create_contact(contact_manager)
        elif choice == '2':
            view_all_contacts(contact_manager)
        elif choice == '3':
            view_contact(contact_manager)
        elif choice == '4':
            update_contact(contact_manager)
        elif choice == '5':
            delete_contact(contact_manager)
        else:
            print('\nInvalid choice. Please try again.')
            input('\nPress Enter to return to the main menu...')


def display_menu():
    '''Displays the main menu options.'''
    print()
    print('Contact Management System'.center(79, '-'))
    print()
    options = {
        '1': 'Create a New Contact',
        '2': 'View All Contacts',
        '3': 'View Contact by ID',
        '4': 'Update an Existing Contact',
        '5': 'Delete a Contact',
        '0': 'Exit'
    }
    for key, description in options.items():
        print(f'{key}: {description}')

    print('\nEnter your choice:')
    choice = get_user_choice('> ', options.keys())
    return choice


def get_user_choice(prompt, options):
    '''Prompts to select option from options.'''
    while True:
        choice = input(prompt)
        if choice == '0':
            return None
        if choice in options:
            return choice
        print(f'Invalid choice! Select from {", ".join(options)}\n')


def get_contact_details():
    '''Prompts the user to enter contact details.'''
    contact_id = input('Enter Contact ID: ').strip()
    name = input('Enter Name: ').strip()
    phone = input('Enter Phone Number: ').strip()
    email = input('Enter Email Address: ').strip()
    address = input('Enter Address (Optional): ').strip()
    return contact_id, name, phone, email, address


def create_contact(contact_manager):
    '''Handles the creation of a new contact.'''
    print('\nCreating a New Contact:')
    contact_id, name, phone, email, address = get_contact_details()
    new_contact = contact_manager.create_contact(
        contact_id, name, phone, email, address)
    if new_contact:
        print('\nContact Created Successfully!')
    else:
        print('\nFailed to Create Contact. '
              'A Contact with this ID Already Exists.')
    input('\nPress Enter to return to the main menu...')


def view_all_contacts(contact_manager):
    '''Displays all contacts.'''
    print('\nAll Contacts:')
    contacts = contact_manager.get_contacts()
    if contacts:
        for contact_id, contact in contacts.items():
            print(f'\nContact ID: {contact_id}')
            print(f'Name: {contact.name}')
            print(f'Phone: {contact.phone}')
            print(f'Email: {contact.email}')
            print(f'Address: {contact.address}')
            print('-' * 30)
    else:
        print('\nNo contacts found.')
    input('\nPress Enter to return to the main menu...')


def view_contact(contact_manager):
    '''Displays a specific contact by ID.'''
    print('\nView Contact by ID:')
    contact_id = input('Enter Contact ID: ').strip()
    contact = contact_manager.read_contact(contact_id)
    if contact:
        print(f'\nContact ID: {contact.contact_id}')
        print(f'Name: {contact.name}')
        print(f'Phone: {contact.phone}')
        print(f'Email: {contact.email}')
        print(f'Address: {contact.address}')
    else:
        print('\nContact Not Found.')
    input('\nPress Enter to return to the main menu...')


def update_contact(contact_manager):
    '''Handles updating an existing contact.'''
    print('\nUpdate a Contact:')
    contact_id = input('Enter Contact ID to Update: ').strip()
    contact = contact_manager.read_contact(contact_id)
    if contact:
        print('\nLeave fields blank to keep current values.')
        name = input(f'Enter New Name (Current: {contact.name}): ').strip()
        phone = input(f'Enter New Phone (Current: {contact.phone}): ').strip()
        email = input(f'Enter New Email (Current: {contact.email}): ').strip()
        address = input(
            f'Enter New Address (Current: {contact.address}): ').strip()

        updated = contact_manager.update_contact(
            contact_id, name or None, phone or None,
            email or None, address or None)
        if updated:
            print('\nContact Updated Successfully!')
        else:
            print('\nFailed to Update Contact.')
    else:
        print('\nContact Not Found.')
    input('\nPress Enter to return to the main menu...')


def delete_contact(contact_manager):
    '''Handles deleting a contact.'''
    print('\nDelete a Contact:')
    contact_id = input('Enter Contact ID to Delete: ').strip()
    deleted = contact_manager.delete_contact(contact_id)
    if deleted:
        print('\nContact Deleted Successfully!')
    else:
        print('\nFailed to Delete Contact. Contact Not Found.')
    input('\nPress Enter to return to the main menu...')


if __name__ == '__main__':
    main()
