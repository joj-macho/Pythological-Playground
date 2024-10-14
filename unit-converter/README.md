# Unit Converter

## Description

The Converter is a command-line program that allows users to convert lengths, masses, or temperatures based on their input and selected units. The program supports three types of conversions: length, mass, and temperature.

## How it Works

- The `main` function enters a loop to perform unit conversions based on the user's choice. Users are prompted to select the type of conversion (length, mass, or temperature) by entering the corresponding number. The menu interface allows users to select the type of conversion they want to perform.

- The program contains three conversion functions: `convert_length`, `convert_weight`, and `convert_temperature`. Each of these functions accepts an input value, the unit to convert from, and the unit to convert to as arguments. They calculate the result using the appropriate conversion formula for the respective type and display the converted value.

- The program provides a list of available units for each type of conversion. This list is obtained through the `get_unit_list` function, which returns the units for the chosen category (length, mass, or temperature).

- The program interacts with the user to collect input values for conversion, including the choice of conversion type and the units involved. It also validates user input to ensure everything works well.

## Running the Program

```bash
# Navigate to the project directory
cd unit-converter/

# Run the main script
python3 converter.py
```

## Program Input & Output

When you run `converter.py`, the output will look like this:

```

Welcome to the Unit Converter Program!

Choose a Conversion Option:
1. Length
2. Mass
3. Temperature

Enter choice: 1

Available units: mm, cm, m, km, inch, foot, yard, mile
Enter the length value: 10
Enter the unit to convert from: km
Enter the unit to convert to: yard
Results: 10.0 km = 10936.1 yard

Do you want to perform another conversion? (y/n): y
Choose a Conversion Option:
1. Length
2. Mass
3. Temperature

Enter choice: 2

Available units: g, kg, mg, lb, oz, ton
Enter the mass value: 10
Enter the unit to convert from: lb
Enter the unit to convert to: oz
Result: 10.0 lb = 160.00036287432755 oz

Do you want to perform another conversion? (y/n): y
Choose a Conversion Option:
1. Length
2. Mass
3. Temperature

Enter choice: 3

Available units: Celsius, Fahrenheit, Kelvin
Enter the temperature value: 0      
Enter the unit to convert from: celcius
Enter the unit to convert to: kelvin
Invalid units.

Do you want to perform another conversion? (y/n): y
Choose a Conversion Option:
1. Length
2. Mass
3. Temperature

Enter choice: 3

Available units: Celsius, Fahrenheit, Kelvin
Enter the temperature value: 0
Enter the unit to convert from: celsius
Enter the unit to convert to: kelvin
Result: 0.0 Celsius = 273.15 Kelvin

Do you want to perform another conversion? (y/n): n
Bye!
```