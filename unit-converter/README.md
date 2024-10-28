# Unit Converter

## Description

The Unit Converter program allows users to convert lengths, masses, or temperatures based on their input and selected units. The program supports three types of conversions: length, mass, and temperature.

## How it Works

- Select the type of conversion (length, mass, or temperature).
- The input value is taken, and the program converts it to the desired unit using predefined conversion factors or formulas (for temperature).

## Running the Program

```bash
# Navigate to the project directory
cd unit-converter/

# Run the main script
python3 unit_converter.py
```

## Program Input & Output

When you run `unit_converter.py`, the output will look like this:

```
The Unit Converter Program.

Choose an option:
1. Convert Length Units.
2. Convert Mass Units.
3. Convert Temperature Units.
Or enter (q)uit to exit.
> 1

Converting length...
Avaliable Units: mm, cm, m, km, inch, foot, yard, mile
Enter the length value: 1
Enter the unit to convert from: m
Enter the unit to convert to: mile
Result: 1.0 m = 0.0006 mile

Choose an option:
1. Convert Length Units.
2. Convert Mass Units.
3. Convert Temperature Units.
Or enter (q)uit to exit.
> 2

Converting mass...
Available Units: g, kg, mg, lb, oz, ton
Enter the mass value: 1
Enter the unit to convert from: kg
Enter the unit to convert to: oz
Result: 1.0 kg = 35.2740 oz

Choose an option:
1. Convert Length Units.
2. Convert Mass Units.
3. Convert Temperature Units.
Or enter (q)uit to exit.
> 3

Conveting temperature...
Available Units: Celsius, Fahrenheit, Kelvin
Enter the temperature value: 42
Enter the unit to convert from: Celsius
Enter the unit to convert to: Fahrenheit
Result: 42.0 Celsius = 107.60 Fahrenheit

Choose an option:
1. Convert Length Units.
2. Convert Mass Units.
3. Convert Temperature Units.
Or enter (q)uit to exit.
> q
Bye!
```