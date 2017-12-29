#!/usr/bin/python

class Counter:
    
    def __init__(self):
        """ Initialize a counter object """
        self.__counter = 0
        
    def setCounter(self, int):
        __counter = int
        
    @property
    def getCounter(self):
        return self.__counter
        
    def addToCounter(self):
        self.__counter += 1
        
