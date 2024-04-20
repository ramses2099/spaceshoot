import pygame
from pygame.math import Vector2 as vec
import os

WIDTH = 600
HEIGHT = 400
TITLE = "Space Shoot"
TITLESIZE = 16
FONT = "assets/fonts/homespun.ttf"
FPS = 60

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
BG = pygame.image.load(os.path.join("./assets/images/Backgrounds/","darkPurple.png"))