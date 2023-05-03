import pygame
from universal import Coord2D, SPRITES

# this module handles management of the game board

class Board:
    def __init__(self, startPos : Coord2D):
        self.startPos = startPos
        self.sideLength = 8
        self.squareLength = 64
        self.surface = SPRITES["board"]