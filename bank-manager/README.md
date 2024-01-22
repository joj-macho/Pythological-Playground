# Bank Account Manager

## Description

The Bank Account Manager (aka ATM Simulator) program is a Python program that emulates an Automated Teller Machine (ATM) experience. This program provides users with a convenient way to interact with their bank accounts by offering functionalities such as balance inquiries, withdrawals, deposits, and transfers.

## How it Works

- The program uses a class-based approach with the `BankAccount` class (in `bank_account_manager.py`) serving as the core structure to manage user accounts. Each `BankAccount` instance represents a distinct user account and has attributes like the account holder's name, pin number, and account balance.

- The `main()` function (in `main_bank.py`) runs the `bank_account_manager`. This function provides a user interface for managing a bank account, allowing users to perform transactions like deposit, withdraw, and transfer. It interacts with the `BankAccount` class to execute these transactions based on user input.

- The program initiates by displaying a welcome screen using the `display_centered` function and introducing a brief delay using the `time.sleep` function for a more 'realistic' user experience.

- On startup, the user is prompted to enter their name, pin number, and initial balance to create their account. These details are used to initialize an instance of the `BankAccount` class.

- The main loop presents users with a menu containing five options: Balance Inquiry, Withdrawal, Deposit, Transfer, and Exit. Users select an option by entering the corresponding number. The program processes the chosen operation by calling the appropriate methods on the user's account instance.

- During interactions, the program provides informative messages to guide users through each step of the operation. It also introduces a short delay using `time.sleep` to simulate processing time, enhancing the realism of the ATM experience..

- In case of withdrawals, deposits, and transfers, the program validates user inputs using the `validate_amount` function, ensuring that the provided amounts are valid positive numbers. If invalid inputs are detected, the program notifies the user accordingly.

## Program Input & Output

When you run the program `main_bank.py`, the output will look like this;

```

****************************************

             ATM SIMULATOR
             
****************************************
Intitializing ATM ...

Enter your name: Joj
Enter your pin number: 1234
Enter your initial balance: 100

****************************************

                  MENU
                  
****************************************
1. Balance Inquiry
2. Withdrawal
3. Deposit
4. Transfer
5. Exit

Enter your choice: 1

****************************************

            BALANCE INQUIRY
            
****************************************
Processing ...
Your current balance is: $100.0 


****************************************

                  MENU
                  
****************************************
1. Balance Inquiry
2. Withdrawal
3. Deposit
4. Transfer
5. Exit

Enter your choice: 2

****************************************

               WITHDRAWAL
               
****************************************
Enter withdrawal amount: 75
Processing ...
Withdrew $75.0.
Current balance: $25.0


****************************************

                  MENU
                  
****************************************
1. Balance Inquiry
2. Withdrawal
3. Deposit
4. Transfer
5. Exit

Enter your choice: 3

****************************************

                DEPOSIT
                
****************************************
Enter deposit amount: 200
Processing ...
Deposited $200.0.
Current balance: $225.0


****************************************

                  MENU
                  
****************************************
1. Balance Inquiry
2. Withdrawal
3. Deposit
4. Transfer
5. Exit

Enter your choice: 4

****************************************

                TRANSFER
                
****************************************
Enter recipient's name: Ana
Enter transfer amount: 220
Processing ...
Transferred $220.0 to Ana.
Current balance: $5.0

****************************************

                  MENU
                  
****************************************
1. Balance Inquiry
2. Withdrawal
3. Deposit
4. Transfer
5. Exit

Enter your choice: 5

Thank you for using the ATM. Goodbye!
```