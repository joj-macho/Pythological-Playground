import json
from pathlib import Path
from contact import Contact

# Directory where this script is located
BASE_PATH = Path(__file__).resolve().parent


class ContactManager:
    def __init__(self, file_name='contacts.json'):
        '''Initialize the Contact Manager.'''
        self.file_path = BASE_PATH / file_name  # Full path to json file
        self.contacts = self.load_contacts()

    def load_contacts(self):
        '''Loads contacts from JSON data file.'''
        try:
            with open(self.file_path, 'r') as file:
                content = file.read().strip()
                if not content:
                    return {}
                data = json.loads(content)
                return {contact_id: Contact.from_dict(
                    contact_data) for contact_id, contact_data in data.items()}
        except FileNotFoundError:
            return {}

    def save_contacts(self):
        '''Saves contacts to the JSON file.'''
        with open(self.file_path, 'w') as file:
            data = {contact_id: contact.to_dict()
                    for contact_id, contact in self.contacts.items()}
            json.dump(data, file, indent=4)

    def create_contact(self, contact_id, name, phone, email, address=None):
        '''Creates a new contact.'''
        if contact_id in self.contacts:
            print('\nContact ID already exists.')
            return None

        new_contact = Contact(contact_id, name, phone, email, address)
        self.contacts[contact_id] = new_contact
        self.save_contacts()
        return new_contact

    def get_contacts(self):
        '''Gets all contacts.'''
        return self.contacts

    def read_contact(self, contact_id):
        '''Reads a new contact by ID.'''
        if contact_id in self.contacts:
            return self.contacts.get(contact_id)
        return None

    def update_contact(self, contact_id, name=None,
                       phone=None, email=None, address=None):
        '''Updates an existing contact.'''
        if contact_id in self.contacts:
            contact = self.contacts.get(contact_id)
            if name:
                contact.name = name
            if phone:
                contact.phone = phone
            if email:
                contact.email = email
            if address:
                contact.address = address
            self.save_contacts()
            return True
        return False

    def delete_contact(self, contact_id):
        '''Deletes a contact from contacts.'''
        if contact_id in self.contacts:
            del self.contacts[contact_id]
            self.save_contacts()
            return True
        return False
