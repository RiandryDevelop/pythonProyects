import pygame , sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_X, pos_Y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load("PNG/street-straight.png"))
        self.sprites.append(pygame.image.load("PNG/street-straight.png"))
        self.sprites.append(pygame.image.load("PNG/street-straight.png"))
        self.sprites.append(pygame.image.load("PNG/street-straight.png"))
        self.sprites.append(pygame.image.load("PNG/street-straight.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_X, pos_Y]

    def update(self):
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
          self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]

# Game Setup
pygame.init()
clock = pygame.time.Clock()

# Screen
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animation street")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(10, 10)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # drawing
    screen.fill((0, 0, 225))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)