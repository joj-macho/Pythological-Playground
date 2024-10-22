# Contact Management

## Description

The Contact Manager program is a simple tool for managing a list of contacts. It allows users to create, view, update, and delete contacts.

## How it Works

- Create a new contact using a unique contact ID and contact information.
- You can view contact information, update a contact, and delete a acontact.

Contact data is loaded and saved to JSON file.

## Running the Program

```bash
# Navigate to the project directory
cd contact-manager/

# Run the main script
python3 main.py
```

## Program Input & Output

When you run the program `main.py`, the output will look like this;

```

---------------------------Contact Management System---------------------------

1: Create a New Contact
2: View All Contacts
3: View Contact by ID
4: Update an Existing Contact
5: Delete a Contact
0: Exit

Enter your choice:
> 1

Creating a New Contact:
Enter Contact ID: 001
Enter Name: Alice
Enter Phone Number: 547899632
Enter Email Address: al@email.com
Enter Address (Optional): 

Contact ID already exists.

Failed to Create Contact. A Contact with this ID Already Exists.

Press Enter to return to the main menu...

---------------------------Contact Management System---------------------------

1: Create a New Contact
2: View All Contacts
3: View Contact by ID
4: Update an Existing Contact
5: Delete a Contact
0: Exit

Enter your choice:
> 2

All Contacts:

Contact ID: 001
Name: Alison
Phone: 123456789
Email: alice@email.com
Address: 220 Alice Street
------------------------------

Contact ID: 002
Name: Robert
Phone: 222222222
Email: bob@email.com
Address: 220 Bob Lane
------------------------------

Contact ID: 003
Name: Charli
Phone: 5966214478
Email: charlie@email.com
Address: 
------------------------------

Press Enter to return to the main menu...

---------------------------Contact Management System---------------------------

1: Create a New Contact
2: View All Contacts
3: View Contact by ID
4: Update an Existing Contact
5: Delete a Contact
0: Exit

Enter your choice:
> 3

View Contact by ID:
Enter Contact ID: 002

Contact ID: 002
Name: Robert
Phone: 222222222
Email: bob@email.com
Address: 220 Bob Lane

Press Enter to return to the main menu...

---------------------------Contact Management System---------------------------

1: Create a New Contact
2: View All Contacts
3: View Contact by ID
4: Update an Existing Contact
5: Delete a Contact
0: Exit

Enter your choice:
> 4

Update a Contact:
Enter Contact ID to Update: 002

Leave fields blank to keep current values.
Enter New Name (Current: Robert): Carol 
Enter New Phone (Current: 222222222): 89654125
Enter New Email (Current: bob@email.com): carol@email.com
Enter New Address (Current: 220 Bob Lane): 

Contact Updated Successfully!

Press Enter to return to the main menu...

---------------------------Contact Management System---------------------------

1: Create a New Contact
2: View All Contacts
3: View Contact by ID
4: Update an Existing Contact
5: Delete a Contact
0: Exit

Enter your choice:
> 2

All Contacts:

Contact ID: 001
Name: Alison
Phone: 123456789
Email: alice@email.com
Address: 220 Alice Street
------------------------------

Contact ID: 002
Name: Carol
Phone: 89654125
Email: carol@email.com
Address: 220 Bob Lane
------------------------------

Contact ID: 003
Name: Charli
Phone: 5966214478
Email: charlie@email.com
Address: 
------------------------------

Press Enter to return to the main menu...

---------------------------Contact Management System---------------------------

1: Create a New Contact
2: View All Contacts
3: View Contact by ID
4: Update an Existing Contact
5: Delete a Contact
0: Exit

Enter your choice:
> 5

Delete a Contact:
Enter Contact ID to Delete: 003

Contact Deleted Successfully!

Press Enter to return to the main menu...

---------------------------Contact Management System---------------------------

1: Create a New Contact
2: View All Contacts
3: View Contact by ID
4: Update an Existing Contact
5: Delete a Contact
0: Exit

Enter your choice:
> 2

All Contacts:

Contact ID: 001
Name: Alison
Phone: 123456789
Email: alice@email.com
Address: 220 Alice Street
------------------------------

Contact ID: 002
Name: Carol
Phone: 89654125
Email: carol@email.com
Address: 220 Bob Lane
------------------------------

Press Enter to return to the main menu...

---------------------------Contact Management System---------------------------

1: Create a New Contact
2: View All Contacts
3: View Contact by ID
4: Update an Existing Contact
5: Delete a Contact
0: Exit

Enter your choice:
> 0
Exiting Contacts... Bye!
```
