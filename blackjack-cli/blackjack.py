import random
import sys

# Game Card Character Codes
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

def main():
    '''
    This function is the entry point of the game.
    It starts the game with $5000 and runs in a while loop until the player cannot afford to continue playing or decides to exit.
    '''
    # The rules of the game
    print('''
Blackjack Card Game.

This game follows these simple rules:
    - Get as close to 21 without going over to win the game.
    - Kings, Queens, and Jacks are worth 10 points each.
    - Aces are worth 1 or 11 points.
    - Cards 2 through 10 are worth their face value.
    - The bet is returned to the player in case of a tie.
    - The dealer stops hitting at 17.
    - Enter (h)it to take another card.
    - Enter (s)tand to stop taking cards.
    - You can (d)ouble down on your first play to increase your bet + will hit one more time.
    ''')
    # The initial funds
    money = 5000
    # The Game loop
    while True:
        # Can you afford to play??
        if money <= 0:
            print('No funds to Continue Game.\nBye!')
            sys.exit()

        # The available funds
        print(f'Available Funds: ${money}')
        
        # Generate bet
        bet = generate_bet(money)

        # Player and Dealer Cards: Each gets two cards from the deck
        deck = generate_card_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        # Player Action
        print(f'Your bet is ${bet}\n')
        while True:
            show_hands(player_hand, dealer_hand, False)

            if generate_hand(player_hand) > 21:
                break

            move = generate_move(player_hand, money - bet)
            if move == 'd':
                additional_bet = generate_bet(min(bet, (money - bet)))
                bet += additional_bet
                print(f'Bet increased to {bet}')
                print(f'Your bet is ${bet}')

            if move in ('h', 'd'):
                new_card = deck.pop()
                rank, suit = new_card
                print(f'You drew a {rank} of {suit}')
                player_hand.append(new_card)

                if generate_hand(player_hand) > 21:
                    continue

            if move in ('s', 'd'):
                break

        # Dealer action
        if generate_hand(player_hand) <= 21:
            while generate_hand(dealer_hand) <= 17:
                print('Dealer hits.')
                dealer_hand.append(deck.pop())
                show_hands(player_hand, dealer_hand, False)

                if generate_hand(dealer_hand) > 21:
                    break
                input('Press Enter to continue.\n\n')

        # Final hand
        show_hands(player_hand, dealer_hand, True)
        player_cards_value = generate_hand(player_hand)
        dealer_cards_value = generate_hand(dealer_hand)
        if dealer_cards_value > 21:
            print(f'Dealer busts. You win ${bet}')
            money += bet
        elif player_cards_value > 21 or player_cards_value < dealer_cards_value:
            print('You lost.')
            money -= bet
        elif player_cards_value > dealer_cards_value:
            print(f'You won ${bet}')
            money += bet
        elif player_cards_value == dealer_cards_value:
            print('A tie! The bet is returned to you.')

        input('Press Enter to Continue...\n')


def generate_bet(betAmount):
    '''This function prompts the player for a bet and returns the bet,'''
    while True:
        bet = input(f'Enter bet amount between $1 - ${betAmount}. Enter (q)uit to exit.\n> ').lower()

        if bet.startswith('q'):
            print('Bye!')
            sys.exit()
        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= betAmount:
            return bet

def generate_card_deck():
    '''This function returns a list of tuples (rank, suit) for all 52 playing cards.'''
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'K', 'Q', 'A'):
            deck.append((rank, suit))

    random.shuffle(deck)

    return deck

def show_hands(player_hand, dealer_hand, show_dealer_hand):
    '''This function shows the player's and dealer's cards'''
    if show_dealer_hand:
        print('Dealer:', generate_hand(dealer_hand))
        show_cards(dealer_hand)
    else:
        print('Dealer: ???')
        show_cards(['backside'] + dealer_hand[1:])

    # Show player cards
    print('Player:', generate_hand(player_hand))
    show_cards(player_hand)

def generate_hand(cards):
    '''This function adds the cards and returns the value of the cards.'''
    value = 0
    num_of_aces = 0

    # Add card values following game rules
    for card in cards:
        rank = card[0]
        if rank == 'A':
            num_of_aces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    # Ace card = 1 point or 11 if can be added without exceeding 21
    value += num_of_aces
    for i in range(num_of_aces):
        if value + 10 <= 21:
            value += 10

    return value
        
def show_cards(cards):
    '''This function displays all the cards on hand'''
    rows = ['', '', '', '', '']

    # draw cards
    for i, card in enumerate(cards):
        rows[0] += ' ___ '  # top card line
        if card == 'backside':
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '  # bottom card line
        else:
            rank, suit = card
            rows[1] += f'|{rank.ljust(2)} |'  # top rank line
            rows[2] += f'| {suit} |'  # suit line
            rows[3] += f'|_{rank.rjust(2, "_")}|'  # bottom rank line

    # Print each row
    for row in rows:
        print(row)


def generate_move(player_hand, money):
    '''This function asks for player's move and returns 'h' for hit, 's' for stand, and 'd' for double down.'''
    # Player must enter correct move
    while True:
        moves = ['(h)it', '(s)tand']
        # Double down
        if len(player_hand) == 2 and money > 0:
            moves.append('(d)ouble down')

        # Player's move
        move = input(','.join(moves) + '\n> ').lower()
        if move in ('h', 's'):
            return move
        if move == 'd' and '(d)ouble down' in moves:
            return move

if __name__ == '__main__':
    main()