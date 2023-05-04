# Simple Address Book

## Description

The Simple Address Address Book is a simple Python program that allows users to manage a list of contacts, including adding new contacts, searching for existing contacts by name, and deleting contacts from the list using a simple command-line interface.


## How it Works

- The program begins by importing required modules, setting the working directory and creates an empty dictionary called <code>contacts</code>. This dictionary will be used to store the contact information for each person.

- The <code>main()</code> function runs the main loop of the program. The function begins by displaying a menu of options to the user and prompts them to select one. Based on the user's input, it calls the appropriate function to perform the selected task. The program runs until the user chooses to quit the program.

- When the user selects the "Add New Contact" option, the <code>addContact()</code> function is called. This function allows the user to add a new contact to the address book by entering the contact's name, phone number, and email address. It then adds this information to the <code>contacts</code> dictionary.

- When the user selects the "Update Contact Information" option, the <code>updateContact()</code> function is called. The <code>updateContact()</code> function allows the user to update the phone number and email address of an existing contact in the address book.

- When the user selects the "Delete Contact" option, the <code>deleteContact()</code> function is called. This function allows the user to delete an existing contact from the address book.

- When the user selects the "Search Contact" option, the <code>searchContact()</code> function is called. The <code>searchContact()</code> function allows the user to search for an existing contact in the address book by entering their name. If the contact exists, the program displays their name, phone number, and email address.

- When the user selects the "View All Contact" option, the <code>viewContact()</code> function is called and then looks up the contact in the <code>contacts</code> dictionary and displays their phone number and email address.

- When the user selects the "Save Contacts" option, the <code>saveContacts()</code> function is called. The <code>saveContacts()</code> function saves the current contents of the contacts dictionary to a JSON file called "contacts.json".


- When the user selects the "Load Contacts" option, the <code>loadContacts()</code> function loads the contacts from the "contacts.json" file into the program's contacts dictionary. If the file does not exist, it creates an empty dictionary.

- When the user selects the "Exit Contacts" option, the program exits.


## Program Input & Output

When you run the program `simple_address_book.py`, the output will look like this;

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
> adam
Enter the Phone Number:
> 123456789
Enter the email:
> adam@email.com
The name Adam has been added to your contacts.
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
> bob
Enter the Phone Number:
> 987654213
Enter the email:
> bob@ddmail.com
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

Name: Adam
Phone: 123456789
Email: adam@email.com

Name: Bob
Phone: 987654213
Email: bob@ddmail.com

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
Enter the New Phone Number:
> 0001112223
Enter the New Email Address:
> bob@fmail.com
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
> 5
View All Contacts:

Name: Adam
Phone: 123456789
Email: adam@email.com

Name: Bob
Phone: 0001112223
Email: bob@fmail.com

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
> 8
Bye!
```
