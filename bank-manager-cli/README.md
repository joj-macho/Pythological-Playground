# Bank Account Manager

## Description

The Bank Account Manager program is a simple Python program that simulates the banking system that allows users to create and manage bank accounts. The program maintains a list of accounts and provides various functions such as creating a new account, depositing money, withdrawing money, checking balance, and displaying all accounts.


## How it Works

- The program starts by creating two sample accounts for Joe and Mary using the <code>new_account</code> function. 

- The program then enters into a while loop that continues to execute until the user chooses to quit. Within the loop, the program displays a menu of options to the user, which the user can choose from by entering the corresponding letter. The program then prompts the user for input depending on the option chosen. For example, if the user chooses to deposit money, the program prompts the user for the account number, the amount to deposit, and the account password.

- The program then calls the corresponding function to perform the user's selected operation. For instance, the <code>deposit()</code> function updates the account balance after validating the password and the deposit amount is positive. The <code>withdraw()</code> function updates the account balance after validating the password and checking that the requested withdrawal amount is less than the account balance. The <code>get_balance()</code> function retrieves the balance for the given account number, provided the password matches. The <code>show_accounts()</code> function is used to display details of all accounts or a particular account number.

- The program exits the while loop when the user chooses to quit by entering 'q'.


## Program Input & Output

When you run the program `bank_manager.py`, the output will look like this;

```
 
Welcome to the Bank Account Manager.

Press b to get the balance
Press d to make a deposit
Press n to create a new account
Press w to make a withdrawal
Press s to show all accounts
Press q to quit

What do you want to do?
> s

Show:
Account 0
       Name Joe
       Balance: 500
       Password: 1234

Account 1
       Name Mary
       Balance: 10
       Password: marry

Press b to get the balance
Press d to make a deposit
Press n to create a new account
Press w to make a withdrawal
Press s to show all accounts
Press q to quit

What do you want to do?
> n

New Account:
What is your name?
> Mike
What is the amount of your initial deposit?
> 0
What password would you like to use for this account?
> mike
Your new account number is: 2
Press b to get the balance
Press d to make a deposit
Press n to create a new account
Press w to make a withdrawal
Press s to show all accounts
Press q to quit

What do you want to do?
> d

Deposit:
Please enter the account number:
> 2
Please enter amount to deposit:
> 100
Please enter the password:
> mike
Your new balance is: 100
Press b to get the balance
Press d to make a deposit
Press n to create a new account
Press w to make a withdrawal
Press s to show all accounts
Press q to quit

What do you want to do?
> w

Withdraw:
Please enter your account number:
> 1
Please enter the amount to withdraw:
> 200
Please enter the password:
> marry
You cannot withdraw more than you have in your account
Press b to get the balance
Press d to make a deposit
Press n to create a new account
Press w to make a withdrawal
Press s to show all accounts
Press q to quit

What do you want to do?
> s

Show:
Account 0
       Name Joe
       Balance: 500
       Password: 1234

Account 1
       Name Mary
       Balance: 10
       Password: marry

Account 2
       Name Mike
       Balance: 100
       Password: mike

Press b to get the balance
Press d to make a deposit
Press n to create a new account
Press w to make a withdrawal
Press s to show all accounts
Press q to quit

What do you want to do?
> q

Bye!
```