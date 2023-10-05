def main():
    '''Main function to run the Converter Program.'''

    print('\nWelcome to the Converter CLI!\n')
    while True:
        choice = get_conversion_choice()
        
        if choice == 1:
            length = float(input('Enter the length: '))
            unit_from = input('Enter the unit to convert from: ').lower()
            unit_to = input('Enter the unit to convert to: ').lower()
            convert_length(length, unit_from, unit_to)
        
        elif choice == 2:
            weight = float(input('Enter the weight: '))
            unit_from = input('Enter the unit to convert from: ').lower()
            unit_to = input('Enter the unit to convert to: ').lower()
            convert_weight(weight, unit_from, unit_to)
        
        elif choice == 3:
            temperature = float(input('Enter the temperature: '))
            unit_from = input('Enter the unit to convert from: ').capitalize()
            unit_to = input('Enter the unit to convert to: ').capitalize()
            convert_temperature(temperature, unit_from, unit_to)

        else:
            print('Invalid choice. Please try again.')

        cont = input('Do you want to perform another conversion? (y/n): ').lower()
        if cont != 'y':
            print('Bye!')
            break

def get_conversion_choice():
    '''Get user's choice for the type of conversion.'''

    print('Select a conversion:')
    print('1. Length')
    print('2. Mass')
    print('3. Temperature')
    choice = input('Enter choice: ')
    return int(choice)


def convert_length(length, unit_from, unit_to):
    '''Convert length to the specified units and print the result.'''
    # Define conversion factors
    conversion_factors = {
        'mm': 1000,
        'cm': 100,
        'm': 1,
        'km': 0.001,
        'inch': 39.3701,
        'foot': 3.28084,
        'yard': 1.09361,
        'mile': 0.000621371
    }

    try:
        length_meters = length / conversion_factors[unit_from]
        result = length_meters * conversion_factors[unit_to]
        print(f'Result: {result} {unit_to}')
    except KeyError:
        print('Invalid units.')

def convert_weight(weight, unit_from, unit_to):
    '''Convert weight to the specified units and print the result.'''
    # Define conversion factors
    conversion_factors = {
        'g': 1,
        'kg': 0.001,
        'mg': 1000,
        'lb': 0.00220462,
        'oz': 0.035274,
        'ton': 1e-6
    }

    try:
        weight_grams = weight / conversion_factors[unit_from]
        result = weight_grams * conversion_factors[unit_to]
        print(f'Result: {result} {unit_to}')
    except KeyError:
        print('Invalid units.')

def convert_temperature(temperature, unit_from, unit_to):
    '''Convert temperature to the specified units and print the result.'''

    if unit_from == 'Celsius' and unit_to == 'Fahrenheit':
        result = temperature * 9/5 + 32
        print(f'Result: {result} {unit_to}')
    elif unit_from == 'Fahrenheit' and unit_to == 'Celsius':
        result = (temperature - 32) * 5/9
        print(f'Result: {result} {unit_to}')
    else:
        print('Invalid units.')


if __name__ == '__main__':
    main()
