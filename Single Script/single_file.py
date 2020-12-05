import pygame
import os
import random
from os import path

os.environ['SDL_VIDEO_CENTERED'] = '1'
img_dir = path.join(path.dirname(__file__), 'img')

WIDTH = 480
HEIGHT = 720
FPS = 60

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# car variables
pos_carspeed  = 2
SPACING = 60
BOX_WIDTH = 30
INSTANCE_COUNT = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class CarsRows(pygame.sprite.Sprite):
    def __init__(self, speed, spacing, bottom, width):
        self.originalspeed = speed
        self.originalbottom = bottom
        self.originalwidth = width
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = (INSTANCE_COUNT * (spacing + BOX_WIDTH))
        self.rect.bottom = bottom
        self.speedx = speed

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x < -30:
            self.rect.x = 480
        if self.rect.x > 480:
            self.rect.x = -30

# load all game graphics
background = pygame.image.load(path.join(img_dir, "background.png")).convert()
background_rect = background.get_rect()

all_sprites = pygame.sprite.Group()
cars = pygame.sprite.Group()

# Cars on Row 1
for i in range(3):
    INSTANCE_COUNT = i + 1
    cars_1 = CarsRows(pos_carspeed, SPACING, 576, BOX_WIDTH)
    all_sprites.add(cars_1)
    cars.add(cars_1)

running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update
    all_sprites.update()
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
quit()
