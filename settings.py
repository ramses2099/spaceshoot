import pygame
from pygame.math import Vector2 as vec
import os

WIDTH = 600
HEIGHT = 400
TITLE = "Space Shoot"
TITLESIZE = 16
FONT = "assets/fonts/kenvector_future.ttf"
FPS = 60
OFFSET = 5

COLORS = {
    'black':(0, 0, 0),
    'white':(255, 255, 255),
    'red':(255, 0, 0),
    'green':(0, 255, 0),
    'blue':(0, 0, 255),
}

INPUTS = {
    'escape':False,
    'space': False,
    'up': False,
    'down': False,
    'left': False,
    'right': False,
    'left_click': False,
    'right_click': False,
    'scroll_up': False,
    'scroll_down': False,
}

# BG
BG = pygame.transform.scale(pygame.image.load(os.path.join("./assets/images/Backgrounds/","darkPurple.png")),(WIDTH,HEIGHT))
# Player
PLAYER = pygame.transform.scale(pygame.image.load(os.path.join("./assets/images/Player/","playerShip1_red.png")),(32, 32))

LASER = {
    "laserBlue01":pygame.image.load(os.path.join("./assets/images/Lasers/","laserBlue01.png")),
    "laserBlue02":pygame.image.load(os.path.join("./assets/images/Lasers/","laserBlue02.png")),
    "laserBlue03":pygame.image.load(os.path.join("./assets/images/Lasers/","laserBlue03.png")),
    "laserBlue04":pygame.image.load(os.path.join("./assets/images/Lasers/","laserBlue04.png")),
    "laserBlue08":pygame.image.load(os.path.join("./assets/images/Lasers/","laserBlue08.png")),
    "laserBlue09":pygame.image.load(os.path.join("./assets/images/Lasers/","laserBlue09.png")),
    "laserBlue10":pygame.image.load(os.path.join("./assets/images/Lasers/","laserBlue10.png")),
    "laserBlue11":pygame.image.load(os.path.join("./assets/images/Lasers/","laserBlue11.png")),
}

ENEMIES = {
    "enemyBlack1":pygame.image.load(os.path.join("./assets/images/Enemies/","enemyBlack1.png")),
    "enemyBlue2":pygame.image.load(os.path.join("./assets/images/Enemies/","enemyBlue2.png")),
    "enemyGreen4":pygame.image.load(os.path.join("./assets/images/Enemies/","enemyGreen4.png")),
    "enemyRed5":pygame.image.load(os.path.join("./assets/images/Enemies/","enemyRed5.png")),
}

METEORS = {
    "meteorBrown_big4":pygame.image.load(os.path.join("./assets/images/Meteors/","meteorBrown_big4.png")),
    "meteorBrown_big2":pygame.image.load(os.path.join("./assets/images/Meteors/","meteorBrown_big2.png")),
    "meteorBrown_tiny2":pygame.image.load(os.path.join("./assets/images/Meteors/","meteorBrown_tiny2.png")),
    "meteorGrey_big3":pygame.image.load(os.path.join("./assets/images/Meteors/","meteorGrey_big3.png")),
    "meteorGrey_small2":pygame.image.load(os.path.join("./assets/images/Meteors/","meteorGrey_small2.png")),
    "meteorGrey_tiny2":pygame.image.load(os.path.join("./assets/images/Meteors/","meteorGrey_tiny2.png")),
}


POWERUPS = {
    "bolt_gold":pygame.image.load(os.path.join("./assets/images/Power-ups/","bolt_gold.png")),
    "pill_blue":pygame.image.load(os.path.join("./assets/images/Power-ups/","pill_blue.png")),
    "shield_bronze":pygame.image.load(os.path.join("./assets/images/Power-ups/","shield_bronze.png")),
}