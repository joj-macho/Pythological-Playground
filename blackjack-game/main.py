from card_deck import Card, Deck


def main():
    '''Play the Blackjack game.'''
    print('''Welcome to the Blackjack Card Game!

The aim is to get as close to 21 without going over. Here are the rules:
    - Kings, Queens, and Jacks are worth 10 points each.
    - Aces can be worth 1 or 11 points, depending on your hand total.
    - Cards 2 through 10 are valued at their face value.
    - The dealer stops hitting at <= 17.

Now, let's get our gambling freak on!
''')

    player_funds = 100
    wins, losses = 0, 0

    while True:  # Main game loop
        # Initial game objects
        deck = Deck()
        player_hand = []
        dealer_hand = []

        # Can you affor to play?
        if player_funds <= 0:
            print('No funds to continue the game!')
            break

        print(f'Player Funds: {player_funds}')

        # Make a bet
        bet_amount = get_bet(player_funds)
        if bet_amount is None:
            print('Exiting game... Bye!')
            break

        print(f'Your bet is {bet_amount}\n')

        # Deal initial cards
        print('Initial Hands:'.center(79, '-'))
        for _ in range(2):
            player_hand.append(deck.deal_card())
            dealer_hand.append(deck.deal_card())
        dealer_hand[0].mark_concealed()

        display_hands(player_hand, dealer_hand)

        while True:  # Player action
            # Check if player bust
            if calculate_hand_value(player_hand) > 21:
                break

            # Player Move
            funds_after_bet = player_funds - bet_amount
            player_move = get_player_move(player_hand, funds_after_bet)

            if player_move in ('d', 'double-down'):
                bet_amount *= 2
                print(f'Bet Doubled to {bet_amount}')

            if player_move in ('h', 'hit', 'd', 'double-down'):
                print()
                print('----- Player Move: Hit -----'.center(79))
                player_hand.append(deck.deal_card())  # Hit
                display_hands(player_hand, dealer_hand)

                if calculate_hand_value(player_hand) > 21:
                    continue

            if player_move in ('s', 'stand', 'd', 'double-down'):
                break

        # Dealer Move
        if calculate_hand_value(player_hand) <= 21:
            # dealer_hand[0].mark_revealed()
            dealer_hits = 0
            while calculate_hand_value(dealer_hand) < 17:
                print('----- Dealer Move: Hit -----'.center(79))
                dealer_hand.append(deck.deal_card())
                dealer_hits += 1
                # dealer_hand[dealer_hits + 1].mark_concealed()
                display_hands(player_hand, dealer_hand)

                if calculate_hand_value(dealer_hand) > 21:
                    break

                input('Dealer Move... Press Enter to continue...\n')

        # Show final hands
        print('----- Final Hands -----'.center(79))
        display_hands(player_hand, dealer_hand, reveal_dealer=True)

        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)
        if dealer_value > 21:
            print('Dealer Busts! You win!')
            player_funds += bet_amount
            wins += 1
        elif player_value < dealer_value:
            print('You Lost!')
            player_funds -= bet_amount
            losses += 1
        elif player_value > 21:
            print('Player Busts! Dealer Wins')
            player_funds -= bet_amount
            losses += 1
        elif player_value > dealer_value:
            print('You won!')
            player_funds += bet_amount
            wins += 1
        elif player_value == dealer_value:
            print('It\'s a Tie!')

        # Scores
        print(f'\nWins: {wins} | Losses: {losses}')


def get_bet(player_funds):
    '''Gets a valid bet from the player.'''
    while True:
        bet = input('\nEnter your bet or enter (q)uit to exit:\n> ')
        if bet in ('q', 'quit'):
            return None

        try:
            bet_amount = float(bet)
            if bet_amount <= 0:
                raise ValueError('Enter a valid positive bet amount!')
            elif bet_amount > player_funds:
                raise ValueError(f'Enter bet <= {player_funds}.')
            return bet_amount
        except ValueError as e:
            print(f'Invalid input: {e}\n')


def display_hands(player_hand, dealer_hand, reveal_dealer=False):
    '''Displays the player and dealer hands'''
    print(f'\nPlayer\'s Hand: {calculate_hand_value(player_hand)}')
    Card.display_cards(player_hand)

    if reveal_dealer:
        print(f'Dealer\'s Hand: {calculate_hand_value(dealer_hand)}')
        dealer_hand[0].mark_revealed()
    else:
        print('Dealer\'s Hand: ???')
    Card.display_cards(dealer_hand)


def calculate_hand_value(hand):
    '''Calculates the total hand value.'''
    value = sum(card.get_value() for card in hand)
    num_of_aces = sum(1 for card in hand if card.get_rank() == 'A')

    while value > 21 and num_of_aces > 0:
        value -= 10
        num_of_aces -= 1
    return value


def get_player_move(player_hand, remaining_funds):
    '''Prompts for for valid move.'''
    while True:
        moves = ['(h)it', '(s)tand']
        if len(player_hand) == 2 and remaining_funds > 0:
            moves.append('(d)ouble-down')

        prompt = 'Enter ' + ', '.join(moves) + '\n> '
        player_move = input(prompt).lower()

        if player_move in ('h', 'hit', 's', 'stand'):
            return player_move
        if player_move in ('d', 'double-down') and '(d)ouble-down' in moves:
            return player_move


if __name__ == '__main__':
    main()
