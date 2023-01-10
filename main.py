#Vinthushan 
#December 20th 2022
#Purpose: a robeats copy but in pygame

import pygame
import random
import os
import sys
import time

# Window dimensions
window_y = 480
window_x = 720

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialise game window
pygame.display.set_caption('Robeats')
game_window = pygame.display.set_mode((window_y, window_x))
print("Y me")
# FPS (frames per second) controller
fps = pygame.time.Clock()

