class Contact:
    def __init__(self, contact_id, name, phone, email, address=None):
        '''Initialize a new contact.'''
        self.contact_id = contact_id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        '''Converts contact information to dict.'''
        return {
            'contact_id': self.contact_id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address
        }

    @staticmethod
    def from_dict(data):
        '''Creates a Contact instance from a dictionary.'''
        contact = Contact(
            data['contact_id'], data['name'], data['phone'], data['email']
        )
        contact.contact_id = data['contact_id']
        contact.name = data['name']
        contact.phone = data['phone']
        contact.email = data['email']
        contact.address = data['address']
        return contact


# Sanity check
if __name__ == '__main__':
    # create a new contact
    contact_1 = Contact(
        '001',
        'Alice',
        '0123456789',
        'alice@email.com',
        '220 Alice')
    print(f'Contact created for {contact_1.name}.\nContact Information:')
    print(f'Contact ID: {contact_1.contact_id}')
    print(f'Contact Phone: {contact_1.phone}')
    print(f'Contact Email: {contact_1.email}')
    print(f'{contact_1.name}\'s Adress: {contact_1.address}')

    print(contact_1.to_dict())
