import pygame
from universal import Coord2D, SPRITES, Side

# this module handles management of the game board and game pieces

class Board:
    def __init__(self, position : Coord2D):
        self.position = position
        self.sideLength = 8
        self.squareLength = 64
        self.surface = SPRITES["board"]

class Piece:
    def __init__(self, position : Coord2D):
        self.position = position

class Knight(Piece):
    def __init__(self, position : Coord2D, side : Side):
        super(position)
        if side == Side.WHITE:
            self.surface = SPRITES["whiteKnight"]
        else:
            self.surface = SPRITES["blackKnight"]