from bank_account_manager import BankAccount
import time

def main():
    '''Main function to run the Bank Manager program.'''
    print('\n' + '*' * 40)
    display_centered('ATM SIMULATOR')
    print('*' * 40)

    print('Intitializing ATM ...')
    time.sleep(1)

    name = input('\nEnter your name: ')
    pin_number = input('Enter your pin number: ')
    initial_balance = float(input('Enter your initial balance: '))

    user_account = BankAccount(name, pin_number, initial_balance)

    while True:
        print('\n' + '*' * 40)
        display_centered('MENU')
        print('*' * 40)
        print('1. Balance Inquiry')
        print('2. Withdrawal')
        print('3. Deposit')
        print('4. Transfer')
        print('5. Exit')

        choice = input('\nEnter your choice: ')

        if choice == '1':
            print('\n' + '*' * 40)
            display_centered('BALANCE INQUIRY')
            print('*' * 40)
            print('Processing ...')
            time.sleep(0.5)
            print(f'Your current balance is: ${user_account.balance} \n')

        elif choice == '2':
            print('\n' + '*' * 40)
            display_centered('WITHDRAWAL')
            print('*' * 40)
            amount_str = input('Enter withdrawal amount: ')
            if not validate_amount(amount_str):
                print('Invalid amount. Please enter a valid positive number.')
                continue
            amount = float(amount_str)
            print('Processing ...')
            time.sleep(0.5)
            print(user_account.withdraw(amount))

        elif choice == '3':
            print('\n' + '*' * 40)
            display_centered('DEPOSIT')
            print('*' * 40)
            amount_str = input('Enter deposit amount: ')
            if not validate_amount(amount_str):
                print('Invalid amount. Please enter a valid positive number.')
                continue
            amount = float(amount_str)
            print('Processing ...')
            time.sleep(0.5)
            print(user_account.deposit(amount))

        elif choice == '4':
            print('\n' + '*' * 40)
            display_centered('TRANSFER')
            print('*' * 40)
            target_name = input('Enter recipient\'s name: ')
            amount_str = input('Enter transfer amount: ')
            if not validate_amount(amount_str):
                print('Invalid amount. Please enter a valid positive number.')
                continue
            amount = float(amount_str)
            target_account = BankAccount(target_name, '', 0)
            print('Processing ...')
            time.sleep(0.5)
            print(user_account.transfer(amount, target_account))

        elif choice == '5':
            print('\nThank you for using the ATM. Goodbye!')
            break

        else:
            print('\nInvalid choice. Please select a valid option.')

        time.sleep(1)

def display_centered(message):
    '''Displays a message centered on the screen.'''
    print('\n' + ' ' * ((40 - len(message)) // 2) + message + '\n' + ' ' * ((40 - len(message)) // 2))

def validate_amount(amount_str):
    '''Validates if the given input can be converted to a positive float.'''
    try:
        amount = float(amount_str)
        if amount <= 0:
            return False
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    main()