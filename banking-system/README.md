# Banking System Simulator

## Description

The "Banking System" program allows users to manage multiple bank accounts securely using a PIN code. Users can perform balance inquiries, deposits, withdrawals, and transfers between accounts.

## How It Works

- **Account Creation**:
    - Users can create multiple bank accounts.
    - Each account is secured with a unique PIN code for access. Access accounts by entering the account number and the corresponding PIN code.

- **Balance Inquiry**:
    - Users can check the current balance of their account after logging in.

- **Deposit**:
   - Users can deposit money into their account.
   - The deposited amount is added to the current balance.

- **Withdrawal**:
   - Users can withdraw money from their account.
   - The withdrawn amount is subtracted from the current balance, provided there are sufficient funds.

- **Transfer**:
   - Users can transfer money between accounts.
   - The transferred amount is subtracted from the sender's account and added to the recipient's account, provided there are sufficient funds in the sender's account.

- **Session Management**:
   - Users can log out after completing their transactions.
   - The system returns to the account access prompt after each session.

## Running the Program

```bash
# Navigate to the project directory
cd pico-fermi-bagels

# Run the main script
python3 pico_fermi_bagels.py
```

## Program Input & Output

When you run the program `main_bank.py`, the output will look like this;

```

```