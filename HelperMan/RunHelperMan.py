import pygame as pg

import game_config
import game_config as config
from GameOdjects.Helper import Helpers
from game_dialog import GameDialog
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
        self.background = load_img("picture/grass.png")
        # Скорость обновления кадров
        self.__FPS = config.FPS
        self.__clock = pg.time.Clock()

        # Текущее значение очков игрока
        self.__current_player_score = 0

        # Создаем объект класса GameDialog
        self.__game_dialog = GameDialog()

        # Запрашиваем имя игрока
        self.__player_name = self.__game_dialog.show_dialog_login()
        print(self.__player_name)

        # TODO
        # self.__first_player_score = 10

        # Вызываем метод инициализациии остальных параметров
        self.__init_game()

    def __init_game(self):
        # Создаем объект основного окна
        self.screen = pg.display.set_mode(game_config.WINDOW_SIZE)
        pg.display.set_caption("Хелпер")

        # Cписок кактусов
        self.kaktus_sprite_group = pg.sprite.Group()

        # Объект хелпера
        self.hepler = Helpers(self.screen)

        self.kaktus_list = []

        # В начале игры будет всего три яблока
        for i in range(3):
            # Объект астероида
            kaktus = Kaktuss(self.screen)
            self.kaktus_list.append(kaktus)
            self.kaktus_sprite_group.add(kaktus)

    def __draw_scene(self):
        # отрисовка
        self.screen.blit(self.background, (0, 0))

        # self.apples.update()
        self.kaktus_sprite_group.draw(self.screen)
        self.hepler.update()
        self.hepler.draw()

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
