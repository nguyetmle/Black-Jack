#a class that creates Cash feature in BlackJack

class Cash:
    """Attributes of Cash class are as follows.
        INSTANCE VARIABLES
        cash: amount of cash that player has"""
    
    def __init__(self,totalcash):
        self.cash = totalcash

    def getCash(self):
        return self.cash 

    def placebet(self,betamt):
        """Deduct cash when place bets"""
        if betamt <= self.cash:
            self.cash = self.cash - betamt
        return(self.cash)
    
    def playerwins(self,betamt):
        """Add cash when player wins"""
        self.cash = self.cash + (2*betamt)
        return self.cash
    
    def push(self,betamt):
        """Put player's bets back if it's a tie game"""
        self.cash = self.cash + betamt
        return self.cash
    
        
        
        
        
        
    
        
    
