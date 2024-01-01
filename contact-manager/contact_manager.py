import json

class ContactManager:
    def __init__(self):
        '''Initialize the ContactManager with an empty contacts dictionary.'''
        self.contacts = {}

    def add_contact(self, name, phone, email):
        '''Add a new contact to the contacts dictionary.'''
        self.contacts[name] = {'phone': phone, 'email': email}

    def display_contact(self, name):
        '''Display contact information for a given name.'''
        contact = self.contacts.get(name)
        if contact:
            print(f'Name: {name}\nPhone: {contact["phone"]}\nEmail: {contact["email"]}\n')
        else:
            print(f'Contact with name {name} not found.\n')

    def update_contact(self, name, new_phone, new_email):
        '''Update contact information for a given name.'''
        if name in self.contacts:
            self.contacts[name]['phone']= new_phone
            self.contacts[name]['email']= new_email
            print(f'Contact information of {name} has been updated!\n')
        else:
            print(f'The name {name} is not in your contacts!\n')

    def search_contact(self, name):
        '''Search for a contact by name.'''
        return self.contacts.get(name)

    def delete_contact(self, name):
        '''Delete a contact by name.'''
        if name in self.contacts:
            del self.contacts[name]
            print(f'Contact {name} has been deleted\n')
        else:
            print(f'The name {name} is not in your contacts!\n')

    def display_all_contacts(self):
        '''Display information for all contacts.'''
        if len(self.contacts) == 0:
            print('Address Book is Empty!\n')
        else:
            for name, contact_info in self.contacts.items():
                print(f'Name: {name}\nPhone: {contact_info["phone"]}\nEmail: {contact_info["email"]}\n')

    def save_to_file(self, filename):
        '''Save contacts to a JSON file.'''
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)
        print(f'Your Contacts have been saved to {filename}')

    def load_from_file(self, filename):
        '''Load contacts from a JSON file.'''
        with open(filename, 'r') as file:
            self.contacts = json.load(file)
        print(f'Contacts have been loaded from {filename}')