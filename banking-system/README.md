# Banking System

## Description

The "Banking System" program simulates a banking system where users can manage multiple bank accounts using an account number and PIN code. Users can perform balance inquiries, deposits, withdrawals, and transfers between existing accounts.

## How It Works

- Create multiple bank accounts using a unique account nunmber and PIN code.
- Each account is managed with a unique account number/ID for access. Access accounts by entering the account number and the corresponding PIN code.

- After creating an account and logging in to your account, you can:
   - Check the current balance.
   - Deposit money into account.
   - Withdraw money from account.
   - Transfer money between accounts.
   - Log out after completing transactions.

Account data can be loaded and saved to JSON file.

## Running the Program

```bash
# Navigate to the project directory
cd banking-system/

# Run the main script
python3 main.py
```

## Program Input & Output

When you run the program `main.py`, the output will look like this;

```
------------------------------ Welcome to X Bank ------------------------------

1: Create an Account
2: Log in to your Account
0: Exit Bank

Enter your choice:
> 1

Creating A New Account
Enter account holder's name: Alice
Enter account number: 1234
Set your PIN Code: 0000
Enter initial deposit amount: 50

Account ID already exists!
Failed to create account!

Press Enter to continue...

------------------------------ Welcome to X Bank ------------------------------

1: Create an Account
2: Log in to your Account
0: Exit Bank

Enter your choice:
> 2
Enter your account number: 1234
Enter your PIN code: 0000

Logged in successfully!

Press Enter to continue...

-------------------------------- Welcome, Alice -------------------------------

Account Menu:

1: Deposit
2: Widthdraw
3: Transfer
4: Check Current Balance
5: View Transaction History
6: Logout
0: Back

Enter your choice:
> 5

14-08-2024 09:16:37 - Account Created: 500

14-08-2024 14:06:46 - Deposit: 250.0

14-08-2024 14:12:58 - Withdrawal: 100.0

14-08-2024 14:14:59 - Transfer to account #5678: -150.0

14-08-2024 14:19:43 - Transfer from account #5678: 5000.0

14-08-2024 14:22:25 - Transfer from account #4321: 1000.0

Press Enter to continue...

-------------------------------- Welcome, Alice -------------------------------

Account Menu:

1: Deposit
2: Widthdraw
3: Transfer
4: Check Current Balance
5: View Transaction History
6: Logout
0: Back

Enter your choice:
> 2
Enter amount to withdraw: 42
Withdrawal successful!

Press Enter to continue...

-------------------------------- Welcome, Alice -------------------------------

Account Menu:

1: Deposit
2: Widthdraw
3: Transfer
4: Check Current Balance
5: View Transaction History
6: Logout
0: Back

Enter your choice:
> 4

Current balance: 6458.0

Press Enter to continue

-------------------------------- Welcome, Alice -------------------------------

Account Menu:

1: Deposit
2: Widthdraw
3: Transfer
4: Check Current Balance
5: View Transaction History
6: Logout
0: Back

Enter your choice:
> 5

14-08-2024 09:16:37 - Account Created: 500

14-08-2024 14:06:46 - Deposit: 250.0

14-08-2024 14:12:58 - Withdrawal: 100.0

14-08-2024 14:14:59 - Transfer to account #5678: -150.0

14-08-2024 14:19:43 - Transfer from account #5678: 5000.0

14-08-2024 14:22:25 - Transfer from account #4321: 1000.0

14-08-2024 14:58:49 - Withdrawal: 42.0

Press Enter to continue...

-------------------------------- Welcome, Alice -------------------------------

Account Menu:

1: Deposit
2: Widthdraw
3: Transfer
4: Check Current Balance
5: View Transaction History
6: Logout
0: Back

Enter your choice:
> 6

Logged out successfully!

Press Enter to continue...

------------------------------ Welcome to X Bank ------------------------------

1: Create an Account
2: Log in to your Account
0: Exit Bank

Enter your choice:
> 2
Enter your account number: 5678
Enter your PIN code: 1111

Logged in successfully!

Press Enter to continue...

--------------------------------- Welcome, Bob --------------------------------

Account Menu:

1: Deposit
2: Widthdraw
3: Transfer
4: Check Current Balance
5: View Transaction History
6: Logout
0: Back

Enter your choice:
> 5

14-08-2024 09:16:37 - Account Created: 42

14-08-2024 14:14:59 - Transfer from account #1234: 150.0

14-08-2024 14:15:40 - Deposit: 10000.0

14-08-2024 14:19:43 - Transfer to account #1234: -5000.0

14-08-2024 14:22:33 - Transfer from account #4321: 1000.0

Press Enter to continue...

--------------------------------- Welcome, Bob --------------------------------

Account Menu:

1: Deposit
2: Widthdraw
3: Transfer
4: Check Current Balance
5: View Transaction History
6: Logout
0: Back

Enter your choice:
> 6

Logged out successfully!

Press Enter to continue...

------------------------------ Welcome to X Bank ------------------------------

1: Create an Account
2: Log in to your Account
0: Exit Bank

Enter your choice:
> 0
Exiting Bank X... Bye!

```