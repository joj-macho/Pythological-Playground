# Import Modules
import os
import json

# Set Working Directory
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

def main():
    '''This is the main function of the program'''
    
    
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
        '\n8. Exit Contacts')

        response = input('Enter your Choice:\n> ')
        if response == '1':
            print('Add New Contact:\n')
            addContact(contacts)
        elif response == '2':
            print('Update Contact Information:\n')
            updateContact(contacts)
        elif response == '3':
            print('Delete Contact:\n')
            deleteContact(contacts)
        elif response == '4':
            print('Search for Contact:\n')
            searchContact(contacts)
        elif response == '5':
            print('View All Contacts:\n')
            viewContact(contacts)
        elif response == '6':
            print('Save All Contacts:\n')
            saveContacts(contacts)
        elif response == '7':
            print('Load All Contacts:\n')
            contacts = loadContacts()
        elif response == '8':
            print('Bye!')
            break
        else:
            print('Enter a valid number choice between 1 and 8!')

def addContact(contacts):
    '''This function adds a new contact to the given dictionary contacts.'''

    name = input('Enter the Name:\n> ').title()
    phone = input('Enter the Phone Number:\n> ')
    email = input('Enter the email:\n> ')
    # Add the above to the contacts dict
    contacts[name] = {'phone': phone, 'email': email}
    print(f'The name {name} has been added to your contacts.')


def updateContact(contacts):
    '''This function updates the phone number and email of an existing contact in the given dictionary contacts.'''

    name = input('Enter the name of the contact you want to update:\n> ')
    if name in contacts:
        newPhone = input('Enter the New Phone Number:\n> ')
        newEmail = input('Enter the New Email Address:\n> ')
        contacts[name]['phone'] = newPhone
        contacts[name]['email'] = newEmail
        print(f'Contact information of {name} has been updated!')
    else:
        print(f'The name {name} is not in your contacts!')


def deleteContact(contacts):
    '''This function deletes an existing contact from the given dictioncontacts.'''

    name = input('Enter the name of the contact to delete:\n> ').title()
    if name in contacts:
        del contacts[name]
        print(f'Contact for {name} has been deleted!')
    else:
        print(f'The name {name} is not in your contacts')

def searchContact(contacts):
    '''This function searches for an existing contact in the given dictionary contacts.'''
    name = input('Enter the name of the contact you are searching for:\n> ').title()
    # Search for name in a dictionary
    if name in contacts:
        print(f'\n{name} Found in Contacts!\n')
        print(f"Name: {name}:\nPhone: {contacts[name]['phone']}\nEmail: {contacts[name]['email']}\n")
    else:
        print(f'The name {name} is not in your contacts\n')

def viewContact(contacts):
    '''This function prints all contacts in the given dictionary contacts.'''
    if len(contacts) == 0:
        print('Address Book is Empty!\n')
    else:
        for name, contact in contacts.items():
            print(f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}\n")


def saveContacts(contacts):
    '''This function saves the given dictionary contacts to a file called contacts.json.'''
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)
    print('Your Contacts have been saved to contacts.json')

def loadContacts():
    '''This function loads the contents of the file 'contacts.json' into a dictionary and returns it.'''
    global contacts

    try:
        with open('contacts.json', 'r') as f:
            contacts = json.load(f)
        print('Contacts loaded from contacts.json')

    except FileNotFoundError:
        print('No Contact File Found.\nUsing an Empty Address Book instead!')

    return contacts
    


# Run Program
if __name__ == '__main__':
    main()

