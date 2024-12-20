import pygame as pg

import game_config
import game_config as config
from game_dialog import GameDialog
from GameOdjects.Brick import Brick
from GameOdjects.Helper import Helpers
from GameOdjects.Kaktus import Kaktuss


def load_img(name):
    img = pg.image.load(name)
    # img = img.convert()
    # colorkey = img.get_at((0, 0))
    # img.set_colorkey(colorkey)
    img = pg.transform.scale(img, config.WINDOW_SIZE)
    return img


class HelperGame():
    """Базовый класс для запуска игры"""

    def __init__(self):
        # Фон игры
        self.background = load_img("HelperMan/Pictures/Песок.jpg")
        # Скорость обновления кадров
        self.__FPS = config.FPS
        self.__clock = pg.time.Clock()

        # Создаем объект класса GameDialog
        self.__game_dialog = GameDialog()

        # self.__player_name = self.__game_dialog.show_dialog_login()

        # Вызываем метод инициализациии остальных параметров
        self.__init_game()

    def __init_game(self):

        # Текущее значение очков игрока
        self.__current_player_score = 0

        # Создаем объект основного окна
        self.screen = pg.display.set_mode(game_config.WINDOW_SIZE)
        pg.display.set_caption("Бегущий человек")

        # Список всех спрайтов (графических объектов)
        self.all_sprites = pg.sprite.Group()

        # Отдельный список кирпичей
        self.bricks_spr_gr = pg.sprite.Group()

        # Объект игрока
        self.dino = Helpers(self.screen)
        self.all_sprites.add(self.dino)

        # Будет всего три кактуса
        count_kaktus = 3
        for i in range(count_kaktus):
            # Объект астероида
            kaktus = Kaktuss(self.screen)
            self.all_sprites.add(kaktus)

        # В начале игры будет всего 1 enemy
        self.count_enemy = 1
        for i in range(self.count_enemy):
            # Объект
            brick = Brick(self.screen)
            self.bricks_spr_gr.add(brick)
            self.all_sprites.add(brick)

    def __draw_scene(self):
        # отрисовка
        self.screen.blit(self.background, (0, 0))

        self.bricks_spr_gr.update()
        self.bricks_spr_gr.draw(self.screen)

        self.all_sprites.update()
        self.all_sprites.draw(self.screen)

        # self.__draw_score()
        self.check_collision()

        # Обновляем экран
        pg.display.update()
        pg.display.flip()
        self.__clock.tick(self.__FPS)

    def run_game(self, game_is_run):
        # Основной цикл игры
        while game_is_run:
            # Обрабатываем событие закрытия окна
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            # Отрисовываем всё
            self.__draw_scene()

    def check_collision(self):
        list_colid = pg.sprite.spritecollide(self.dino, self.bricks_spr_gr, False)
        if len(list_colid) > 0:
            if self.__game_dialog.show_dialog_game_over():
                self.__init_game()
            else:
                exit()
        for brick in self.bricks_spr_gr:
            if brick.rect.x < 0:
                self.__current_player_score += 1
                self.bricks_spr_gr.remove(brick)
                self.all_sprites.remove(brick)
                # Через каждые 3 побежденных противника, добавляем еще одного
                if self.__current_player_score % 3 == 0:
                    self.count_enemy += 1

        if len(self.bricks_spr_gr) < self.count_enemy:
            newBrick = Brick(self.screen)
            self.all_sprites.add(newBrick)
            self.bricks_spr_gr.add(newBrick)

    def __draw_score(self):
        font = pg.font.Font(None, 28)
        text_name = font.render(f"Игрок: {self.__player_name}", True, 'white')
        text_name_rect = text_name.get_rect(topleft=(10, 30))
        self.screen.blit(text_name, text_name_rect)

        text_score = font.render(f"Очки: {self.__current_player_score}", True, "white")
        text_score_rect = text_score.get_rect(toplest=(10, 50))
        self.screen.blit(text_score, text_score_rect)
