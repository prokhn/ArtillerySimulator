import pygame
import Constants
from GlobalVariables import Globals, scale
from Engine.ImageLoader import ImageLoader
from UI.UIHandler import UIHandler
from UI.Button import Button

class Menu:
    def __init__(self):
        self.__name__ = 'Menu'
        self.images = {}
        self.ui = UIHandler()

    def init_ui(self):
        self.btn_exit = Button(0, 'center', scale(20), 'bottom',
                                       'ui_button', 'ui_button_h', 'ui_button_p')
        self.btn_exit.set_text('Выход', 50)
        self.btn_exit.set_text_rect(0, 'center', 0, 'center')

        self.btn_about = Button(0, 'center', scale(25) + self.btn_exit.rect.height, 'bottom',
                               'ui_button', 'ui_button_h', 'ui_button_p')
        self.btn_about.set_text('Об игре', 50)
        self.btn_about.set_text_rect(0, 'center', 0, 'center')

        self.btn_play = Button(0, 'center', scale(30) + 2 * self.btn_exit.rect.height, 'bottom',
                                       'ui_button', 'ui_button_h', 'ui_button_p')
        self.btn_play.set_text('Играть', 50)
        self.btn_play.set_text_rect(0, 'center', 0, 'center')

        self.ui.add(self.btn_play, self.btn_about, self.btn_exit)

    def on_load(self):
        iml = ImageLoader('sprites/')
        Globals.images.update(iml.load([('background', 'background_menu.png'),
                                        ('ui_button',  'ui_menubutton.png'),
                                        ('ui_button_h', 'ui_menubutton_h.png'),
                                        ('ui_button_p', 'ui_menubutton_p.png')]))

    def run(self):
        pygame.init()

        self.on_load()
        self.init_ui()
        Globals.logger('o', 'Menu.run() - loading ok')

        running = True
        while running:
            Globals.input.update()
            self.ui.update()
            if pygame.K_ESCAPE in Globals.input.k_pressed:
                Globals.input.quit = True
                return Constants.EXC_EXIT
            elif Globals.input.quit:
                return Constants.EXC_EXIT
            if self.btn_exit.doing_action:
                return Constants.EXC_EXIT
            if self.btn_play.doing_action:
                return Constants.EXC_GAME
            if self.btn_about.doing_action:
                return Constants.EXC_ABOUT

            Globals.screen.blit(Globals.images['background'], (0, 0))

            self.ui.draw(Globals.screen)

            pygame.display.update()
            Globals.clock.tick(Globals.fps)