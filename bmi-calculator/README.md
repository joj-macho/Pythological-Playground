# BMI Calculator

## Description

BMI is a numerical value of a person's weight in relation to their height. It is used to classify individuals into different weight categories, indicating whether they are underweight, normal weight, overweight, or obese. 

This is a Python program to calculate Body Mass Index (BMI) based on the provided height and weight.

## How it Works

The BMI is calculated using the following formula: $BMI = \frac{\text{Weight (kg)}}{(\text{height (m)})^2} = \frac{\text{Weight (kg)}}{(\frac{\text{height (cm)}}{100})^2}$

- The `main()` function runs the program. It prompts the user to enter their height (in centimeters) and weight (in kilograms), then it calculates the BMI using `calculate_bmi` function by applying the above BMI formular, and displays the results of your BMI.

- The `classify_bmi(bmi)` function, which classifies the BMI based on the BMI value, returns a classification such as "Normal", "Overweight", "Obese Class I", etc.

## Program Input & Output

When you run the program `bmi_calculator.py`, the output will look like this:

```python

Welcome to the BMI Calculator!

Enter your height in cm: 100
Enter your weight in kg: 15

Your BMI is: 15.00
You are Severely Thin

.
.
.

Enter your height in cm: 100
Enter your weight in kg: 17

Your BMI is: 17.00
You are Mildly Thin

.
.
.

Enter your height in cm: 100
Enter your weight in kg: 26

Your BMI is: 26.00
You are Overweight

.
.
.

Enter your height in cm: 100
Enter your weight in kg: 45

Your BMI is: 45.00
You are Obese Class III
```