# Michelle Le, Samuel Crockford
# Programming Assignment 5
# Due Date: April 19, 2022
# This program allows users to play BlackJack with betting feature


from cash import *
from graphics import *
from button import Button
from blackjack import Blackjack
from deck import Deck
from playingcard import Card


def introWin():  #window for game intro
    #background
    win = GraphWin("Welcome to Black Jack Game", 972, 473)
    background = Image(Point(486,236),"img/Blackjack-Game.gif")
    background.draw(win)

    #button for Start, Quit, Rules 
    startButton = Button(win, Point(320,380), 100, 50, "Start")
    quitButton = Button(win, Point(470,380), 100, 50, "Quit")
    ruleButton = Button(win, Point(620,380), 100, 50, "Rules")

    return win, startButton, quitButton, ruleButton

def rulesWin():  #window to display rules
    #background
    win = GraphWin("Black Jack Rules", 612,408)
    background = Image(Point(306,204),"img/rules-background.gif")
    background.draw(win)

    #title
    title = Text(Point(306,50),"RULES")
    title.setSize(20)
    title.setTextColor("lemon chiffon")
    title.setFace("arial")
    title.setStyle("bold")
    title.draw(win)

    #rules
    line1 = Text(Point(306, 100), "All number cards has face value")
    line1.setTextColor("white")
    line1.setFace("arial")
    line1.setStyle("bold")
    line1.draw(win)
    
    line2 = Text(Point(306, 130), "Jack, King and Queen has a value of 10")
    line2.setTextColor("white")
    line2.setFace("arial")
    line2.setStyle("bold")
    line2.draw(win)

    line3 = Text(Point(306, 180), "Ace is counted as 1 or 11 \nsuitable to player's chances of winning ")
    line3.setTextColor("white")
    line3.setFace('arial')
    line3.setStyle("bold")
    line3.draw(win)
    
    line4 = Text(Point(306, 240), "Try to get 21 or as close to 21 as possible.\nIf the sum exceeds 21, player busts and loses instantly")
    line4.setTextColor("white")
    line4.setFace("arial")
    line4.setStyle("bold")
    line4.draw(win)
    
    line5 = Text(Point(306, 280), "Click 'Hit': Deal one more card to player's hand")
    line5.setTextColor("white")
    line5.setFace("arial")
    line5.setStyle("bold")
    line5.draw(win)
    
    line6 = Text(Point(306, 320), "Click 'Stand': Stop dealing card to player. \nDealer got dealt new cards until hit 'soft 17'")
    line6.setTextColor("white")
    line6.setFace("arial")
    line6.setStyle("bold")
    line6.draw(win)

