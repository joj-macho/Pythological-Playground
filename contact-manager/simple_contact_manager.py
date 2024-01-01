import os
import json

# Change the current working directory to the script's directory
PATH = os.path.dirname(os.path.realpath(__file__))
os.chdir(PATH)
    
def main():
    '''Main function to run the contact manager'''
    print('\nWelcome to Address Book.\n')

    # Store Contacts in a dictionary
    contacts = {}

    # Menu Screen
    while True:
        print('Select a what you want to do between 1 and 8:'
        '\n1. Add New Contact'
        '\n2. Update Contact Information'
        '\n3. Delete Contact'
        '\n4. Search Contact'
        '\n5. View All Contact'
        '\n6. Save Contacts'
        '\n7. Load Contacts'
        '\n8. Exit')

        choice = input('Enter your Choice:\n> ')

        if choice == '1':
            print('Add New Contact:\n')
            add_contact(contacts)
        elif choice == '2':
            print('Update Contact Information:\n')
            update_contact(contacts)
        elif choice == '3':
            print('Delete Contact:\n')
            delete_contact(contacts)
        elif choice == '4':
            print('Search for Contact:\n')
            search_contact(contacts)
        elif choice == '5':
            print('View All Contacts:\n')
            view_contact(contacts)
        elif choice == '6':
            print('Save All Contacts:\n')
            save_contact(contacts)
        elif choice == '7':
            print('Load All Contacts:\n')
            contacts = load_contacts()
        elif choice == '8':
            print('Bye!')
            break
        else:
            print('Enter a valid number choice between 1 and 8!')

def add_contact(contacts):
    '''Add a new contact to the contacts dictionary.'''
    name = input('Enter the Name:\n> ').title()
    phone = input('Enter the Phone Number:\n> ')
    email = input('Enter the email:\n> ')

    contacts[name] = {'phone': phone, 'email': email}
    print(f'The name {name} has been added to your contacts.')

def update_contact(contacts):
    '''Update the phone number and email of an existing contact for a name.'''
    name = input('Enter the name of the contact you want to update:\n> ')

    if name in contacts:
        new_phone_num = input('Enter the updated Phone Number:\n> ')
        new_email = input('Enter the updated Email Address:\n> ')
        contacts[name]['phone'] = new_phone_num
        contacts[name]['email'] = new_email
        print(f'Contact information of {name} has been updated!')
    else:
        print(f'The name {name} is not in your contacts!')

def delete_contact(contacts):
    '''Delete an existing contact from the contact dictionary.'''
    name = input('Enter the name of the contact to delete:\n> ').title()
    
    if name in contacts:
        del contacts[name]
        print(f'Contact for {name} has been deleted!')
    else:
        print(f'The name {name} is not in your contacts')

def search_contact(contacts):
    '''Search for an existing contact in the given dictionary contacts.'''

    name = input('Enter the name of the contact you are searching for:\n> ').title()
    if name in contacts:
        print(f'\n{name} Found in Contacts!\n')
        print(f"Name: {name}:\nPhone: {contacts[name]['phone']}\nEmail: {contacts[name]['email']}\n")
    else:
        print(f'The name {name} is not in your contacts\n')

def view_contact(contacts):
    '''Display all contacts in the given dictionary contacts.'''
    if len(contacts) == 0:
        print('Address Book is Empty!\n')
    else:
        for name, contact in contacts.items():
            print(f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}\n")

def save_contact(contacts):
    '''Save the given dictionary contacts to contacts.json file.'''
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)
    print('Your Contacts have been saved to contacts.json')

def load_contacts():
    '''Load the contents of the file 'contacts.json' into a dictionary and returns it.'''
    global contacts

    try:
        with open('contacts.json', 'r') as f:
            contacts = json.load(f)
        print('Contacts loaded from contacts.json')
    except FileNotFoundError:
        print('No Contact File Found.\nUsing an Empty Address Book instead!')

    return contacts
    
if __name__ == '__main__':
    main()