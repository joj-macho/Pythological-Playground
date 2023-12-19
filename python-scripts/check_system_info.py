'''
check_system_info.py

This script checks and prints information about the Python version and various
system-related details using the sys and platform modules. 

'''

import sys
import platform

def check_python_version():
    '''Prints information about the Python version.'''
    print(f'Python Version: {sys.version}')
    print(f'Python Version Info: {sys.version_info}')
    print(f'Python Major Version: {sys.version_info.major}')
    print(f'Python Minor Version: {sys.version_info.minor}')

def check_system_info():
    '''Prints various system-related information.'''
    print(f'System: {platform.system()}')
    print(f'Node: {platform.node()}')
    print(f'Release: {platform.release()}')
    print(f'Version: {platform.version()}')
    print(f'Machine: {platform.machine()}')
    print(f'Processor: {platform.processor()}')

if __name__ == '__main__':
    check_python_version()
    print('\nSystem Information:')
    check_system_info()
