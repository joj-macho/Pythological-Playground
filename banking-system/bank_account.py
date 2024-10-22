from datetime import datetime


class BankAccount:
    def __init__(self, account_holder, account_id, pin, initial_balance=500.0):
        '''Initialize a new bank account

        Parameters:
            account_holder (str): Name of the account holder.
            account_id (str): Account number.
            pin (str): Pin code for the bank account.
            initial_balance (float): Initial balance.
        '''
        self.account_holder = account_holder
        self.account_id = account_id
        self.pin = pin
        self.balance = initial_balance

        self.transactions = []
        self.add_transaction('Account Created', initial_balance)

    def add_transaction(self, transaction_type, amount):
        '''Adds transaction to transaction history.'''
        transaction = {
            'transaction_type': transaction_type,
            'amount': amount,
            'date': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        }
        self.transactions.append(transaction)

    def deposit(self, amount):
        '''Deposits money into account.'''
        if amount <= 0:
            print('\nDeposit amount must be positive!')
            return False
        self.balance += amount
        self.add_transaction('Deposit', amount)
        return True

    def withdraw(self, amount):
        '''Withdraws money from account.'''
        if amount <= 0:
            print('\nWithdrawal amount must be positive!')
            return False
        if amount > self.balance:
            print('\nInsufficient funds!')
            return False
        self.balance -= amount
        self.add_transaction('Withdrawal', amount)
        return True

    def get_balance(self):
        '''Gets the balance of the account.'''
        return self.balance

    def get_transaction_history(self):
        '''Gets the transaction history of the account.'''
        return self.transactions

    def to_dict(self):
        '''Converts the account to a dictionary format.'''
        return {
            'account_holder': self.account_holder,
            'account_id': self.account_id,
            'pin': self.pin,
            'balance': self.balance,
            'transactions': self.transactions
        }

    @staticmethod
    def from_dict(data):
        '''Creates a BankAccount instance from a dictionary.'''
        account = BankAccount(
            data['account_holder'], data['account_id'], data['pin']
        )
        account.account_holder = data['account_holder']
        account.account_id = data['account_id']
        account.balance = data['balance']
        account.transactions = data['transactions']
        return account


# Sanity Check
if __name__ == '__main__':
    # Create a new bank account
    account_1 = BankAccount('Alice', '0000', '0000')
    print(f'Account created for {account_1.account_holder}')
    print(f'Initial account details:\n'
          f'Account Holder: {account_1.account_holder}\n'
          f'Account Number: {account_1.account_id}\n'
          f'Account Pin Number: {account_1.pin}\n'
          f'Initial Balance: {account_1.balance}\n'
          f'Initial transaction history: '
          f'{account_1.transactions}')
    print()

    # Deposit Money
    print('Depositing money into account:')
    if account_1.deposit(250):
        print('Deposit successful')
    else:
        print('Deposit Failed')
    print(f'Balance after deposit: {account_1.get_balance()}')
    print(f'Transaction history: {account_1.transactions}')

    # Withdraw money
    print('\nWithdrawing money from account:')
    if account_1.withdraw(500):
        print('Withdarwal successful')
    else:
        print('Withdrawal failed')
    print(f'Balance after withdrawal: {account_1.get_balance()}')
    print(f'Transaction History: {account_1.transactions}')

    # Transactio History:
    print('\nTransaction History:')
    history = account_1.get_transaction_history()
    for transaction in history:
        print(transaction)
