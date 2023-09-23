import random
import sys

# Game Card Constants 
NUM_OF_CARDS = 8
# Game Card Character Codes
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)


def main():
    '''Main game logic for Higher or Lower Card Game'''

    # Display game rules and instructions
    print('''
Welcome to Higher or Lower card game!

In this game, you have to choose whether the next card will be higher or lower than the current card.
    - Starting with 50 points...
    - If you guess correctly, you get 20 points
    - If you guess incorrectly, you lose 15 points

How to Play:
    - Enter (h)igher to guess higher card.
    - Enter (l)lower to guess lower card.
    - You can (q)uit to exit program.
    ''')

    # Generate the deck of cards
    deck = generate_card_deck()
    current_card = deck.pop()
    # Intitial Score
    score = 50
    
    while True:
        print('Starting card:')
        show_card(current_card)

        # Play game of 8 cards
        for _ in range(0, NUM_OF_CARDS):
            guess = input('Do you think the next card will be (h)igher or (l)ower? (q)uit to exit: ').lower()
            if guess == 'q':
                print('Bye!')
                sys.exit()
        
            next_card = deck.pop()
            print('Next Card is:')
            show_card(next_card)
        
            if guess == 'h':
                if next_card > current_card:
                    print('Correct! You guessed higher.')
                    score += 20
                else:
                    print('Wrong! The card is lower.')
                    score -= 15
            elif guess == 'l':
                if next_card < current_card:
                    print('Correct! You guessed lower.')
                    score += 20
                else:
                    print('Wrong! The card is higher.')
                    score -= 15


            print(f'Your Score: {score}.\n')

            current_card = next_card

        play_again = input('Press ENTER to play again, press (q)uit to exit: ').lower()
        if play_again.startswith('q'):
            break

def generate_card_deck():
    '''Generate card deck and return a list of tuples (rank, suit) for all 52 playing cards.'''

    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'K', 'Q', 'A'):
            deck.append((rank, suit))
    
    # Shuffle card deck
    random.shuffle(deck)

    return deck


def show_card(card):
    '''Display a card in a stylized format.'''

    rank, suit = card
    print(f' ___ ')
    print(f'|{rank:<2} |')
    print(f'| {suit} |')
    print(f'|__{rank}|\n')

    
if __name__ == '__main__':
    main()