def gameWin(cash):  #window to set up blackjack game
    #background
    win = GraphWin("Black Jack", 1000, 600)
    background = Image(Point(500,300), "img/game-background.gif")
    background.draw(win)

    #buttons
    deal = Button(win,Point(500,530),70,30, "Deal") #deal button
    deal.deactivate()
    dealImg = Image(Point(500,470),"img/deal.gif")
    dealImg.draw(win)
    
    stand = Button(win,Point(850,150),70,30,"Stand") #stand button 
    stand.deactivate()

    hit = Button(win,Point(850,200),70,30,"Hit") #hit button
    hit.deactivate()
    
    restart = Button(win,Point(850, 250),70,30, "Restart") #restart button

    quitButton = Button(win,Point(850,300),70,30,"Quit") #quit button 

    betButtonImg = Image(Point(100,530),"img/bet button.gif")
    betButtonImg.draw(win)
    betButton = Button(win,Point(100,530),70,30, "Bet") #bet button

    #role holder 
    dtext = Text(Point(300,100),"Dealer: ")
    dtext.setStyle("bold")
    dtext.setSize(18)
    dtext.setTextColor("white")
    dtext.draw(win)
    
    ptext = Text(Point(300,300),"Player: ")
    ptext.setStyle("bold")
    ptext.setSize(18)
    ptext.setTextColor("white")
    ptext.draw(win)

    #score holder
    dScore = Text(Point(300,150), "")
    dScore.setStyle("bold")
    dScore.setSize(25)
    dScore.setTextColor("white")
    dScore.draw(win)

    pScore = Text(Point(300,350), "")
    pScore.setStyle("bold")
    pScore.setSize(25)
    pScore.setTextColor("white")
    pScore.draw(win)

    #result holder
    result = Text(Point(500,230),"")
    result.setStyle("bold")
    result.setSize(21)
    result.setTextColor("lemon chiffon")
    result.draw(win)

    #chip
    whitechipImg = Image(Point(100,150),"img/white chip.gif")
    whitechipImg.draw(win)
    whitechip = Button(win,Point(100,150),30,20,"50")
    
    redchipImg = Image(Point(100,220),"img/red chip.gif")
    redchipImg.draw(win)
    redchip = Button(win,Point(100,220),30,20,"100")
    
    bluechipImg = Image(Point(100,290),"img/blue chip.gif")
    bluechipImg.draw(win)
    bluechip = Button(win,Point(100,290),30,20,"200")
    
    blackchipImg = Image(Point(100,360),"img/black chip.gif")
    blackchipImg.draw(win)
    blackchip = Button(win,Point(100,360),30,20,"500")

    #initiate cash and bet amount
    cashgame = Cash(cash)
    cash = cashgame.getCash()
    bet = 0
    
    showCash = Text(Point(100,50),"Cash: $" + str(cash))
    showCash.setFill("lemon chiffon")
    showCash.setSize(22)
    showCash.draw(win)
    
    showBet = Text(Point(100,80),"Bet: $" + str(bet))
    showBet.setFill("lemon chiffon")
    showBet.setSize(22)
    showBet.draw(win)

    #check if player has money before the game starts
    betList = []
    chipVal = [50,100,200,500]
    chipName = [whitechip,redchip,bluechip,blackchip]

    if cash <= 0:  #if player runs out of cash
        result.setText("No more cash to bet! Quit and start new game!")
        betButton.deactivate()
        restart.deactivate()
        pt = win.getMouse()
        while not quitButton.isClicked(pt):
            pt = win.getMouse()
        win.close()

    else: #if not, let user place bet
        result.setText("Choose chips to place your bet")
        pt = win.getMouse()
        while not betButton.isClicked(pt):
            for i in range(4):
                if chipName[i].isClicked(pt): #if player click on chips
                    betamt = chipVal[i] #set bet amount according to chips chosen
                    #check if bet amount exceeds cash amount
                    if bet + betamt <= cash:
                        bet = bet + betamt
                        newtext = cashgame.placebet(betamt)
                        showCash.setText("Cash: $" + str(newtext))
                        showBet.setText("Bet: $" + str(bet))
                        betList.append(bet) 
                    else:
                        result.setText("Not enough cash to bet more!")
                           
                else: #if player doesn't click on chip 
                    betamt = 0 #set bet amount to 0
                    bet = bet + betamt
                    showBet.setText("Bet: $" + str(bet))
                    betList.append(bet)
                totalbet = betList[-1]
            pt = win.getMouse()
        result.setText("")  
        betButton.deactivate()
        deal.activate()
        
        #deal first round
        pt = win.getMouse() 
        while not deal.isClicked(pt): #notify player to click deal again 
            result.setText("You didn't click Deal to start game")
            pt = win.getMouse()

        #once deal button is clicked, start game
        result.setText("")
        game = Blackjack()
        game.initDeal(win, Point(300,150), Point(300,350))
        deal.deactivate()
        hit.activate()
        stand.activate()

        #scores
        playertotal = game.evalHand(game.pHand)
        dealertotal = game.evalHand(game.dHand)
        
        pScore.setText(str(playertotal)) #only show player's score

        #if player score is 21 after first deal
        if playertotal == 21 and dealertotal != 21:
            game.hideCard.undraw()
            dScore.setText(str(dealertotal))
            result.setText("BLACK JACK! YOU WIN!")
            newtext = cashgame.playerwins(totalbet)
            showCash.setText("Cash: $" + str(newtext))
            hit.deactivate()
            stand.deactivate()

        if playertotal == 21 and dealertotal == 21:
            game.hideCard.undraw()
            dScore.setText(str(dealertotal))
            newtext = cashgame.push(totalbet)
            showCash.setText("Cash: $" + str(newtext))
            result.setText("PUSH!")
            hit.deactivate()
            stand.deactivate()

        #if not, allow user to choose hit or stand
        pt = win.getMouse()
        px = 600
        dx = 600
        while not quitButton.isClicked(pt):
            #if hit button is clicked
            if hit.isClicked(pt): 
                game.hit(win,Point(px,350)) #deal new card to player
                playertotal = game.evalHand(game.pHand) #calculate score 
                pScore.setText(str(playertotal))
                px = px + 100 #increment x value so cards don't overlap each other

                #check player's card value
                if playertotal == 21:
                    game.hideCard.undraw()
                    dealertotal = game.evalHand(game.dHand)
                    dScore.setText(str(dealertotal))
                    if playertotal == dealertotal:
                        newtext = cashgame.push(totalbet)
                        showCash.setText("Cash: $" + str(newtext))
                        result.setText("PUSH!") 
                        hit.deactivate()
                        stand.deactivate()
                    else:
                        newtext = cashgame.playerwins(totalbet)
                        showCash.setText("Cash: $" + str(newtext))
                        result.setText("YOU WIN!")
                        hit.deactivate()
                        stand.deactivate()

                elif playertotal > 21: #check if player busts
                    game.hideCard.undraw()
                    dealertotal = game.evalHand(game.dHand)
                    dScore.setText(str(dealertotal))
                    result.setText("BUSTED! You Lose!")
                    hit.deactivate()
                    stand.deactivate()
                    
            #if stand button is clicked
            elif stand.isClicked(pt): 
                #reveal dealer's hidden card
                game.hideCard.undraw()

                #check if dealer has a blackjack
                if dealertotal == 21:
                    dScore.setText(str(dealertotal)) #show dealer's score
                    result.setText("Dealer has BlackJack! DEALER WINS!")

                #if not, deal new cards to dealer until hit soft 17
                else:
                    game.dealerPlays(win, Point(dx,150))
                    dealertotal = game.evalHand(game.dHand)
                    dScore.setText(str(dealertotal))
                    dx = dx + 100
                    
                    hit.deactivate()
                    stand.deactivate()

                    #check dealer's card value
                    if dealertotal == 21: 
                        result.setText("DEALER WINS!")

                    elif dealertotal > 21:
                        result.setText("DEALER BUSTED! YOU WIN!")
                        newtext = cashgame.playerwins(totalbet)
                        showCash.setText("Cash: $" + str(newtext))

                    else: #if dealer total is smaller than or equal to 21
                        if dealertotal > playertotal:
                            result.setText("DEALER WINS!")
                            showCash.setText("Cash: $" + str(newtext))
                        elif dealertotal < playertotal:
                            result.setText("YOU WIN!")
                            newtext = cashgame.playerwins(totalbet)
                            showCash.setText("Cash: $" + str(newtext))
                        else:
                            newtext = cashgame.push(totalbet)
                            showCash.setText("Cash: $" + str(newtext))
                            result.setText("PUSH!")

            #if restart button is clicked
            if restart.isClicked(pt):
                #clear player's and dealer's current cards
                game.dHand.clear()
                game.pHand.clear()
                cash = cashgame.cash  #set current cash amount as initial cash in new game
                win.close() 
                gameWin(cash) #run game again with current cash amount
                break #break out of while loop after gameWin is closed
            pt = win.getMouse()
        win.close()    

def main():
    #create intro window
    win1, startButton, quitButton, ruleButton = introWin()

    #get user click
    pt = win1.getMouse()
    
    #while user doesn't click the quit button
    while not quitButton.isClicked(pt): 
        if startButton.isClicked(pt): #if start button is clicked, play game
            win1.close()
            gameWin(4000)
            break #break out of the while loop after introWin is closed
        elif ruleButton.isClicked(pt): #if rule button is clicked, show rules
            rulesWin()
        pt = win1.getMouse()
        
    win1.close() #when quit button is clicked, exit game
main()

