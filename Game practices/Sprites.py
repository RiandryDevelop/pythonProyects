import pygame, sys, random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("Sprites ( Resources)/Game Sounds/DISPARO.wav")

    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, crosshair_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]



# General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("Sprites ( Resources)/PNG/Stall/bg_green.png")
pygame.mouse.set_visible(False)

# Crosshair
crosshair = Crosshair("Sprites ( Resources)/PNG/Objects/rifle_red.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# Target
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target("Sprites ( Resources)/PNG/Objects/duck_outline_target_white.png", random.randrange(0, screen_width-20), random.randrange(0, screen_height-20))
    target_group.add(new_target)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    pygame.display.flip()
    screen.blit(background, (0, 0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair.update()
    clock.tick(60)