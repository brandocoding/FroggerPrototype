import pygame
import os 
from os import path
from settings import *
from sprites import *

class Game():
    def __init__(self):
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.img_dir = path.join(path.dirname(__file__), 'img')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def load(self):
        for i in range(3):
            INSTANCE_COUNT = i + 1
            self.cars_1 = CarsRows(pos_carspeed, SPACING, 576, BOX_WIDTH)
            self.all_sprites.add(self.cars_1)
            self.cars.add(self.cars_1)

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.cars = pygame.sprite.Group()
        self.background = pygame.image.load(path.join(self.img_dir, "background.png")).convert()
        self.background_rect = self.background.get_rect()
        self.load()
        print(self.all_sprites)
        print(self.cars)
        self.run()
        

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()  

    def update(self):
        self.all_sprites.update()
        self.cars.update()

    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.background, self.background_rect)
        self.all_sprites.draw(self.screen)
        pygame.display.update()

    def show_start_screen(self):
        pass

g = Game()
while g.running:
    g.new()

pygame.quit()
quit()
