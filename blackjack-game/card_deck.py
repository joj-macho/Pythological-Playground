import random


class Card:
    SUITS = {'Spades': chr(9824), 'Hearts': chr(9829), 'Clubs': chr(9827),
             'Diamonds': chr(9830)}
    RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self, rank, suit):
        '''
        Initialize a new playing card with rank and suit.

        Parameters:
            rank (str): The rank of the card
            suit (str): The suit of the card
        '''
        self.rank = rank
        self.suit = suit
        self.symbol = Card.SUITS[suit]
        self.value = self._get_value()
        self.concealed = False  # Init card is facing up

    def _get_value(self):
        '''Determine the value of the card based on its rank.'''
        if self.rank in ('J', 'Q', 'K'):
            return 10
        elif self.rank == 'A':
            return 11  # 11 or 1
        else:
            return int(self.rank)

    def get_name(self):
        '''Get the name of the card.'''
        return f'{self.rank} of {self.suit} {self.symbol}'

    def get_rank(self):
        '''Get the rank of the card.'''
        return self.rank

    def get_value(self):
        '''Get the value of the card.'''
        return self.value

    def mark_concealed(self):
        '''Mark the card as concealed (face down).'''
        self.concealed = True

    def mark_revealed(self):
        '''Mark the card as revealed (face up).'''
        self.concealed = False

    def display_card(self):
        '''Display the card.'''
        if self.concealed:
            # print('**********')
            return '**********'
        else:
            # print(f'{self.rank} of {self.suit}')
            return f'{self.rank} of {self.suit} {self.symbol}'

    def __repr__(self):
        '''String representation of the card.'''
        return self.get_name()

    @classmethod
    def display_cards(cls, cards):
        '''Display all the cards ASCII art in the given list of cards.'''
        rows = ['', '', '', '', '']

        for card in cards:
            rows[0] += ' ___  '  # Top line of the card.
            if card.concealed:
                rows[1] += '|## | '
                rows[2] += '|###| '
                rows[3] += '|_##| '
            else:
                rank = card.get_rank()
                suit = card.symbol
                rows[1] += '|{} | '.format(rank.ljust(2))
                rows[2] += '| {} | '.format(suit)
                rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

        for row in rows:
            print(row)


class Deck:
    '''Represents a deck of 52 playing cards.'''

    def __init__(self):
        '''Initialize a new deck with 52 cards.'''
        self.cards = []
        self.reset_cards()

    def reset_cards(self):
        '''Reset and shuffle the deck with 52 cards.'''
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)

    def deal_card(self):
        '''Deal a card from the deck.'''
        if len(self.cards) == 0:
            raise IndexError('Deck is empty, cannot deal card.')
        return self.cards.pop()

    def cards_left(self):
        '''Get the number of cards left in the deck.'''
        return len(self.cards)


# Sanity Check
if __name__ == '__main__':
    # Creating cards
    card1 = Card('A', 'Spades')
    card2 = Card('10', 'Hearts')
    card3 = Card('K', 'Diamonds')
    card4 = Card('5', 'Clubs')
    card5 = Card('Q', 'Spades')

    # Initial card states
    print('Initial card state:')
    print('Card 1:', card1.display_card())
    print('Card 2:', card2.display_card())
    print('Card 3:', card3.display_card())
    print('Card 4:', card4.display_card())
    print('Card 5:', card5.display_card())

    # Test getter methods
    print('\nTesting getter methods:')
    print('Card 1 name:', card1.get_name())
    print('Card 1 rank:', card1.get_rank())
    print('Card 1 value:', card1.get_value())

    print('Card 5 name:', card5.get_name())
    print('Card 5 rank:', card5.get_rank())
    print('Card 5 value:', card5.get_value())

    # Concealing and revealing cards
    card3.mark_concealed()
    print('\nConceal card 3:', card3.display_card())
    card3.mark_revealed()
    print('Reveal card 3:', card3.display_card())
    card4.mark_concealed()
    print('Conceal card 4:', card4.display_card())

    # Display cards ASCII art
    cards = [card1, card2, card3, card4, card5]
    print('\nDisplay all card ASCII art:')
    Card.display_cards(cards)
