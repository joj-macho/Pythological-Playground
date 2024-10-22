import random


def main():
    '''Run the coin flip simulator N times.'''
    print('Welcome to the Coin Flip Simulator!\n')

    while True:
        response = input('Enter the number of coin flips to simulate. '
                         'Enter (q)uit to exit.\n> ')
        if response.strip().lower() in ('q', 'quit'):
            print('Bye!')
            break

        try:
            num_flips = int(response)
            if num_flips <= 0:
                raise ValueError('Please enter a positive integer.')
            if num_flips > 1_000_000:
                num_flips = 1_000_000
        except ValueError as e:
            print(f'Invalid input: {e}\n')
            continue

        # Start flipping
        print(f'\nSimulating {num_flips:,} coin flips...')
        heads, tails = simulate_coin_flips(num_flips)

        print('\n----------- Results -----------')
        print(f'Total Flips: {num_flips:,}')
        print(f'Heads: {heads:<5,} | P(H) = {(heads/num_flips)*100:.2f}%')
        print(f'Tails: {tails:<5,} | P(T) = {(tails/num_flips)*100:.2f}%')
        print('-' * 31)
        print()


def simulate_coin_flips(num_flips):
    '''Simulates flipping a coin num_tosses times.'''
    heads_count = 0
    tails_count = 0

    for _ in range(num_flips):
        if random.choice(['H', 'T']) == 'H':
            heads_count += 1
        else:
            tails_count += 1

    return heads_count, tails_count


if __name__ == '__main__':
    main()
