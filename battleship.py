#!usr/bin/python

from console import *
from gameboard import *

class Battleship:
    
    # make a console object
    myConsole = Console()
    
    # create gameboards for user and computer
    userBoard = Gameboard()
    computerBoard = Gameboard()
    

    def beginGame(self):
        while myConsole.playAgain is True:
           setUpGame()
           playGame()
           
    def setUpGame(self):
        """ Sets up boards so the game can begin """
        # TODO
        
    def playGame(self):
        """ Runs game play """
        # TODO
    
def __main__(self):
    myBattleship = Battleship()
    myBattleship.beginGame()
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
