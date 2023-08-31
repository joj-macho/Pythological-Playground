import time

class BankAccount:
    '''Represents a bank account with the ability to perform transactions like deposit, withdraw, and transfer.'''

    def __init__(self, name, password, initial_balance):
        '''Initializes a BankAccount instance.'''

        self.name = name
        self.password = password
        self.balance = initial_balance

    def deposit(self, amount):
        '''Deposits a specified amount into the account.'''

        self.balance += amount
        return f'Deposited ${amount}.\nCurrent balance: ${self.balance}\n'

    def withdraw(self, amount):
        '''Withdraws a specified amount from the account.'''

        if self.balance >= amount:
            self.balance -= amount
            return f'Withdrew ${amount}.\nCurrent balance: ${self.balance}\n'
        else:
            return f'Insufficient balance! Enter amount ${self.balance} or lower to withdraw.\n'

    def transfer(self, amount, target_account):
        '''Transfers a specified amount from the account to a target account.'''

        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
            return f'Transferred ${amount} to {target_account.name}.\nCurrent balance: ${self.balance}'
        else:
            return f'Insufficient balance for transfer! Enter amount ${self.balance} or lower to withdraw.\n'


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


def main():
    print('\n' + '*' * 40)
    display_centered('ATM SIMULATOR')
    print('*' * 40)

    print('Intitializing ATM ...')
    time.sleep(1)  # Introduce a delay of 1 second

    name = input('\nEnter your name: ')
    password = input('Enter your password: ')
    initial_balance = float(input('Enter your initial balance: '))

    user_account = BankAccount(name, password, initial_balance)

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

        time.sleep(1)  # Introduce a delay of 1 second


if __name__ == '__main__':
    main()
