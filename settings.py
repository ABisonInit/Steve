import os
import pygame

# defining variables with Bison Dos
white = (255, 255, 255)
black = (0, 0, 0)
navyblue = (0, 2, 35)
lightgrey = (169, 169, 169)

# game settings
width = 1024
height = 768
fps = 60
title = "Steve"
BgColour = navyblue

tilesize = 32
gridwidth = width / tilesize
gridheight = height / tilesize

# assets folder
gameFolder = os.path.dirname(__file__)
senseiFolder = os.path.join(gameFolder, "img/generic-rpg-pack_v0.3_(alpha-release)_vacaroxa/rpg-pack/chars/sensei")

# loadingScreen
x_steve = 5
y_steve = 5

# Steve
steveSpeed = 1
