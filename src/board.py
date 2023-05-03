import pygame
from universal import Coord2D, SPRITES

# this module handles management of the game board

class Board:
    def __init__(self, startPos : Coord2D, surface, sideLength=8):
        self.startPos = startPos
        self.sideLength = sideLength
        self.surface = surface