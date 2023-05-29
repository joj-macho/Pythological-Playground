import random

TICKET_COST = 2
JACKPOT_AMOUNT = 500000000
MAX_PLAYS = 1000000

def main():
    '''Main function that simulates the Powerball Lottery game.'''
    
    print('\nWelcome to the Powerball Lottery Simulator!\n')
    print('Experience the excitement of the Powerball Lottery without spending a dime.\n')
    print(f'Each Powerball lottery ticket typically costs $2, and the current jackpot stands at ${JACKPOT_AMOUNT}.')
    print('However, with odds of 1 in 292,201,338, winning the jackpot is extremely unlikely.\n')
    print('This simulation allows you to enjoy the thrill of playing without the financial risk.\n')


    while True:
        numbers = get_numbers()
        powerball = get_powerball()
        num_of_plays = get_num_of_plays()
        simulate_lottery(numbers, powerball, num_of_plays)

        replay = input('\nDo you want to play again? Enter (y)es/(n)o:\n> ')
        if replay.lower() != 'yes':
            break

    print('Thanks for playing!')

def get_numbers():
    '''Prompt the user to enter 5 different numbers from 1 to 69.'''
    
    while True:
        response = input('Enter 5 different numbers from 1 to 69, separated by spaces:\n> ')
        numbers = response.split()

        if len(numbers) != 5:
            print('Please enter 5 numbers.')
            continue

        try:
            numbers = [int(num) for num in numbers]
        except ValueError:
            print('Please enter numbers only.')
            continue

        if not all(1 <= num <= 69 for num in numbers):
            print('The numbers must be between 1 and 69.')
            continue

        if len(set(numbers)) != 5:
            print('You must enter 5 different numbers.')
            continue

        return numbers

def get_powerball():
    '''Prompt the user to enter the powerball number from 1 to 26.'''
    
    while True:
        response = input('Enter the powerball number from 1 to 26:\n> ')

        try:
            powerball = int(response)
        except ValueError:
            print('Please enter a number.')
            continue

        if not (1 <= powerball <= 26):
            print('The powerball number must be between 1 and 26.')
            continue

        return powerball

def get_num_of_plays():
    '''Prompt the user to enter the number of times they want to play.'''
    
    while True:
        response = input('How many times do you want to play? (Max: 1000000):\n> ')

        try:
            num_of_plays = int(response)
        except ValueError:
            print('Please enter a number.')
            continue

        if not (1 <= num_of_plays <= MAX_PLAYS):
            print('You can play between 1 and', MAX_PLAYS, 'times.')
            continue

        return num_of_plays

def simulate_lottery(numbers, powerball, num_of_plays):
    '''Simulate the lottery draw and check if the user has won.'''
    
    price = TICKET_COST * num_of_plays
    print('\nIt costs $', price, 'to play', num_of_plays, 'times, but don\'t')
    print('worry. I\'m sure you\'ll win it all back.')
    input('Press Enter to start...')

    possibleNumbers = list(range(1, 70))
    for _ in range(num_of_plays):
        random.shuffle(possibleNumbers)
        winning_numbers = possibleNumbers[:5]
        winning_powerball = random.randint(1, 26)

        print('\nThe winning numbers are:', end=' ')
        all_winning_nums = ' '.join(str(num) for num in winning_numbers)
        print(all_winning_nums, 'and', winning_powerball, end='')

        if set(numbers) == set(winning_numbers) and powerball == winning_powerball:
            print('\nYou have won the Powerball Lottery! Congratulations,')
            print('you would be a billionaire if this was real!')
            break
        else:
            print('You lost.')

    print('\nYou have wasted $', price)
    
if __name__ == '__main__':
    main()
