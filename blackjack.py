#a class that simulates BlackJack game

from button import Button
from deck import Deck
from playingcard import Card
from graphics import *

class Blackjack:
    """"Attributes of Blackjack class are as follows.
       INSTANCE VARIABLES
        dealerHand: a list of PlayingCard objects representing the dealer's hand
        playerHand: a list of PlayingCard objects representing the player's hand
        playingDeck: a Deck object representing the deck of cards the game is being played with"""
    def __init__(self, dHand=[], pHand=[]):
        """Create a deck of cards, then shuffle it
            Initiate list to contains the hands of player and dealer"""
        self.deck = Deck()
        self.deck.shuffle()
        self.dHand = dHand
        self.pHand = pHand
        self.hideCard = Image(Point(0,0),"img/b2fv.gif")

    def initDeal(self, window, dPoint, pPoint):
        """Deal out first two cards to player and dealer
            Display player and dealer hands on graphical win
            Hide the first card of dealer"""
        #deal cards to player
        playerCard1 = self.deck.dealCard()
        self.pHand.append(playerCard1)
        playerCard2 = self.deck.dealCard()
        self.pHand.append(playerCard2)
        px = pPoint.getX()
        py = pPoint.getY()
        for card in self.pHand:
            suit = card.getSuit()
            rank = card.getRank()
            px = px + 100
            pPoint = Point(px,py)
            pCard = Image(pPoint,"img/"+suit+str(rank)+".gif")
            pCard.draw(window)

        #deal cards to dealer
        dealerCard1 = self.deck.dealCard()
        self.dHand.append(dealerCard1)
        dealerCard2 = self.deck.dealCard()
        self.dHand.append(dealerCard2)
        dx = dPoint.getX()
        dy = dPoint.getY()
        for card in self.dHand:
            suit = card.getSuit()
            rank = card.getRank()
            dx = dx + 100
            dPoint = Point(dx,dy)
            dCard = Image(dPoint,"img/"+suit+str(rank)+".gif")
            dCard.draw(window)

        #hide first card of dealer
        self.hideCard.draw(window)
        self.hideCard.move(dx-100,dy)
                
    def hit(self,window,point):
        """Add a new card to player's hand and place it at a point"""
        newCard = self.deck.dealCard() #deal new card
        suit = newCard.getSuit()
        rank = newCard.getRank()
        newImg = Image(point,"img/"+suit+str(rank)+".gif") #draw new card
        newImg.draw(window)
        self.pHand.append(newCard) #add new card into the list of hand

    def evalHand(self, hand):
        """Calculate total value of cards in hands
            Evaluate the value of Ace card"""
        hasAce = False #flag for whether an Ace is in hand or not
        value = 0

        for card in hand:
            if card.getValue() == 1: #record that an Ace was dealt
                hasAce = True
            value = value + card.getValue() #count Ace as 1, add 1 to total

        #if counting Ace as 11 still allows total value to stay under 21
        if hasAce and value + 10 <= 21: 
            value = value + 10 #then count Ace as 11, add 10 more to total

        return value

    def dealerPlays(self,window,dPoint):
        """Deal new cards to dealer until hit 'soft 17'"""
            
        value = self.evalHand(self.dHand) #calculate card value of dealer's hand
        dx = dPoint.getX()
        dy = dPoint.getY()
        while value <= 17: #while total value is smaller than 17
            newCard = self.deck.dealCard() #keep dealing new card
            self.dHand.append(newCard)
            value = self.evalHand(self.dHand)
            suit = newCard.getSuit()
            rank = newCard.getRank()
            newImg = Image(dPoint, "img/"+suit+str(rank)+".gif")
            newImg.draw(window)
            dx = dx + 100  #increment x value so cards don't overlap each other
            dPoint = Point(dx,dy)

        return value

def main(): 
    win = GraphWin("Test BJ", 800,600)
    win.setBackground("dark green")

    game = Blackjack()
    game.initDeal(win, Point(200,200), Point(200,400))
    game.hit(win,Point(500,400))

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()


            
                
                
            
                    

            
                
                

                
                
            
