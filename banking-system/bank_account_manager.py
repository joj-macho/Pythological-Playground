class BankAccount:
    '''Represents a bank account with the ability to perform transactions like deposit, withdraw, and transfer.'''

    def __init__(self, name, pin_number, initial_balance):
        '''
        Initializes a BankAccount instance.

        Parameters:
            - name (str): The name associated with the bank account.
            - pin_number (str): The pin-number associated with the bank account.
            - initial_balance (float): The initial balance of the bank account.
        '''
        self.name = name
        self.pin_number = pin_number
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
