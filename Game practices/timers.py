import pygame as pg
import sys

# We initiate the program
pg.init()

# This the screen
screen = pg.display.set_mode((400, 400))
# this is the  clock
clock = pg.time.Clock()

# Current Time
current_time = 0

# Time when you hit the keyword
button_pressed = 0

# Game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            button_pressed = pg.time.get_ticks()
            screen.fill((255, 0, 0))

    current_time = pg.time.get_ticks()

    if current_time - button_pressed > 2000:
        screen.fill((0, 0, 0))

    pg.display.flip()
    clock.tick(60)
