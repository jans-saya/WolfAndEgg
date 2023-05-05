from utils import load_image
import pygame
import random


class Egg:
    """
    Данный класс описывает логику движения яиц в игре
    """

    def __init__(self, screen: pygame.Surface, width_screen, height_screen, speed: int, fps: int):
        """
        Инициализирующий метод, принимающий в себя основные параметры
        :param screen: объект холста, на котором сконструировать начальное положение яйца
        :param width_screen: ширина холста
        :param height_screen: высота холста
        :param speed: интервал вызова собственного события игры "появление яйца", в мс
        :param fps: ФПС
        """
        self.screen = screen
        self.width_screen = width_screen
        self.height_screen = height_screen
        self.speed = speed
        self.fps = fps
        self.egg_image = load_image('../data/egg.png', colorkey=-1)
        self.egg_size = 20
        self.side = random.randint(1, 4)
        self.coords = None
        self.degree = 0
        self.delta_y = self.speed // self.fps - 0.7
        self._construct_egg()

    def _construct_egg(self):
        """
        Protected метод класса, защищенный, чтобы применять только внутри класса, описывает
        начальное положение яйца
        :return:
        """
        if self.side == 1:
            coords = (0 + self.egg_size, int(self.height_screen * .18))
        elif self.side == 2:
            coords = (self.width_screen - self.egg_size, int(self.height_screen * .18))
        elif self.side == 3:
            coords = (self.width_screen - self.egg_size, int(self.height_screen * .45))
        else:
            coords = (0 + self.egg_size, int(self.height_screen * .45))
        self.coords = coords

    def move(self, screen: pygame.Surface):
        """
        Отвечает за перемещение яйца на холсте
        :param screen: холст
        :return:
        """
        egg_image = pygame.transform.rotate(self.egg_image, self.degree)
        self.degree = (self.degree + 10) % 360
        delta_x = self.speed // self.fps
        delta_x = delta_x if self.side == 1 or self.side == 4 else -delta_x
        self.coords = (self.coords[0] + delta_x, self.coords[1] + self.delta_y)
        screen.blit(egg_image, self.coords)
        return screen

    def check_position(self):
        """
        проверяет не зашло ли яйцо за условную границу
        :return: bool значение
        """
        if self.side == 1 or self.side == 4:
            return self.coords[0] < self.width_screen // 3 - 60 and self.coords[1] < self.height_screen - self.egg_size
        else:
            return self.coords[0] > self.width_screen // 3 * 2 + 60 and self.coords[
                1] < self.height_screen - self.egg_size
