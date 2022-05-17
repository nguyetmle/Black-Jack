#a class that generates a deck of cards

from playingcard import Card
from random import shuffle
from graphics import *

class Deck:
    """Attributes of Deck class are as follows.
        INSTANCE VARIABLES:
        self.cards: a list of all cards in deck"""
    def __init__(self):
        """create a deck of 52 cards in standard order"""
        self.cards = []
        for suit in ["s","c","h","d"]:
            for rank in range(1,14):
                self.cards.append(Card(rank,suit))

    def shuffle(self):
        """randomize the order the cards"""
        shuffle(self.cards)
        return self.cards

    def dealCard(self):
        """return the first card in the deck and remove that card"""
        return self.cards.pop(0)

    def cardsLeft(self):
        return str(len(self.cards))


def main():
    deck = Deck()
    deck.shuffle()
    deck.printDeck()
    card = deck.dealCard()
    print(card)
    print(deck.cardsLeft())

if __name__== "__main__":
    main()



