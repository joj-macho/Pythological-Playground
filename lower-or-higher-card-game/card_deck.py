import random

class Card:
    '''Class to represent a playing card.'''

    SUIT_SYMBOLS = {'Spades': chr(9824), 'Hearts': chr(9829), 'Clubs': chr(9827), 'Diamonds': chr(9830)}
    RANK_TUPLE = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self, rank, suit, value):
        '''
        Initializes a Card object.

        Parameters:
        - rank (str): The rank of the card (e.g. 'Ace', '2', 'Jack').
        - suit (str): The suit of the card (e.g. 'Hearts', 'Spades').
        - value (int): The numerical value of the card.

        Attributes:
        - rank (str): The rank of the card.
        - suit (str): The suit of the card.
        - value (int): The numerical value of the card.
        - card_name (str): A formatted string representing the card (e.g. 'Ace of Hearts').
        '''
        self.rank = rank
        self.suit = suit
        self.value = value
        self.card_name = f'{rank} of {self.SUIT_SYMBOLS[suit]}'
        
    def display_card(self):
        '''Display the ASCII art representation of the card.'''
        print(' ___ ')
        print(f'|{self.rank:<2} |')
        print(f'| {self.SUIT_SYMBOLS[self.suit]} |')
        print(f'|__{self.rank}|\n')

    def __str__(self):
        '''Returns a string representation of the card.'''
        return self.card_name

class Deck:
    '''Class to represent a deck of playing cards.'''

    SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')

    def __init__(self):
        '''
        Initializes a Deck object.

        Attributes:
        - all_cards (list): List to store all the cards in the deck.
        - remaining_cards (list): List to store the remaining cards to be played.
        '''
        self.all_cards = []
        self.remaining_cards = []

        self.generate_deck()
        self.shuffle_deck()

    def generate_deck(self):
        '''Generates a standard deck of 52 playing cards.'''
        for suit in self.SUIT_TUPLE:
            for value, rank in enumerate(Card.RANK_TUPLE):
                card = Card(rank, suit, value + 1)
                self.all_cards.append(card)

    def shuffle_deck(self):
        '''Shuffles the deck of cards.'''
        random.shuffle(self.all_cards)
        self.remaining_cards = self.all_cards.copy()

    def draw_card(self):
        '''Draws a card from the deck.'''
        return self.remaining_cards.pop() if self.remaining_cards else None
