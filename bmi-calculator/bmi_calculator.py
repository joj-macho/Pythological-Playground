
def main():
    '''Main function for the BMI calculator.'''

    print('\nWelcome to the BMI Calculator!\n')

    # Input height and weight
    height = input('Enter your height in cm: ')
    weight = input('Enter your weight in kg: ')

    # Calculate BMI
    bmi = calculate_bmi(height, weight)

    # Display result
    classification = classify_bmi(bmi)
    print(f'\nYour BMI is: {bmi:.2f}')
    print(f'You are {classification}\n')


def calculate_bmi(height, weight):
    '''Calculate BMI based on height and weight.'''

    try:
        height_cm = float(height)
        weight_kg = float(weight)

        # BMI calculation
        bmi = weight_kg / ((height_cm / 100) ** 2)
        return bmi
    except ValueError:
        return None


def classify_bmi(bmi):
    '''Classify BMI based on given ranges.'''

    if bmi is None:
        return 'ERROR: Invalid input'

    if bmi < 16:
        return 'Severely Thin'
    elif 16 <= bmi < 17:
        return 'Moderately Thin'
    elif 17 <= bmi < 18.5:
        return 'Mildly Thin'
    elif 18.5 <= bmi < 25:
        return 'Normal'
    elif 25 <= bmi < 30:
        return 'Overweight'
    elif 30 <= bmi < 35:
        return 'Obese Class I'
    elif 35 <= bmi < 40:
        return 'Obese Class II'
    else:
        return 'Obese Class III'


if __name__ == '__main__':
    main()
