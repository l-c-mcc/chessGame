import pygame

# this file contains all types, data, and helper functions used across the game

###############
# Data
###############

# holds all sprite sources in the game. is not meant to be modified after initialization.
SPRITES = dict()

# takes a file location as an argument and turns it into a surface.
def prepareSprite(spriteFile : str, doubleSize : bool = True) -> pygame.Surface:
    sprite = pygame.image.load(spriteFile).convert_alpha()
    if(doubleSize):
        sprite = doubleSpriteSize(sprite)
    return sprite

# returns a sprite double the size (length and width) as the input.
def doubleSpriteSize(sprite : pygame.Surface) -> pygame.Surface:
    spriteWidth = sprite.get_width()
    originalSprite = pygame.image.tobytes(sprite, "RGBA")
    currentRow = bytearray()
    newSprite = bytearray()
    col = 0
    for i in range(0,len(originalSprite),4):
        if col == spriteWidth:
            col = 0
            newSprite += currentRow + currentRow
            currentRow = bytearray()
        col += 1
        for j in range(0,2):
            for k in range(0,4):
                currentRow.append(originalSprite[i+k])
    newSprite += currentRow + currentRow
    return pygame.image.frombytes(bytes(newSprite),(spriteWidth*2,spriteWidth*2),"RGBA")

# initializes sprite dictionary
def initializeSpriteDict():
    SPRITES["board"] = prepareSprite("../Assets/chessBoards/chessBoard.png")
    SPRITES["bishopWhite"] = prepareSprite("../Assets/chessPieces/bishopWhite.png")
    SPRITES["knightWhite"] = prepareSprite("../Assets/chessPieces/knightWhite.png")
    SPRITES["kingWhite"] = prepareSprite("../Assets/chessPieces/kingWhite.png")
    SPRITES["pawnWhite"] = prepareSprite("../Assets/chessPieces/pawnWhite.png")
    SPRITES["queenWhite"] = prepareSprite("../Assets/chessPieces/queenWhite.png")
    SPRITES["rookWhite"] = prepareSprite("../Assets/chessPieces/rookWhite.png")
    SPRITES["bishopBlack"] = prepareSprite("../Assets/chessPieces/bishopBlack.png")
    SPRITES["knightBlack"] = prepareSprite("../Assets/chessPieces/knightBlack.png")
    SPRITES["kingBlack"] = prepareSprite("../Assets/chessPieces/kingBlack.png")
    SPRITES["pawnBlack"] = prepareSprite("../Assets/chessPieces/pawnBlack.png")
    SPRITES["queenBlack"] = prepareSprite("../Assets/chessPieces/queenBlack.png")
    SPRITES["rookBlack"] = prepareSprite("../Assets/chessPieces/rookBlack.png")


###############
# Types
###############

Coord2D = tuple[int, int]

###############
# Helpers
###############