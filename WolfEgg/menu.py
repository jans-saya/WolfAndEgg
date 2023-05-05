from game import Game
import pygame


class Menu:
    """Основной класс меню"""
    def __init__(self, game):
        self.game = game
        self.mid_w = self.game.DISPLAY_W / 2
        self.mid_h = self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 70, 70)
        self.offset2 = 5
        self.offset = 175

    def draw_cursor(self):
        self.game.draw_text('*', 60, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    """Класс главного окна  (открывается в самом начале)"""
    def __init__(self, game):
        Menu.__init__(self, game)
        self.start_x, self.start_y = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 1.7
        self.helping_x, self.helping_y = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 1.5
        self.state = "Начало"
        self.cursor_rect.midtop = (self.start_x - self.offset, self.start_y + self.offset2)

    def draw_cursor(self):
        self.game.draw_text('*', 60, self.cursor_rect.x, self.cursor_rect.y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.WHITE)
            self.game.draw_text('Ну, погоди!', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2.4)
            self.game.draw_text("Начать игру", 60, self.start_x, self.start_y)
            self.game.draw_text("Помощь", 60, self.helping_x, self.helping_y)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Начало":
                self.cursor_rect.midtop = (self.helping_x - self.offset, self.helping_y + self.offset2)
                self.state = "Помощь"
            elif self.state == "Помощь":
                self.cursor_rect.midtop = (self.start_x - self.offset, self.start_y + self.offset2)
                self.state = "Начало"
        elif self.game.UP_KEY:
            if self.state == "Начало":
                self.cursor_rect.midtop = (self.helping_x - self.offset, self.helping_y + self.offset2)
                self.state = "Помощь"
            elif self.state == "Помощь":
                self.cursor_rect.midtop = (self.start_x - self.offset, self.start_y + self.offset2)
                self.state = "Начало"

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Помощь":
                self.game.curr_menu = self.game.helping
            elif self.state == 'Начало':
                self.game.curr_menu = self.game.difficulty
            self.run_display = False


class Difficulty(Menu):
    """Класс выбора сложности"""
    def __init__(self, game):
        Menu.__init__(self, game)
        self.easy_x, self.easy_y = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2.4
        self.normal_x, self.normal_y = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2.0
        self.hard_x, self.hard_y = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 1.7
        self.state = "Легко"
        self.cursor_rect.midtop = (self.easy_x - self.offset, self.easy_y + self.offset2)

    def draw_cursor(self):
        self.game.draw_text('*', 60, self.cursor_rect.x, self.cursor_rect.y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.WHITE)
            self.game.draw_text('Легко', 60, self.easy_x, self.easy_y)
            self.game.draw_text("Нормально", 60, self.normal_x, self.normal_y)
            self.game.draw_text("Сложно", 60, self.hard_x, self.hard_y)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Легко":
                self.cursor_rect.midtop = (self.normal_x - self.offset, self.normal_y + self.offset2)
                self.state = "Нормально"
            elif self.state == "Нормально":
                self.cursor_rect.midtop = (self.hard_x - self.offset, self.hard_y + self.offset2)
                self.state = "Сложно"
            elif self.state == "Сложно":
                self.cursor_rect.midtop = (self.easy_x - self.offset, self.easy_y + self.offset2)
                self.state = "Легко"
        elif self.game.UP_KEY:
            if self.state == "Легко":
                self.cursor_rect.midtop = (self.hard_x - self.offset, self.hard_y + self.offset2)
                self.state = "Сложно"
            elif self.state == "Сложно":
                self.cursor_rect.midtop = (self.normal_x - self.offset, self.normal_y + self.offset2)
                self.state = "Нормально"
            elif self.state == "Нормально":
                self.cursor_rect.midtop = (self.easy_x - self.offset, self.easy_y + self.offset2)
                self.state = "Легко"
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            width = 1400
            height = 900
            size = width, height
            v = 250
            fps = 60
            clock = pygame.time.Clock()
            screen = pygame.display.set_mode(size)
            if self.state == "Легко":
                eggs_speed = 3000
                game = Game(screen, v, fps, eggs_speed,
                            clock, width, height)
                game.run()
                k = game.run()
                f = open('./data/data.txt', 'w')
                f.write(str(k + 1))
                self.game.curr_menu = self.game.game_over
            elif self.state == 'Нормально':
                eggs_speed = 2100
                game = Game(screen, v, fps, eggs_speed,
                            clock, width, height)
                game.run()
                k = game.run()
                f = open('./data/data.txt', 'w')
                f.write(str(k + 1))
                self.game.curr_menu = self.game.game_over
            elif self.state == "Сложно":
                eggs_speed = 1500
                game = Game(screen, v, fps, eggs_speed,
                            clock, width, height)
                game.run()
                k = game.run()
                f = open('./data/data.txt', 'w')
                f.write(str(k))
                self.game.curr_menu = self.game.game_over
            self.run_display = False


class GameOver(Menu):
    """Класс окончания игры"""
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        f = open('./data/data.txt', 'r+')
        eggs_counter = f.readline()
        f.close()
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.WHITE)
            self.game.draw_text('Вы проиграли!', 80, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2.4)
            self.game.draw_text(f'Ваш результат: {int(eggs_counter) - 3}',
                                60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 1.9)
            self.blit_screen()


class HelpMenu(Menu):
    """Класс помощи"""
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.WHITE)
            self.game.draw_text('Помощь!', 80, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2.4)
            self.game.draw_text('При помощи стрелочек управляй волком,', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
            self.game.draw_text('чтобы поймать как можно больше яиц.', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 1.8)
            self.game.draw_text('Чтобы вернуться обратно нажми backspace.', 60, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 1.4)
            self.blit_screen()
