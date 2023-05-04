accounts_list = []

def main():
    '''This is the main function'''

    print('\nWelcome to the Bank Account Manager.\n')

    # Create two sample accounts
    new_account("Joe", 500, '1234')
    new_account("Mary", 10, 'marry')

    while True:
        print('Press b to get the balance')
        print('Press d to make a deposit')
        print('Press n to create a new account')
        print('Press w to make a withdrawal')
        print('Press s to show all accounts')
        print('Press q to quit')
        print()

        response = input('What do you want to do?\n> ').lower()
        print()
        
        if response.startswith('b'):
            print('Get Balance:')
            account_number = int(input('Please enter your account number:\n> '))
            password = input('Please enter the password:\n> ')
            balance = get_balance(account_number, password)
            if balance is not None:
                print('Your balance is:', balance)

        elif response.startswith('d'):
            print('Deposit:')
            account_number = int(input('Please enter the account number:\n> '))
            deposit_amount = int(input('Please enter amount to deposit:\n> '))
            password = input('Please enter the password:\n> ')

            new_balance = deposit(account_number, deposit_amount, password)
            if new_balance is not None:
                print('Your new balance is:', new_balance)

        elif response.startswith('n'):
            print('New Account:')
            name = input('What is your name?\n> ')
            starting_amount = int(input('What is the amount of your initial deposit?\n> '))
            password = input('What password would you like to use for this account?\n> ')

            account_number = len(accounts_list)
            new_account(name, starting_amount, password)
            print('Your new account number is:', account_number)

        elif response.startswith('s'):   #show all
            print('Show:')
            n_accounts = len(accounts_list)
            for account_number in range(0, n_accounts):
                show_accounts(account_number)

        elif response.startswith('w'):
            print('Withdraw:')
            account_number = int(input('Please enter your account number:\n> '))
            withdraw_amount = int(input('Please enter the amount to withdraw:\n> '))
            password = input('Please enter the password:\n> ')

            new_balance = withdraw(account_number, withdraw_amount, password)
            if new_balance is not None:
                print('Your new balance is:', new_balance)

        elif response.startswith('q'):
            print('Bye!')
            break


def new_account(name, balance, password):
    '''This function adds a new account to the accounts_list'''

    new_account_dict = {'name':name, 'balance':balance, 'password':password}
    accounts_list.append(new_account_dict)
   
def show_accounts(account_number):
    '''This function displays the details of a particular account.'''

    print('Account', account_number)
    this_account_dict = accounts_list[account_number]
    print('       Name', this_account_dict['name'])
    print('       Balance:', this_account_dict['balance'])
    print('       Password:', this_account_dict['password'])
    print()

def get_balance(account_number, password):
    '''This function returns the balance of a particular account.'''

    this_account_dict = accounts_list[account_number]
    if password != this_account_dict['password']:
        print('Incorrect password')
        return None
    return this_account_dict['balance']

def deposit(account_number, amountToDeposit, password):
    '''This function deposits the specified amount into the specified account and returns the new balance of the account.'''

    this_account_dict = accounts_list[account_number]
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None
        
    if password != this_account_dict['password']:
        print('Incorrect password')
        return None
    
    this_account_dict['balance'] = this_account_dict['balance'] + amountToDeposit
    return this_account_dict['balance']
    
def withdraw(account_number, amountToWithdraw, password):
    '''This function withdraws the specified amount from the specified account and returns the new balance of the account.'''

    this_account_dict = accounts_list[account_number]
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None

    if password != this_account_dict['password']:
        print('Incorrect password for this account')
        return None

    if amountToWithdraw > this_account_dict['balance']:
        print('You cannot withdraw more than you have in your account')
        return None

    this_account_dict['balance'] = this_account_dict['balance'] - amountToWithdraw
    return this_account_dict['balance']


if __name__ == '__main__':
    main()
