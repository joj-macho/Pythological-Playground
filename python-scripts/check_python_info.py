'''
check_python_installation.py

This script checks whether Python is installed on the user's system and prints the Python version if installed.
If Python is not installed, it prints an error message.

Usage:
    python check_python_installation.py
'''

import sys
import platform
import shutil

def check_using_version_info():
    '''Checks whether Python is installed on the system using sys.version_info.'''
    try:
        # Check if Python is installed by printing the version
        version_info = sys.version_info
        print(f'Python Version: {version_info.major}.{version_info.minor}.{version_info.micro}')
        print('Python is installed on your system.')
    except Exception as e:
        # If an exception occurs, Python is not installed
        print('Python is not installed on your system.')
        print(f'Error: {e}')

def check_using_executable():
    '''Checks whether Python is installed on the system using sys.executable.'''
    try:
        if sys.executable:
            print(f'Python executable path: {sys.executable}')
            print('Python is installed on your system.')
        else:
            print('Python is not installed on your system.')
    except Exception as e:
        print(f'Error while checking sys.executable: {e}')

def check_using_python_version():
    '''Checks whether Python is installed on the system using platform.python_version.'''
    try:
        python_version = platform.python_version()
        print(f'Python Version: {python_version}')
        print('Python is installed on your system.')
    except Exception as e:
        print(f'Error while checking platform.python_version: {e}')

def check_using_shutil_which():
    '''Checks whether Python is installed on the system using shutil.which.'''
    try:
        python_executable = shutil.which('python')
        if python_executable:
            print(f'Python executable path: {python_executable}')
            print('Python is installed on your system.')
        else:
            print('Python is not installed on your system.')
    except Exception as e:
        print(f'Error while checking shutil.which: {e}')


if __name__ == '__main__':
    check_using_version_info()
    check_using_executable()
    check_using_python_version()
    check_using_shutil_which()
