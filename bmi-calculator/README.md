# BMI Calculator

## Description

BMI is a numerical value of a person's weight in relation to their height. It is used to classify individuals into different weight categories, indicating whether they are underweight, normal weight, overweight, or obese. 

This is a Python program to calculate Body Mass Index (BMI) based on the provided height and weight.

## How it Works

The BMI is calculated using the following formula: $BMI = \frac{\text{Weight (kg)}}{(\text{height (m)})^2} = \frac{\text{Weight (kg)}}{(\frac{\text{height (cm)}}{100})^2}$

- The `main()` function is defined. It starts by printing the welcome message and prompts the user to enter their height and height, then it calculates the BMI using `calculate_bmi` function, and displays the result along with the classification.

- The `calculate_bmi(height, weight)` function calculates BMI based on the given height (in cm) and weight (in kg) using the formular defined above.

- After calculating the BMI, the program calls the `classify_bmi(bmi)` function, which classifies the BMI based on the BMI value. It returns a classification such as "Normal", "Overweight", "Obese Class I", etc.

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