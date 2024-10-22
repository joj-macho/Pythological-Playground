import json
from pathlib import Path
from bank_account import BankAccount

# Directory where this script is located
BASE_PATH = Path(__file__).resolve().parent


class BankSystem:
    def __init__(self, file_name='bank_accounts.json'):
        '''
        Initialize the banking system.
        
        Parameters:
            file_name (str): File name for storing banking data.
        '''
        self.file_path = BASE_PATH / file_name  # Full path to json file
        self.accounts = self.load_accounts()
        self.logged_in_account = None

    def load_accounts(self):
        '''Load accounts from json data file file.'''
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return {acc_id: BankAccount.from_dict(acc_data)
                        for acc_id, acc_data in data.items()}
        except FileNotFoundError:
            return {}

    def save_accounts(self):
        '''Save accounts json data file.'''
        with open(self.file_path, 'w') as file:
            data = {acc_id: acc.to_dict() for acc_id, acc
                    in self.accounts.items()}
            json.dump(data, file, indent=4)

    def create_account(self, account_holder, account_id, pin,
                       initial_balance=0):
        '''Create a new Bank Account.'''
        if account_id in self.accounts:
            print('\nAccount ID already exists!')
            return None

        new_account = BankAccount(account_holder, account_id, pin,
                                  initial_balance)
        self.accounts[account_id] = new_account
        self.save_accounts()
        return new_account

    def login(self, account_id, pin):
        '''Login to account.'''
        if account_id not in self.accounts:
            print('\nAccount ID does not exist!')
            return False

        account = self.accounts[account_id]
        if account.pin != pin:
            print('\nInvalid Pin!')
            return False

        self.logged_in_account = account
        return True

    def logout(self):
        '''Logout from current account.'''
        if self.logged_in_account:
            self.logged_in_account = None
            return True
        return False

    def deposit(self, amount):
        '''Deposit into current account.'''
        if self.logged_in_account:
            success = self.logged_in_account.deposit(amount)
            self.save_accounts()
            return success
        return False

    def withdraw(self, amount):
        '''Withdraw from current account.'''
        if self.logged_in_account:
            success = self.logged_in_account.withdraw(amount)
            self.save_accounts()
            return success
        return False

    def get_balance(self):
        '''Get the abalnce of the current account.'''
        if self.logged_in_account:
            return self.logged_in_account.get_balance()
        return None

    def get_transaction_history(self):
        '''Get the transaction history of the current account.'''
        if self.logged_in_account:
            return self.logged_in_account.get_transaction_history()
        return None

    def transfer(self, to_account_id, amount):
        '''Transfer money to another account from current account.'''
        if self.logged_in_account:
            if to_account_id not in self.accounts:
                print('\nRecipient account does not exist!')
                return False
            if to_account_id == self.logged_in_account.account_id:
                print('\nCannot transfer money to your own account!')
                return False

            recipient_account = self.accounts[to_account_id]
            if amount <= 0:
                print('\nInvalid amount! Enter positive amount to transfer.')
                return False
            if self.logged_in_account.balance < amount:
                print('\nInsufficient funds!')
                return False

            self.logged_in_account.balance -= amount
            recipient_account.balance += amount

            self.logged_in_account.add_transaction(
                'Transfer to account #' + to_account_id, -amount)
            recipient_account.add_transaction(
                'Transfer from account #' +
                self.logged_in_account.account_id,
                amount)
            self.save_accounts()
            return True
        return False


# Sanity Check
if __name__ == '__main__':
    bank = BankSystem('test_accounts.json')
    # Create new accounts
    if '1234' in bank.accounts:
        # load account
        account_1 = bank.accounts['1234']
    else:
        account_1 = bank.create_account('Alice', '1234', '0000', 500)

    if '5678' in bank.accounts:
        account_2 = bank.accounts['5678']
    else:
        account_2 = bank.create_account('Bob', '5678', '1111', 42)
    print('New accounts:')
    print(account_1.to_dict())
    print(account_2.to_dict())

    # Login to an account
    print('\nLogin to Alice account:')
    if bank.login('1234', '0000'):
        print(f'Logged in as {bank.logged_in_account.account_holder}')
        print(f'History: {bank.logged_in_account.get_transaction_history()}')
    else:
        print('Failed to login!')

    print('Logout:')
    bank.logout()
    if bank.logged_in_account is None:
        print('Logged out!')
    else:
        print(f'{bank.logged_in_account.account_holder} logged in')

    print('\nLogin as Bob:')
    if bank.login('56781', '11111'):
        print(f'Logged in as {bank.logged_in_account.account_holder}')
        print(f'Account balance: {bank.logged_in_account.get_balance()}')
    else:
        print('Failed to login!')
