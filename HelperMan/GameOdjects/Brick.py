
# Класс ящик
import pygame as pg
import random

import game_config


def load_img(name):
    img = pg.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    img = pg.transform.scale(img, (100, 100))
    return img


class Brick(pg.sprite.Sprite):
    def __init__(self, screen):
        pg.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = load_img(random.choice(["Pictures/kaktus_pixel_art1.png", "Pictures/kaktus_pixel_art.png2.png"]))
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() + self.rect.width + random.randint(0, screen.get_width())
        self.rect.bottom = screen.get_height() - game_config.BOTTOM_DINO
        self.speed = 5

    def update(self):
        self.rect.x -= self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)
