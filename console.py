#!/usr/bin/python

import time
from gameboard import *
from counter import *

class Console:
    
    # I/O
    
    min = gameboard.getMinValue()
    max = gameboard.getMaxValue()
    
    def __int__(self):
        """ Initialize a console object """
        
    def displayMessage(self, string):
        """ Outputs message """
        """ string -> void """
        print("{}".format(string))
        
    def getCoordinate(self, string):
        """ Get coordinate from user or computer and validate it """
        """ string -> integer """
        
        running = True;
        
        # validate coordinate
        while(running):
            coordinate = input()
            
            try:
                coordinate = int()
            except ValueError:
                print("That input is invalid.\nPlease enter a number between {} and {}:".format(min, max))
                continue
                
            if coordinate < min or coordinate > max:
                print("That input is invalid.\nPlease enter a number between {} and {}:".format(min, max))
                continue
            else:
                running = False
        
        return coordinate
        
    def displayBoard(self):
        """ Adds 'frame' around gameboard and displays it """
        pass
        # TODO
        
    def pause(self, int):
        """ Pauses game """
        """ int -> void """
        time.sleep(int)        

    def playAgain(self):
        """ Checks if player wants to play again """
        pass
        # TODO
        
    def showFleetStatus(self, board):
        """ Displays the number of ships still in play """
        
        myCounter = Counter()
        
        for ship in board.getMyShips():
            if ship.getActive() is True:
                myCounter.addToCounter()
                
        if(Counter.getCounter(myCounter) >= 2):
            Console.displayMessage("\n\nYou have {} ships left in your fleet.".format(myCounter.getCounter())
        else:
            Console.displayMessage("\n\nYou have {} ship left in your fleet.".format(myCounter.getCounter())
