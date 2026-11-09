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
        self.x = x
        self.y = y
        self.calc_scr_coords()

    def calc_scr_coords(self):
        self.scx = self.x          # Later to use the proper projection
        self.scy = self.y
        self.rect = self.image.get_rect(center=(self.scx, self.y))

    def set_location(self, x, y):
        self.x = x
        self.y = y
        self.calc_scr_coords()
