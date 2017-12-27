#!usr/bin/python

from Console import Console
from Gameboard import Gameboard

class Battleship:
    
    # make a console object
    myConsole = Console()
    
    # create gameboards for user and computer
    userBoard = Gameboard()
    computerBoard = Gameboard()
    
    def __main__(self):
        myBattleship = Battleship()
        myBattleship.beginGame(self)
        
    def beginGame(self):
        while myConsole.playAgain is True:
           setUpGame()
           playGame()
           
    def setUpGame():
        # TODO
        
    def playGame():
        # TODO
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
