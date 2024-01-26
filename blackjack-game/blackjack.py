import sys
from card_deck import Deck

class BlackjackGame:
    def __init__(self):
        self.player_hand = []
        self.dealer_hand = []
        self.deck = Deck()
        self.player_score = 0
        self.dealer_score = 0
        self.player_funds = 1000  # Intial player funds

    def get_player_bet(self, player_funds):
        '''Prompt the player to enter a valid bet amount.'''
        while True:
            bet = input(f'Enter bet amount between $1 - ${player_funds}. Enter (q)uit to exit.\n> ').lower()

            if bet.startswith('q'):
                print('Bye!')
                sys.exit()
            if not bet.isdecimal():
                continue

            bet = int(bet)
            if 1 <= bet <= self.player_funds:
                return bet

    def display_hands(self, show_dealer_hand=False):
        '''Display the current hands of the dealer and player.'''
        # Display Dealer's Hand
        if show_dealer_hand:
            print('Dealer:', self.calculate_hand_value(self.dealer_hand))
            for card in self.dealer_hand:
                card.display_card()
            print()
        else:
            print('Dealer: ???')
            # Only display the first card of the dealer if not showing all cards
            self.dealer_hand[0].display_card(show_backside=True)
            for card in self.dealer_hand[1:]:
                card.display_card()
            print()
        
        # Display Player's Hand
        print('Player:', self.calculate_hand_value(self.player_hand))
        for card in self.player_hand:
            card.display_card()
        print()

    def calculate_hand_value(self, hand):
        '''Calculate the total value of a hand, considering the value of each card.'''
        value = 0
        num_of_aces = 0

        for card in hand:
            rank = card.rank
            if rank == 'A':
                num_of_aces += 1
            elif rank in ('K', 'Q', 'J'):
                value += 10
            else:
                value += int(rank)

        value += num_of_aces
        for i in range(num_of_aces):
            if value + 10 <= 21:
                value += 10

        return value

    def get_player_move(self):
        '''Prompt the player to choose a move.'''
        while True:
            move = input('Choose your move: (h)it, (s)tand, or (d)ouble down\n> ').lower()

            if move in ('h', 's', 'd'):
                return move
            else:
                print('Invalid input. Please enter (h)it, (s)tand, or (d)ouble down.')

def main():
    '''Main function for the Blackjack Card Game.'''
    print('''
Welcome to the Blackjack Card Game!

The aim is to get as close to 21 without going over. Let's go over the rules:
  - Kings, Queens, and Jacks are worth 10 points each.
  - Aces can be worth 1 or 11 points.
  - Cards 2 through 10 are valued at their face value.
  - The dealer stops hitting at 17.
  - If you tie with the dealer, your bet is returned.

Now, Let's get our gambling freak on!
''')

    game = BlackjackGame()

    while True:
        # Can you afford to play?
        if game.player_funds <= 0:
            print('No funds to Continue Game.\nBye!')
            sys.exit()

        print(f'Your Available Funds: ${game.player_funds}')

        bet_amount = game.get_player_bet(game.player_funds)

        # Player and Dealer Cards
        game.player_hand = [game.deck.draw_card(), game.deck.draw_card()]
        game.dealer_hand = [game.deck.draw_card(), game.deck.draw_card()]

        print(f'\nYour bet is ${bet_amount}\n')

        # Player action
        while True:
            print('\n------ Current Hands ------\n')
            game.display_hands()

            if game.calculate_hand_value(game.player_hand) == 21:
                print('BLACKJACK! You Win.')
                break

            if game.calculate_hand_value(game.player_hand) > 21:
                print('Player busts! You lose.')
                break

            move = game.get_player_move()

            if move == 'd':
                additional_bet = game.get_player_bet(min(bet_amount, game.player_funds - bet_amount))
                bet_amount += additional_bet
                print(f'\nYour bet has been increased to ${bet_amount}')

            if move in ('h', 'd'):
                game.player_hand.append(game.deck.draw_card())

                if game.calculate_hand_value(game.player_hand) > 21:
                    continue

            if move in ('s', 'd'):
                break

        # Dealer action
        if game.calculate_hand_value(game.player_hand) <= 21:
            while game.calculate_hand_value(game.dealer_hand) < 17:
                print('Dealer is drawing...\n')
                game.dealer_hand.append(game.deck.draw_card())
                game.display_hands()

                if game.calculate_hand_value(game.dealer_hand) > 21:
                    break
                input('\nPress Enter to Continue')
                print()

        # Final Hands
        print('\n------ Final Hands ------\n')
        game.display_hands(show_dealer_hand=True)

        player_hand_value = game.calculate_hand_value(game.player_hand)
        dealer_hand_value = game.calculate_hand_value(game.dealer_hand)

        if dealer_hand_value > 21:
            print('Dealer Busts!')
            print(f'You win ${bet_amount}')
            game.player_score += 1
            game.player_funds += bet_amount
        elif player_hand_value > 21 or player_hand_value < dealer_hand_value:
            print('You lose!')
            game.dealer_score += 1
            game.player_funds -= bet_amount
        elif player_hand_value > dealer_hand_value:
            print(f'You won ${bet_amount}')
            game.player_score += 1
            game.player_funds += bet_amount
        elif player_hand_value == dealer_hand_value:
            print('It\'s a tie! The bet is returned to you.')

        print(f'\nPlayer Wins: {game.player_score} | Dealer Wins: {game.dealer_score}')
        print(f'Your Total Funds: ${game.player_funds}\n')

        # Play again??
        play_again = input('Do you want to play another round? (y/n)\n> ').lower()

        if play_again != 'y':
            print('Thanks for playing!\nBye!')
            sys.exit()

if __name__ == '__main__':
    main()