from bank_system import BankSystem


def main():
    '''Run the Banking System Simulator.'''
    bank = BankSystem('test_accounts.json')  # Usign test json file

    while True:
        choice = main_menu()
        if choice is None:
            print('Exiting Bank X... Bye!')
            break

        if choice == '1':  # create a new account
            print('\nCreating A New Account')
            account_holder = input('Enter account holder\'s name: ')
            account_id = input('Enter account number: ')
            pin = input('Set your PIN Code: ')
            initial_balance = float(input('Enter initial deposit amount: '))
            if bank.create_account(
                    account_holder, account_id, pin, initial_balance):
                print('Account created successfully!')
            else:
                print('Failed to create account!')
            input('\nPress Enter to continue...')

        elif choice == '2':
            account_id = input('Enter your account number: ')
            pin = input('Enter your PIN code: ')
            if bank.login(account_id, pin):
                print('\nLogged in successfully!')
                is_login = True
            else:
                print('\nFailed to login!')
                is_login = False
            input('\nPress Enter to continue...')

            if is_login:
                handle_transactions(bank)

        else:
            break


def main_menu():
    '''Display the main menu options.'''
    print()
    print(' Welcome to X Bank '.center(79, '-'))
    print()
    options = {
        '1': 'Create an Account',
        '2': 'Log in to your Account',
        '0': 'Exit Bank'
    }
    for key, description in options.items():
        print(f'{key}: {description}')

    print('\nEnter your choice:')
    choice = get_user_choice('> ', options.keys())
    return choice


def get_user_choice(prompt, options):
    '''Prompt the user to select option from options.'''
    while True:
        choice = input(prompt)
        if choice == '0':
            # print('Exiting Bank X... Bye!')
            return None
        if choice in options:
            return choice
        print(f'Invalid choice! Select from {", ".join(options)}\n')


def handle_transactions(bank):
    '''Handle bank transactions.'''
    while bank.logged_in_account:
        choice = account_menu(bank.logged_in_account.account_holder)
        if choice is None:
            print('Back to main menu...')
            break

        if choice == '1':  # Deposit
            amount = float(input('Enter amount to deposit: '))
            if bank.deposit(amount):
                print('Deposit successful!')
            else:
                print('Failed to deposit!')
            input('\nPress Enter to continue...')
        elif choice == '2':  # Withdraw
            amount = float(input('Enter amount to withdraw: '))
            if bank.withdraw(amount):
                print('Withdrawal successful!')
            else:
                print('Failed to withdraw!')
            input('\nPress Enter to continue...')
        elif choice == '3':  # Transfer
            to_account_id = input('Enter recipeint account number: ')
            amount = float(input('Enter amount to transfer: '))
            if bank.transfer(to_account_id, amount):
                print('Transfer successful!')
            else:
                print('Failed to transfer!')
            input('\nPress Enter to continue...')
        elif choice == '4':  # CHeck balance
            balance = bank.get_balance()
            if balance is not None:
                print(f'\nCurrent balance: {balance}')
            else:
                print('\nFailed to check balance!')
            input('\nPress Enter to continue')
        elif choice == '5':  # View history
            transactions = bank.get_transaction_history()
            if transactions is not None:
                for trans in transactions:
                    print(f'\n{trans["date"]} - {trans["transaction_type"]}: '
                          f'{trans["amount"]}')
            else:
                print('\nFailed to retrieve transaction history!')
            input('\nPress Enter to continue...')
        else:  # Logout
            bank.logout()
            print('\nLogged out successfully!')
            input('\nPress Enter to continue...')
            break


def account_menu(account_holder):
    '''Display current account menu screen.'''
    print()
    print(f' Welcome, {account_holder} '.center(79, '-'))
    print('\nAccount Menu:\n')
    options = {
        '1': 'Deposit',
        '2': 'Widthdraw',
        '3': 'Transfer',
        '4': 'Check Current Balance',
        '5': 'View Transaction History',
        '6': 'Logout',
        '0': 'Back'
    }
    for key, description in options.items():
        print(f'{key}: {description}')

    print('\nEnter your choice:')
    choice = get_user_choice('> ', options.keys())
    return choice


if __name__ == '__main__':
    main()
