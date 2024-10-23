import random
import datetime
from collections import Counter


def main():
    '''Run the Birthday Problem.'''
    print('''The Birthday Problem.

The birthday paradox reveals that in a group of 23 people, there is about a
50% chance that at least two people will share the same birthday.

How likely is it for at least two people to havethe same birthday in a given
group size? Let's find out...
''')
    while True:
        num_of_people = get_user_input(
            'Enter the number of people in the group (1 - 100) '
            'or (q)uit to exit:\n> ', 1, 100)
        if num_of_people is None:
            break
        num_of_simulations = get_user_input(
            'Enter the number of simulations to run (1 - 1,000,000) '
            'or (q)uit to exit:\n> ', 1, 1000000)
        if num_of_simulations is None:
            break

        # Generate birthdays for group size
        birthdays = generate_birthdays(num_of_people)
        print(f'\n{len(birthdays)} birthdays randomly generated...')
        for birthday in birthdays:
            print(birthday.strftime('%d %B'), end=', ')
        print()

        # Any shared birthdays in birthdays?
        birthday_counts = Counter(birthdays)
        # print(f'Birthday counts: {birthday_counts}')
        shared_birthdays = {birthday: count for birthday, count in
                            birthday_counts.items() if count > 2}
        # print(f'Shared birthdays: {shared_birthdays}')
        print('\nIn this simulation run #0:')
        if shared_birthdays:
            for bday, count in shared_birthdays.items():
                print(f'{count} people share the same birthday, '
                      f'{bday.strftime("%d %B")}.')
        else:
            print('There are no shared birthdays.')

        input('\nPress Enter to start the Simulation...')

        print(f'\nSimulating {num_of_people} random birthdays '
              f'{num_of_simulations:,} times...\n')

        probability, matching_results = simulate_bday_problem(
            num_of_people, num_of_simulations)
        print()
        print('Simulation Results'.center(78, '-'))
        print(f'\nNumber of simulations performed: {num_of_simulations:,}')
        print(f'Number of simulations with at least one shared birthday: '
              f'{matching_results}')
        print(f'In a group of {num_of_people} people, the probability of '
              f'having at least two people with the same birthday is '
              f'{probability:.2%}.')
        print()


def get_user_input(prompt, min_val, max_val):
    '''Prompts the user for a valid positive integer.'''
    while True:
        response = input(prompt).strip().lower()
        if response in ('q', 'quit'):
            print('\nExiting simulator... Bye!')
            return None
        try:
            value = int(response)
            if not min_val <= value <= max_val:
                raise ValueError(
                    f'Value must be between {min_val} and {max_val}.')
            return value
        except ValueError as e:
            print(f'Invalid input: {e}\n')


def simulate_bday_problem(num_of_people, num_of_simulations):
    '''Simulates the birthday paradox for a group of people to estimate
    probabilites.'''
    num_of_duplicates = 0
    progress_interval = num_of_simulations // 10
    if progress_interval == 0:
        progress_interval = 1

    for i in range(num_of_simulations):
        birthdays = generate_birthdays(num_of_people)
        if len(birthdays) != len(set(birthdays)):  # Check for duplicates
            num_of_duplicates += 1

        if (i + 1) % (progress_interval) == 0:
            print(f'Progress: {(i + 1) * 100 / num_of_simulations:.0f}%')

    probability = num_of_duplicates / num_of_simulations
    return probability, num_of_duplicates


def generate_birthdays(num_of_people):
    '''Generates a list of random birthdays for a group of people.'''
    birthdays = []
    for _ in range(num_of_people):
        month = random.randint(1, 12)
        day = random.randint(1, 31)

        if month == 2 and day > 28:  # Handle leap years
            day = 28
        elif month in (4, 6, 9, 11) and day > 30:  # handle 30 days months
            day = 30

        birthday = datetime.date(2020, month, day)  # Year does not matter
        birthdays.append(birthday)
    return birthdays


if __name__ == '__main__':
    main()
