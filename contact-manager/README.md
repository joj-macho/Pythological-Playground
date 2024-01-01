# Contact Management System

## Description

The Contact Manager is a Python program that allows users to manage a dictionary of contacts, including adding new contacts, updating contacts, searching and displaying existing contacts by name, deleting contacts, saving contacts to json file, and loading contacts from json file, all done using a simple command-line interface.

## How it Works

#### Simple Contact Manager (simple_contact_manager.py)

- The program begins by importing required modules, setting the working directory and creates an empty dictionary called `contacts`. This dictionary will be used to store the contact information for each person.

- The `main()` function begins by displaying a menu of options to the user and prompts them to select one. Based on the user's input, it calls the appropriate function to perform the selected task. The program runs until the user chooses to quit the program.

- The `add_contact()` function allows the user to add a new contact to the address book by entering the contact's name, phone number, and email address. It then adds this information to the `contacts` dictionary.

- The `update_contact()` function allows the user to update the phone number and email address of an existing contact in the address book.

- The `delete_contact()` allows the user to delete an existing contact from the address book.

- The `search_contact()` function allows the user to search for an existing contact in the address book by entering their name. If the contact exists, the program displays their name, phone number, and email address. If contact name not in `contacts`, a response message is displayed.

- The `view_contact()` function allows the user to look up the contact in the `contacts` dictionary and displays their phone number and email address if the name is found.

- The `save_contact()` function saves the current contents of the contacts dictionary to a JSON file called "contacts.json", which is found in the current working directory.

- The `load_contacts()` function loads the contacts from the "contacts.json" file into the program's contacts dictionary. If the file does not exist, it creates an empty dictionary.

#### Object-Oriented Contact Manager (main_contact.py and contact_manager.py)

- The object-oriented version of the Contact Manager uses two files: `main_contact.py` and `contact_manager.py`.

- The `ContactManager` class in `contact_manager.py` encapsulates the functionality of the contact management system. It includes methods for adding, updating, deleting, searching, displaying, saving, and loading contacts.

- The `main_contact.py` file runs the `contact_manager`. It creates an instance of the `ContactManager` class and interacts with it based on user input.

## Program Input & Output

When you run the program `simple_contact_manager.py` or the OOP version with `main_contact.py`, the output will look like this;

```

Welcome to Address Book.

Select a what you want to do between 1 and 8:
1. Add New Contact
2. Update Contact Information
3. Delete Contact
4. Search Contact
5. View All Contact
6. Save Contacts
7. Load Contacts
8. Exit Contacts
Enter your Choice:
> 1
Add New Contact:

Enter the Name:
> Alice
Enter the Phone Number:
> 123456789
Enter the email:
> alice@email.com
The name Alice has been added to your contacts.
Select a what you want to do between 1 and 8:
1. Add New Contact
2. Update Contact Information
3. Delete Contact
4. Search Contact
5. View All Contact
6. Save Contacts
7. Load Contacts
8. Exit Contacts
Enter your Choice:
> 1  
Add New Contact:

Enter the Name:
> Bob
Enter the Phone Number:
> 987654321
Enter the email:
> bob@email.com
The name Bob has been added to your contacts.
Select a what you want to do between 1 and 8:
1. Add New Contact
2. Update Contact Information
3. Delete Contact
4. Search Contact
5. View All Contact
6. Save Contacts
7. Load Contacts
8. Exit Contacts
Enter your Choice:
> 5
View All Contacts:

Name: Alice
Phone: 123456789
Email: alice@email.com

Name: Bob
Phone: 987654321
Email: bob@email.com

Select a what you want to do between 1 and 8:
1. Add New Contact
2. Update Contact Information
3. Delete Contact
4. Search Contact
5. View All Contact
6. Save Contacts
7. Load Contacts
8. Exit Contacts
Enter your Choice:
> 2
Update Contact Information:

Enter the name of the contact you want to update:
> Bob
Enter the updated Phone Number:
> 741852963
Enter the updated Email Address:
> bobby@email.com
Contact information of Bob has been updated!
Select a what you want to do between 1 and 8:
1. Add New Contact
2. Update Contact Information
3. Delete Contact
4. Search Contact
5. View All Contact
6. Save Contacts
7. Load Contacts
8. Exit Contacts
Enter your Choice:
> 3
Delete Contact:

Enter the name of the contact to delete:
> Alise
The name Alise is not in your contacts
Select a what you want to do between 1 and 8:
1. Add New Contact
2. Update Contact Information
3. Delete Contact
4. Search Contact
5. View All Contact
6. Save Contacts
7. Load Contacts
8. Exit Contacts
Enter your Choice:
> 6
Save All Contacts:

Your Contacts have been saved to contacts.json
Select a what you want to do between 1 and 8:
1. Add New Contact
2. Update Contact Information
3. Delete Contact
4. Search Contact
5. View All Contact
6. Save Contacts
7. Load Contacts
8. Exit Contacts
Enter your Choice:
> 5
View All Contacts:

Name: Alice
Phone: 123456789
Email: alice@email.com

Name: Bob
Phone: 741852963
Email: bobby@email.com

Select a what you want to do between 1 and 8:
1. Add New Contact
2. Update Contact Information
3. Delete Contact
4. Search Contact
5. View All Contact
6. Save Contacts
7. Load Contacts
8. Exit Contacts
Enter your Choice:
> 8
Bye!
```
