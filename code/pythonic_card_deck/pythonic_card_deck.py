#!/usr/bin/env python3
"""
project: Pythonic Card Deck
created:2021-10-19
@author:seraph
email:seraph776@gmail.com
"""


from collections import namedtuple
from random import choice

# namedtuple used to construct a simple class to represent individual cards:
Card = namedtuple('Card', ['rank', 'suit'])


class CardDeck:
    """A Deck class."""
    # develop 2 lists of ranks and suits:
    ranks: list = [str(n) for n in range(2, 11)] + list('JQKA')
    suits: list = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        """Initialize attributes."""
        # Develop complete deck of 52 cards:
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        # to get the length of the deck
        return len(self._cards)

    def __getitem__(self, position):
        # To support indexing and slicing:
        return self._cards[position]


def main():    
    deck = CardDeck()
    print(len(deck)) # 52
    print(deck[0])   # Card(rank='2', suit='spades')
    print(deck[0][0])  # 2
    print(deck[0][1])  # spades
    # Get a randoom card
    print(choice(deck))


if __name__ == '__main__':
    main()

 

