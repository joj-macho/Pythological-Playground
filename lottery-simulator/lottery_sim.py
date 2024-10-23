import random
from collections import defaultdict


def main():
    '''Run the lottery simulator.'''
    print('''The Lottery Simulator.

Test your luck by choosing 5 unique numbers between 1 and 69,
along with a Powerball number between 1 and 26.

The program will run multiple simulations to see how often your chosen numbers
match the randomly drawn numbers and Powerball.

Will you hit the jackpot or waste your time and money? Let's find out...
''')

    while True:
        # Get user input
        numbers = get_lottery_numbers()
        if numbers is None:
            break
        powerball = get_powerball()
        if powerball is None:
            break
        num_of_simulations = get_num_simulations()
        if num_of_simulations is None:
            break

        input('\nPress Enter to Start Simulation...')
        # Generate lottery numbers
        results = simulate_lottery(numbers, powerball, num_of_simulations)

        # Print simulation results
        print()
        match_counts = defaultdict(int)
        powerball_matches = 0
        best_match = {'matched numbers': 0, 'matched powerball': False,
                      'drawn numbers': [], 'drawn powerball': 0}
        best_match_simulation = None
        picked_numbers = ', '.join(map(str, sorted(numbers)))

        for i, result in enumerate(results):
            matched_numbers = result[1]['matched numbers']
            matched_powerball = result[1]['matched powerball']
            match_counts[matched_numbers] += 1

            if matched_powerball:
                powerball_matches += 1

            if (matched_numbers > best_match['matched numbers'] or
                    (matched_numbers == best_match['matched numbers'] and
                        matched_powerball)):
                best_match = result[1]
                best_match_simulation = i + 1

        print(' Simulation Results '.center(50, '-'))
        print(f'Your Lottery Numbers + Powerball: {picked_numbers} + '
              f'{powerball}')
        print(f'Number of simulations: {num_of_simulations:,}\n')

        for match, count in sorted(match_counts.items(), reverse=True):
            if match == 1 and powerball_matches > 0:
                print(f'{count} Simulations matched {match} number and the '
                      'Powerball.')
            else:
                print(f'{count} Simulations matched {match} numbers.')

        if best_match_simulation is not None:
            print(f'\nMax number of matches: {best_match["matched numbers"]} '
                  'numbers.')

            print(f'Simulation #{best_match_simulation} numbers: '
                  f'{", ".join(map(str, best_match["drawn numbers"]))} + '
                  f'{best_match["drawn powerball"]} and '
                  f'{match_counts[best_match["matched numbers"]] - 1} other '
                  f'simulation(s) matched {best_match["matched numbers"]} '
                  'numbers.')
        print('\n' + '-'*50)
        print()


def get_lottery_numbers():
    '''Prompts for 5 unique numbers between 1 and 69.'''
    while True:
        print('Enter 5 unique numbers from 1 to 69, separated by spaces. '
              'Enter (q)uit to exit.')
        response = input('> ').strip().lower()
        if response in ('q', 'quit'):
            print('Exiting program... Bye!')
            return None

        numbers = response.split()
        # Check for 5 numbers
        if len(numbers) != 5:
            print('Enter 5 numbers (separated by spaces)!\n')
            continue

        try:
            numbers = [int(num) for num in numbers]
        except ValueError:
            print('Enter valid integer numbers!\n')
            continue

        # Check if numbers between 1 and 69
        if any(num < 1 or num > 69 for num in numbers):
            print('The numbers must be between 1 and 69!\n')
            continue

        # CHeck if numbrs are unique
        if len(set(numbers)) != 5:
            print('Enter 5 unique numbers!\n')
            continue

        return numbers


def get_powerball():
    '''Prompts for a powerball number between 1 and 26.'''
    while True:
        print('Enter the Powerball number from 1 to 26. '
              'Enter (q)uit to exit.')
        response = input('> ').strip().lower()
        if response in ('q', 'quit'):
            print('Exiting program...Bye!')
            return None

        try:
            powerball = int(response)
        except ValueError:
            print('Enter a valid integer powerball number!\n')
            continue

        # Check if number between 1 and 26
        if not (1 <= powerball <= 26):
            print('Enter powerball number between 1 and 26!\n')
            continue

        return powerball


def get_num_simulations():
    '''Promts for valid number of simulations.'''
    while True:
        print('Enter the number of simulations < 1,000,000. '
              'Enter (q)uit to exit.')
        response = input('> ').strip().lower()
        if response in ('q', 'quit'):
            print('Exiting program...Bye!')
            return None

        try:
            num_simulations = int(response)
        except ValueError:
            print('Enter a valid integer number of simulations!\n')
            continue

        # Check for num_sim between 1 and 1,000,000
        if not (1 <= num_simulations <= 1000000):
            print('Enter number of simulations between 1 and 1,000,000!\n')
            continue

        return num_simulations


def simulate_lottery(numbers, powerball, num_simulations):
    '''Simulates the lottery draw.'''
    simulation_results = []
    # Show progress creen
    progress_interval = num_simulations // 10
    if progress_interval == 0:
        progress_interval = 1

    for i in range(num_simulations):
        drawn_numbers, drawn_powerball = generate_lottery_numbers()
        matches = check_matches(numbers, powerball,
                                drawn_numbers, drawn_powerball)
        matches['drawn numbers'] = drawn_numbers
        matches['drawn powerball'] = drawn_powerball
        simulation_results.append((i, matches))

        if (i + 1) % progress_interval == 0:
            progress_perc = (i + 1) * 100 / num_simulations
            print(f'Progress: {progress_perc:.0f}%')

    return simulation_results


def generate_lottery_numbers():
    '''Generates a set of random lottery numbers.'''
    numbers = random.sample(range(1, 70), 5)
    powerball = random.randint(1, 26)
    return numbers, powerball


def check_matches(numbers, powerball, drawn_numbers, drawn_powerball):
    '''Checks how many numbers match between the picked and drawn numbers.'''
    num_matched_numbers = len(set(numbers) & set(drawn_numbers))
    matched_powerball = powerball == drawn_powerball
    matches = {'matched numbers': num_matched_numbers,
               'matched powerball': matched_powerball}
    return matches


if __name__ == '__main__':
    main()
