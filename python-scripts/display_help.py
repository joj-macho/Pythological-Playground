'''
display_help.py

This script provides help or information about a specific Python function or module.

Usage:
    python display_help.py <function_or_module_name>
'''

import sys

def display_help(item_name):
    '''
    Display help or information about a specific Python function or module.

    Parameters:
        item_name (str): The name of the function or module.

    Raises:
        AttributeError: If the provided item name is not a valid attribute in the builtins module.
        ImportError: If the provided item name is not a valid module.

    Example:
        python display_help.py print
    '''
    try:
        item = getattr(__builtins__, item_name)
        help(item)
    except AttributeError:
        try:
            item = __import__(item_name)
            help(item)
        except ImportError:
            print(f'Error: {item_name} is not a valid Python function or module.')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <function_or_module_name>')
    else:
        item_name = sys.argv[1]
        display_help(item_name)
