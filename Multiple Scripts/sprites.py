import pygame
from settings import *

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
