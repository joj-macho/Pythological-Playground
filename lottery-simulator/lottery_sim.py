import random

def main():
    '''Main function for the lottery simulation.'''

    print('''
Welcome to the Lottery Simulator!
This program simulates a lottery draw where you choose 5 numbers from 1 to 69 and a Powerball number from 1 to 26.
You can specify how many times you want to play and see the results.
    ''')

    while True:
        # Get user input for numbers, powerball, and number of plays
        numbers = get_user_numbers()
        powerball = get_user_powerball()
        num_plays = get_user_num_plays()

        # Simulate the lottery based on user inputs
        simulate_lottery(numbers, powerball, num_plays)

        # Ask the user if they want to play again
        play_again = input('Do you want to play again? Enter (y)es or (n)o: ').lower()
        if play_again == 'yes' or play_again == 'y':
            continue
        else:
            print('Thanks for playing!')
            break


def get_user_numbers():
    '''Prompt the user to enter 5 different numbers from 1 to 69.'''
    
    while True:
        print('Enter 5 different numbers from 1 to 69, separated by spaces:')
        response = input('> ')

        # Check that the player entered 5 items:
        numbers = response.split()
        if len(numbers) != 5:
            print('Please enter 5 numbers, separated by spaces.')
            continue

        # Convert the strings into integers:
        try:
            for i in range(5):
                numbers[i] = int(numbers[i])
        except ValueError:
            print('Please enter numbers, like 27, 35, or 62.')
            continue

        # Check that the numbers are between 1 and 69:
        for i in range(5):
            if not (1 <= numbers[i] <= 69):
                print('The numbers must all be between 1 and 69.')
                continue

        # Check that the numbers are unique:
        if len(set(numbers)) != 5:
            print('You must enter 5 different numbers.')
            continue

        return numbers


def get_user_powerball():
    '''Prompt the user to enter a Powerball number from 1 to 26.'''

    while True:
        print('Enter the Powerball number from 1 to 26:')
        response = input('> ')

        # Convert the string into an integer:
        try:
            powerball = int(response)
        except ValueError:
            print('Please enter a number, like 3, 15, or 22.')
            continue

        # Check that the number is between 1 and 26:
        if not (1 <= powerball <= 26):
            print('The Powerball number must be between 1 and 26.')
            continue

        return powerball


def get_user_num_plays():
    '''Prompt the user to enter the number of times they want to play.'''

    while True:
        print('How many times do you want to play? (Max: 1000000)')
        response = input('> ')

        # Convert the string into an integer:
        try:
            num_plays = int(response)
        except ValueError:
            print('Please enter a number, like 3, 15, or 22000.')
            continue

        # Check that the number is between 1 and 1_000_000:
        if not (1 <= num_plays <= 1_000_000):
            print('You can play between 1 and 1_000_000 times.')
            continue

        return num_plays


def simulate_lottery(numbers, powerball, num_plays):
    '''Simulate the lottery draw and display results.'''

    # Calculate the total cost for the specified number of plays
    price = f'${2 * num_plays}'
    print(f'If the cost of the lotto ticket is $2. It would cost {price} to play {num_plays} times...\nNow then let\' get our gambling freak on!')
    input('Press Enter to start...')
    print()

    # Initialize variables to track hits and maximum hits
    hits = {}
    max_hits = 0

    # Initialize the list of possible lottery numbers
    possible_numbers = list(range(1, 70))

    # Simulate each play
    for i in range(num_plays):
        # Generate winning lottery numbers
        random.shuffle(possible_numbers)
        winning_numbers = possible_numbers[0:5]
        winning_powerball = random.randint(1, 26)

        # Check for matching numbers and powerball
        matching_numbers = set(numbers).intersection(set(winning_numbers))
        num_matching_numbers = len(matching_numbers)
        hit_powerball = powerball == winning_powerball

        # Check if the player won the lottery
        if num_matching_numbers == 5 and hit_powerball:
            print(f'You won the Powerball Lottery on attempt {i + 1}!')

        # Update hit records
        if num_matching_numbers in hits:
            hits[num_matching_numbers].append((winning_numbers, i + 1, hit_powerball))
        else:
            hits[num_matching_numbers] = [(winning_numbers, i + 1, hit_powerball)]

        # Update maximum hits
        max_hits = max(max_hits, num_matching_numbers)

        # Print progress for long simulations
        if 1 <= num_plays <= 10_000 and i % num_plays == 0:
            print(f'{num_plays} Simulations Completed...')
        if 10_000 < num_plays <= 100_000 and i % 10_000 == 0:
            print(f'{i} Simulations Completed...')
        if 100_000 < num_plays <= 1_000_000 and i % 100_000 == 0:
            print(f'{i} Simulations Completed...')

    # Print final results
    print()
    print_results(price, hits, max_hits, num_plays, numbers, powerball)


def print_results(price, hits, max_hits, num_plays, numbers, powerball):
    '''Print the simulation results.'''

    # Print a message indicating simulation completion for long simulations
    if 10_000 < num_plays <= 100_000:
        print(f'{num_plays} Simulations Completed...\n')

    # Generate a string representation of the chosen numbers
    your_numbers = ', '.join(map(str, numbers)) + f', ({powerball}-Powerball Number)'

    # Print the player's chosen numbers and the total number of simulations
    print(f'Your numbers: {your_numbers}')
    print(f'Out of {num_plays} Simulations...')

    # Iterate through hits and print details for each hit
    for num_matching_numbers, matches in sorted(hits.items(), reverse=True):
        num_hits = len(matches)

        # Generate a string representation of matching numbers and attempts
        match_str = '\n    '.join([f'Attempt {match[1]}: {" ".join(map(str, match[0]))}' for match in matches])

        # Print the number of hits and the matching numbers for up to 20 hits
        if num_matching_numbers == 0:
            print(f'\n{num_hits} Simulations matched {num_matching_numbers} numbers.')
        if num_matching_numbers > 0 and num_hits <= 20:
            print(f'\n{num_hits} Simulations matched {num_matching_numbers} numbers:')
            print(f'    {match_str}')
        if num_matching_numbers > 0 and num_hits > 20:
            print(f'\n{num_hits} Simulations matched {num_matching_numbers} numbers:')

    # Print the maximum number of hits
    print(f'\nMaximum Hits: {max_hits} numbers\n')


if __name__ == '__main__':
    main()
