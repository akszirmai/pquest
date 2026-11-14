import pygame

from pygame.sprite import Sprite
from src.location import Location

class Player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)

        filename = "./resource/Player_char_1.png"
        try:
            self.image = pygame.image.load(filename).convert_alpha()
        except FileNotFoundError:
            print(f"Player image file: {filename} cannot be found")
            return 1
        self.position = pygame.Vector2(x, y)
        self.x = self.position.x
        self.y = self.position.y

        self.calc_scr_coords()

    def calc_scr_coords(self):
        self.scx = self.position.x          # Later to use the proper projection
        self.scy = self.position.y
        self.rect = self.image.get_rect(center=(self.scx, self.scy))

#    def set_location(self, x, y):
#        self.x = x
#        self.y = y
#        self.calc_scr_coords()

    def update(self, dt: float) -> None:
        vert_mul = 0.25
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move(pygame.Vector2(-dt, 0))
        if keys[pygame.K_d]:
            self.move(pygame.Vector2(dt, 0))
        if keys[pygame.K_w]:
            self.move(pygame.Vector2(0, -dt*vert_mul))
        if keys[pygame.K_s]:
            self.move(pygame.Vector2(0, dt*vert_mul))

    def move(self, dirvect: pygame.Vector2) -> None:
        self.position += dirvect * 100
        self.calc_scr_coords()


    def draw(self):
        print("WTF")
