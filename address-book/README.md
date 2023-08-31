# Simple Address Book

## Description

The Simple Address Address Book is a simple Python program that allows users to manage a dictionary of contacts, including adding new contacts, updating contacts, searching and displaying existing contacts by name, deleting contacts, saving contacts to json file, and loading contacts from json file, all done using a simple command-line interface.


## How it Works

- The program begins by importing required modules, setting the working directory and creates an empty dictionary called <code>contacts</code>. This dictionary will be used to store the contact information for each person.

- The <code>main()</code> function begins by displaying a menu of options to the user and prompts them to select one. Based on the user's input, it calls the appropriate function to perform the selected task. The program runs until the user chooses to quit the program.

- Response 1 - "Add New Contact": The <code>add_contact()</code> function allows the user to add a new contact to the address book by entering the contact's name, phone number, and email address. It then adds this information to the <code>contacts</code> dictionary.

- Response 2 - "Update Contact Information": The <code>update_contact()</code> function allows the user to update the phone number and email address of an existing contact in the address book.

- Response 3 - "Delete Contact": The <code>delete_contact()</code> allows the user to delete an EXISTING contact from the address book.

- Response 4 - "Search Contact": The <code>search_contact()</code> function allows the user to search for an existing contact in the address book by entering their name. If the contact exists, the program displays their name, phone number, and email address. If contact name not in <code>contacts</code>, a response message is displayed.

- Response 5 - "View All Contact": The <code>view_contact()</code> function allows the user to look up the contact in the <code>contacts</code> dictionary and displays their phone number and email address if the name is found.

- Response 6 - "Save Contacts" option: The <code>save_contact()</code> function saves the current contents of the contacts dictionary to a JSON file called "contacts.json", which is found in the current working directory.

- Response 7 - "Load Contacts": The <code>load_contacts()</code> function loads the contacts from the "contacts.json" file into the program's contacts dictionary. If the file does not exist, it creates an empty dictionary.

- Response 8 - "Exit Contacts": The program exits when the user selects this option


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
