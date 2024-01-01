import pytest
import os
from contact_manager import ContactManager

# Pytest for ContactManager
def test_add_contact():
    contact_manager = ContactManager()
    contact_manager.add_contact('Jonathan', '123456789', 'jonathan@example.com')
    assert contact_manager.contacts['Jonathan']['phone'] == '123456789'
    assert contact_manager.contacts['Jonathan']['email'] == 'jonathan@example.com'

def test_display_contact(capsys):
    contact_manager = ContactManager()
    contact_manager.add_contact('Jonathan', '123456789', 'jonathan@example.com')

    # Capture print output
    contact_manager.display_contact('Jonathan')
    captured = capsys.readouterr()

    expected_output = "Name: Jonathan\nPhone: 123456789\nEmail: jonathan@example.com"
    assert captured.out.strip() == expected_output

    # Display for nonexistent contact
    contact_manager.display_contact('Nonexistent')
    captured = capsys.readouterr()
    assert captured.out.strip() == "Contact with name Nonexistent not found."

def test_update_contact():
    contact_manager = ContactManager()
    contact_manager.add_contact('Jonathan', '123456789', 'jonathan@example.com')
    contact_manager.update_contact('Jonathan', '987654321', 'newemail@example.com')
    assert contact_manager.contacts['Jonathan']['phone'] == '987654321'
    assert contact_manager.contacts['Jonathan']['email'] == 'newemail@example.com'

def test_search_contact():
    contact_manager = ContactManager()
    contact_manager.add_contact('Jonathan', '123456789', 'jonathan@example.com')
    assert contact_manager.search_contact('Jonathan') == {'phone': '123456789', 'email': 'jonathan@example.com'}
    assert contact_manager.search_contact('Nonexistent') is None

def test_delete_contact():
    contact_manager = ContactManager()
    contact_manager.add_contact('Jonathan', '123456789', 'jonathan@example.com')
    contact_manager.delete_contact('Jonathan')
    assert 'Jonathan' not in contact_manager.contacts

def test_display_all_contacts(capsys):
    contact_manager = ContactManager()
    contact_manager.add_contact('Jonathan', '123456789', 'jonathan@example.com')
    contact_manager.add_contact('Alice', '987654321', 'alice@example.com')
    contact_manager.add_contact('Bob', '555555555', 'bob@example.com')

    expected_output = """Name: Jonathan
Phone: 123456789
Email: jonathan@example.com

Name: Alice
Phone: 987654321
Email: alice@example.com

Name: Bob
Phone: 555555555
Email: bob@example.com

"""
    contact_manager.display_all_contacts()

    captured = capsys.readouterr()
    assert captured.out == expected_output

def test_save_load_to_file(tmpdir):
    contact_manager = ContactManager()
    contact_manager.add_contact('Jonathan', '123456789', 'jonathan@example.com')
    contact_manager.add_contact('Alice', '987654321', 'alice@example.com')
    contact_manager.save_to_file(os.path.join(tmpdir, 'test_contacts.json'))

    # Load contacts from the file to verify
    loaded_contact_manager = ContactManager()
    loaded_contact_manager.load_from_file(os.path.join(tmpdir, 'test_contacts.json'))

    assert loaded_contact_manager.contacts == contact_manager.contacts