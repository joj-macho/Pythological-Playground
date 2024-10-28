def main():
    '''Run unit converter program.'''
    print('The Unit Converter Program.\n')

    options = {
        '1': 'Convert Length Units.',
        '2': 'Convert Mass Units.',
        '3': 'Convert Temperature Units.'
    }
    while True:
        print('Choose an option:')
        for key, description in options.items():
            print(f'{key}. {description}')
        print('Or enter (q)uit to exit.')

        choice = get_choice('> ', options.keys())
        if choice is None:
            break

        if choice == '1':
            print('\nConverting length...')
            print('Avaliable Units:', ', '.join(get_unit_list('length')))
            convert_length()

        elif choice == '2':
            print('\nConverting mass...')
            print('Available Units:', ', '.join(get_unit_list('mass')))
            convert_mass()

        elif choice == '3':
            print('\nConveting temperature...')
            print('Available Units:', ', '.join(get_unit_list('temperature')))
            convert_temperature()


def get_choice(prompt, options):
    '''Prompts to select an option from given options.'''
    while True:
        choice = input(prompt).strip().lower()
        if choice in ('q', 'quit'):
            print('Bye!')
            return None
        if choice in options:
            return choice
        print(f'Invalid choice! Enter {", ".join(options)}'
              ' or (q)uit to exit.\n')


def get_unit_list(category):
    '''Retrieves the list of available units for a given category.'''
    unit_categories = {
        'length': ['mm', 'cm', 'm', 'km', 'inch', 'foot', 'yard', 'mile'],
        'mass': ['g', 'kg', 'mg', 'lb', 'oz', 'ton'],
        'temperature': ['Celsius', 'Fahrenheit', 'Kelvin']
    }
    return unit_categories.get(category, [])


def convert_length():
    '''Converts length to different units.'''
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

    # Convert to valid units
    try:
        length = float(input('Enter the length value: '))
        unit_from = input('Enter the unit to convert from: ').lower()
        unit_to = input('Enter the unit to convert to: ').lower()

        if unit_from in conversion_factors and unit_to in conversion_factors:
            length_unit = length / conversion_factors[unit_from]
            result = length_unit * conversion_factors[unit_to]
            print(f'Result: {length} {unit_from} = {result:.4f} {unit_to}\n')
        else:
            print('Invalid Units. Choose valid units from the list.\n')

    except ValueError:
        print('Invalid input! Enter a valid number for the length.\n')


def convert_mass():
    '''Converts mass to different units.'''
    conversion_factors = {
        'g': 1,
        'kg': 0.001,
        'mg': 1000,
        'lb': 0.00220462,
        'oz': 0.035274,
        'ton': 1e-6
    }

    try:
        mass = float(input('Enter the mass value: '))
        unit_from = input('Enter the unit to convert from: ').lower()
        unit_to = input('Enter the unit to convert to: ').lower()

        if unit_from in conversion_factors and unit_to in conversion_factors:
            mass_unit = mass / conversion_factors[unit_from]
            result = mass_unit * conversion_factors[unit_to]
            print(f'Result: {mass} {unit_from} = {result:.4f} {unit_to}\n')
        else:
            print('Invalid units. Choose valid units from the list.\n')

    except ValueError:
        print('Invalid Input! Enter a valid number for the mass.\n')


def convert_temperature():
    '''Converts temperature to different units.'''
    try:
        temperature = float(input('Enter the temperature value: '))
        unit_from = input('Enter the unit to convert from: ').capitalize()
        unit_to = input('Enter the unit to convert to: ').capitalize()

        if unit_from == 'Celsius' and unit_to == 'Fahrenheit':
            result = temperature * 9 / 5 + 32
        elif unit_from == 'Celsius' and unit_to == 'Kelvin':
            result = temperature + 273.15
        elif unit_from == 'Fahrenheit' and unit_to == 'Celsius':
            result = (temperature - 32) * 5 / 9
        elif unit_from == 'Fahrenheit' and unit_to == 'Kelvin':
            result = (temperature - 32) * 5 / 9 + 273.15
        elif unit_from == 'Kelvin' and unit_to == 'Celsius':
            result = temperature - 273.15
        elif unit_from == 'Kelvin' and unit_to == 'Fahrenheit':
            result = (temperature - 273.15) * 9 / 5 + 32
        else:
            print('Invalid units. Please choose valid units from the list.')
            return

        print(f'Result: {temperature} {unit_from} = {result:.2f} {unit_to}\n')
    except ValueError:
        print('Invalid input! Enter a valid number for the temperature.\n')


if __name__ == '__main__':
    main()
