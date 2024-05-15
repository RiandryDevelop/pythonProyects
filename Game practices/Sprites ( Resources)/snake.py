import pygame
from pygame.locals import *

def draw_player():
    screen.fill((255, 255, 255))
    screen.blit(player, (player_x, player_y))


    def update(self):
        self.rect.center = pygame.mouse.get_pos()

# we're going to recreate the classic game (SNAKE)
if __name__ == "__snake__":
    pygame.init()

    #Screen
    screen_width = 400
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("SNAKE")
    screen.fill((255, 255, 255))


    # Snake (player)
    player = pygame.image.load("python_projects-main/1_snake_game/resources/block.jpg").convert()
    player_x = 100
    player_y = 100
    screen.blit(player, (player_x, player_y))

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            elif event.type == QUIT:
                running = False