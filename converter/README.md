# Converter

## Description

The Converter is a command-line program that allows users to convert lengths, masses, or temperatures based on their input and selected units. The program supports three types of conversions: length, mass, and temperature.


## How it Works

- The <code>main</code> function begins by printing a welcome message. Then it prompts the user to choose the desired type of conversion by entering the corresponding number.

- The program contains three conversion functions. Each of these functions takes the input value, the unit to convert from, and the unit to convert to as arguments. They calculate the result based on the conversion formula for the respective type (length, weight, or temperature) and print the converted value.
    - <code>convert_length</code>: Converts a length from one unit to another.
    - <code>convert_weight</code>: Converts a weight from one unit to another.
    - <code>convert_temperature</code>: Converts a temperature from one unit to another.

- Each of these functions takes the input value, the unit to convert from, and the unit to convert to as arguments. They calculate the result based on the conversion formula for the respective type (length, weight, or temperature) and print the converted value.

- The program interacts with the user to collect input values for the conversion, including the type of conversion and the units involved. It validates user input and ensures a smooth flow of the conversion process.

- The menu interface is governed by the <code>get_conversion_choice</code> function and the <code>main</code> function. It allows users to select the type of conversion they wish to perform. It provides options to choose from and guides the user through the conversion process based on their choice.

## Program Input & Output

When you run `converter.py`, the output will look like this:

```

Welcome to the Converter CLI!

Select a conversion:
1. Length
2. Mass
3. Temperature
Enter choice: 1
Enter the length: 42
Enter the unit to convert from: inch
Enter the unit to convert to: m
Result: 1.066799423928311 m
Do you want to perform another conversion? (y/n): y
Select a conversion:
1. Length
2. Mass
3. Temperature
Enter choice: 2
Enter the weight: 100
Enter the unit to convert from: kg
Enter the unit to convert to: lb
Result: 220.462 lb
Do you want to perform another conversion? (y/n): y
Select a conversion:
1. Length
2. Mass
3. Temperature
Enter choice: 3
Enter the temperature: 32
Enter the unit to convert from: celsius
Enter the unit to convert to: fahrenheit
Result: 89.6 Fahrenheit
```