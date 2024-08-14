from card_deck import Card, Deck


def main():
    '''Play the Lower or Higher game.'''
    print('''Welcome to the Lower or Higher Card Game!

You start with 100 points. Gain 15 points for a correct answer, lose 10
points for an incorrect answer.

Game Rules:
    - You will be shown one card face up.
    - Each round, you guess whether the next card will be higher or lower.
    - Points are adjusted based on your guess.
    - The game ends when all cards are revealed.

Let's begin!
''')
    while True:
        deck = Deck()
        current_card = deck.deal_card()
        cards = [current_card] + [deck.deal_card() for _ in range(7)]
        player_points = 100
        cards_remaining = 7
        current_index = 0
        correct_guesses = 0
        incorrect_guesses = 0
        ties = 0

        for card in cards[1:]:  # Conceal all but the first card
            card.mark_concealed()

        while cards_remaining > 0:
            print(f'ATTEMPT {8 - cards_remaining}'.center(78, '-'))
            print(f'Current card: {current_card.get_name()}')
            Card.display_cards(cards[:8])

            # Get player guess
            guess = get_player_guess()
            if guess is None:
                print('\nExiting game... Bye!')
                return

            # Move to the next card
            current_index += 1
            next_card = cards[current_index]
            next_card.mark_revealed()

            if guess == 'h' and \
                    next_card.get_value() > current_card.get_value():
                print('\nCorrect! +15 Points.')
                print(f'The next card, {next_card.get_name()}, is higher.')
                player_points += 15
                correct_guesses += 1
            elif guess == 'l' and \
                    next_card.get_value() < current_card.get_value():
                print('\nCorrect! +15 Points.')
                print(f'The next card, {next_card.get_name()}, is lower.')
                player_points += 15
                correct_guesses += 1
            elif next_card.get_value() == current_card.get_value():
                print('\nIt\'s a Tie!')
                print(f'The next card, {next_card.get_name()} = current card.')
                ties += 1
            else:
                low_or_high = 'higher' if next_card.get_value(
                ) > current_card.get_value() else 'lower.'
                print('\nIncorrect! -10 Points.')
                print(f'The next card, {next_card.get_name()}, '
                      f'is {low_or_high}')
                player_points -= 10
                incorrect_guesses += 1

            current_card = next_card
            cards_remaining -= 1
            print(f'Your points: {player_points}')
            print(f'Cards remaining: {cards_remaining}\n')

        # Display the final game state
        print(f'Final card: {current_card.get_name()}')
        Card.display_cards(cards)

        print('GAME OVER!')
        print(f'Final Points: {player_points}', end=' | ')
        print(f'Correct Guesses: {correct_guesses}', end=' | ')
        print(f'Wrong Guesses: {incorrect_guesses}', end=' | ')
        print(f'Ties: {ties}')
        print()

        if correct_guesses == 7:
            print('Congratulations! You guessed all the cards correctly!\n')
        elif incorrect_guesses == 7:
            print('Unfortunately, you guessed all the cards incorrectly.\n')

        while True:
            play_again = input('Play again? Enter (y)es or (n)o:\n> ').lower()
            print()
            if play_again in ('y', 'yes'):
                print('Playing Another Round!')
                break
            elif play_again in ('n', 'no'):
                print('Exiting game... Bye!')
                return
            else:
                print('Invalid input. Enter (y)es or (n)o.')


def get_player_guess():
    '''Prompt the player for a valid guess.'''
    while True:
        prompt = 'Is the next card (l)ower or (h)igher? '
        exit = 'Enter (q)uit to exit.\n> '
        guess = input(prompt + exit).strip().lower()

        if guess in ('q', 'quit'):
            return None
        if guess in ('higher', 'h', 'lower', 'l'):
            return guess
        print()


if __name__ == '__main__':
    main()
