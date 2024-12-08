import random

import pygame as pg

import game_config


def load_img(name):
    img = pg.image.load(name)
    # img = img.convert()
    # colorkey = img.get_at((0, 0))
    # img.set_colorkey(colorkey)
    img = pg.transform.scale(img, (100, 100))
    return img


class Kaktuss(pg.sprite.Sprite):
    def __init__(self, screen):
        pg.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = load_img('Pictures/')
        self.rect = self.image.get_rect()
        self.rect.y = game_config.WINDOW_SIZE[1] - 100
        self.rect.x = game_config.WINDOW_SIZE[0]
        self.speed = random.randint(3, 5)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x > self.screen.get_wight():
            self.rect.x = random.randint(0, self.screen.get_wight() - self.rect.width)
            self.rect.bottom = 0
            self.speed = random.randint(3, 5)

    def draw(self):
        self.screen.blit(self.image, self.rect)
