import pygame

# this file contains all types, data, and helper functions used across the game

###############
# Data
###############

SPRITES = dict()

def prepareSprite(spriteFile : str) -> pygame.Surface:
    sprite = pygame.image.load(spriteFile).convert_alpha()
    sprite = doubleSpriteSize(sprite)
    return sprite

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

def initializeSpriteDict():
    SPRITES["board"] = prepareSprite("../Assets/chessBoards/chessBoard.png")


###############
# Types
###############

Coord2D = tuple[int, int]

###############
# helpers
###############