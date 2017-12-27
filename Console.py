#!/usr/bin/python

import time

class Console:
    
    # I/O
    
    min = Gameboard.getMinValue()
    max = getMaxValue()
    
    def __int__(self):
        """ Initialize a console object """
    
    def displayMessage(self, string):
        """ Outputs message """
        print("%s", string)
        
    def getCoordinate(self, string):
        """ Get coordinate from user or computer and validate it"""
        
        running = True;
        
        # validate coordinate
        while(running):
            coordinate = input("%s", string)
            
            try:
                coordinate = int()
            except ValueError:
                print("That input is invalid.\nPlease enter a number between %s and %s:", min, max)
                continue
                
            if coordinate < min or coordinate > max:
                print("That input is invalid.\nPlease enter a number between %s and %s:", min, max)
                continue
            else:
                running = False
        
        return coordinate
        
    def displayBoard(self):
        """ Adds 'frame' to 2darray and displays it """
        # TODO
        
    def pause(self, int):
        """ Pauses game """
        time.sleep(int)
        
    def showFleetStatus(self, board):
        """ Displays the number of ships still in play """
        
        myCounter = Counter()
        
        for ship in board.getMyShips():
            if ship.getActive() is True:
                myCounter.addToCounter()
                
        if(myCounter.getCounter() >= 2):
            Console.displayMessage("\n\nYou have %s ships left in your fleet.", myCounter.getCounter())
        else:
            Console.displayMessage("\n\nYou have %s ship left in your fleet.", myCounter.getCounter())
            
    
