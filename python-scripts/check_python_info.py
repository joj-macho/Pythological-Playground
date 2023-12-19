'''
check_python_installation.py

This script checks whether Python is installed on the user's system and prints the Python version if installed.
If Python is not installed, it prints an error message.

Usage:
    python check_python_installation.py
'''

import sys

def check_python_installation():
    '''Checks whether Python is installed on the system.'''
    try:
        # Check if Python is installed by printing the version
        version_info = sys.version_info
        print(f'Python Version: {version_info.major}.{version_info.minor}.{version_info.micro}')
        print('Python is installed on your system.')
    except Exception as e:
        # If an exception occurs, Python is not installed
        print('Python is not installed on your system.')
        print(f'Error: {e}')

if __name__ == '__main__':
    check_python_installation()

