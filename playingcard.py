#a class that create a Card to play in BlackJack

class Card:
    """Attributes of Card class are as follows.
        INSTANCE VARIABLES:
        self.rank: card's rank
        self.suit: card's suit"""
    def __init__(self,rank,suit):
        self.rank = rank 
        self.suit = suit
        self.values = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:10,12:10,13:10}
        self.suits = {"d": "Diamonds","c": "Clubs","h": "Hearts","s": "Spades"}
        if rank == 11:
            self.name = "Jack of " + self.suits.get(suit)
        elif rank == 12:
            self.name = "Queen of " + self.suits.get(suit)
        elif rank == 13: 
            self.name = "King of " +  self.suits.get(suit)
        elif rank == 1:
            self.name = "Ace of " + self.suits.get(suit)
        else: 
            self.name = str(self.rank) + " of " + str(self.suits.get(suit))
    def getRank(self):
        return self.rank 
    def getSuit(self):
        return self.suit
    def getValue(self):
        return self.values.get(self.rank)
    def __str__(self):
        return str(self.name)


def main():
    card =  Card(10,"d")
    print(card.getValue())
    print(card.getSuit())

if __name__== "__main__":
    main()
    
        



        
