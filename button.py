# a class that creates a Button object which will be clickable

from graphics import *

class Button:
    def __init__(self, win, center, width, height, label):
        """ Create a rectangular button, where: 
            win is the GraphWin where the button will be drawn
            center will be a Point object where the button is centered
            width is an integer that is the width of the button in pixels
            height is an intefer that is the height of the button in pixels
            label is a string that appear in the button"""

        x,y = center.getX(), center.getY()
        self.xmin = x - width/2
        self.xmax = x + width/2
        self.ymin = y - height/2
        self.ymax = y + height/2
        pt1 = Point(self.xmin,self.ymin)
        pt2 = Point(self.xmax,self.ymax)
        self.rect = Rectangle(pt1,pt2)
        self.rect.setFill('linen')
        self.rect.draw(win)
        self.words = Text(center,label)
        self.words.draw(win)
        self.activate()

    def deactivate(self):
        """sets this button to deactivated, so it is not click-able"""
        # color text gray
        self.words.setFill("darkgrey")
        # set the outline to be thinner
        self.rect.setWidth('1')
        # set the boolen flag self.active to False
        self.active = False

    def activate(self):
        """sets this button to activated, which means it can be clicked"""
        # set the color of the label to black
        self.words.setFill("black")
        # set the the outline to look bolder
        self.rect.setWidth(2)
        # set the boolean flag self.active to True
        self.active = True 

    def isClicked(self,pt):
        """returns True if pt is within the boudaries of the button, False otherwise"""
        if self.active and \
            self.xmin <= pt.getX() <= self.xmax and \
            self.ymin <= pt.getY() <= self.ymax: 
                return True
        else:
            return False

def main():
    gwin = GraphWin("Button Test",200,200)
    myButton = Button(gwin,Point(100,100),50,25,"Quit")
    p= gwin.getMouse()
    if myButton.isClick(p):
        print("Button was clicked")
    else:
        print("Button was not clicked")

if __name__== "__main":
    main()
    
