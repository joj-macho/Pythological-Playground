from card_deck import Deck

def main():
    '''Main function to play the Higher or Lower card game.'''

    print('''
Welcome to the Higher or Lower Card Game!

Rules:
    - Guess whether the next card will be higher or lower than the current card.
    - Correct guesses earn 20 points, incorrect guesses result in a loss of 15 points.
    - The game starts with a score of 50 points.''')

    deck = Deck()
    score = 50  # Initial score

    while True:
        print()
        current_card = deck.draw_card()
        print('Starting card:')
        current_card.display_card()
        print()

        for _ in range(8):  # play one game with 8 cards
            while True:
                answer = input(f'Will the next card be (h)igher or (l)ower than the current card ({current_card})?\nPress "h" for higher, "l" for lower\n> ').lower()

                if answer in {'h', 'l'}:
                    break
                else:
                    print('Invalid input. Please enter "h" for higher or "l" for lower.\n')

            next_card = deck.draw_card()
            print('Next card:')
            next_card.display_card()

            if (answer == 'h' and next_card.value > current_card.value) or (answer == 'l' and next_card.value < current_card.value):
                print(f"Correct! {next_card} is {'higher' if answer == 'h' else 'lower'} than {current_card}.\nYou earned 20 points.")
                score += 20
            else:
                print(f"Wrong! {next_card} is {'lower' if answer == 'h' else 'higher'} than {current_card}.\nYou lost 15 points.")
                score -= 15

            print('Your current score:', score)
            print()
            current_card = next_card

        print(f'Game Over!\nYour final score is {score}.\n')

        play_again = input('To play again, press ENTER, or "q" to quit:\n> ').lower()
        if play_again == 'q':
            break

    print('Thank you for playing! Goodbye!')

if __name__ == '__main__':
    main()