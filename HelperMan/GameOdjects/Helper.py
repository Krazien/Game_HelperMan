# Класс объекта игрока
import pygame as pg
import HelperMan.game_config as game_config


def load_img(name):
    img = pg.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    img = pg.transform.scale(img, (50, 100))
    return img


class Helpers(pg.sprite.Sprite):
    def __init__(self, screen):
        pg.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = load_img("HelperMan/Pictures/Helper-pixel_art1.png")
        self.rect = self.image.get_rect()
        self.dino_bottom = screen.get_height() - game_config.BOTTOM_DINO
        self.rect.bottom = self.dino_bottom
        self.rect.centerx = 200
        self.speedx = 0
        # для прыжка
        self.is_jumping = False
        self.jump_height = self.dino_bottom - 150
        self.speedy = 10

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.speedx = -8
        elif keys[pg.K_RIGHT]:
            self.speedx = 8
        else:
            self.speedx = 0

        self.rect.x += self.speedx
        if self.rect.right > game_config.WINDOW_SIZE[0]:
            self.rect.right = game_config.WINDOW_SIZE[0]
        if self.rect.left < 0:
            self.rect.left = 0

        # для прыжка
        if not self.is_jumping and self.rect.bottom == self.dino_bottom:
            if keys[pg.K_SPACE]:
                self.is_jumping = True

        self.jump()

    def jump(self):
        if self.is_jumping and self.rect.bottom > self.jump_height:
            self.rect.bottom -= self.speedy
            # Если достигли высоты прыжка
            if self.rect.bottom <= self.jump_height:
                self.is_jumping = False
        else:
            if self.rect.bottom < self.dino_bottom:
                self.rect.bottom += self.speedy
            else:
                self.rect.bottom = self.dino_bottom

    def draw(self):
        self.screen.blit(self.image, self.rect)
