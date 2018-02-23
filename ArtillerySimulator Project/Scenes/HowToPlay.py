import pygame
import Constants
from GlobalVariables import Globals, scale
from Engine.ImageLoader import ImageLoader
from UI.Button import Button

class HowToPlayScene:
    def __init__(self):
        self.__name__ = 'HowToPlay'

    def init_ui(self):
        self.btn_back = Button(scale(10), 'right', scale(10), 'bottom', 'ui_button', 'ui_button_h', 'ui_button_p')
        self.btn_back.set_text('Назад', 50)
        self.btn_back.set_text_rect(0, 'center', 0, 'center')

        Globals.ui.add(self.btn_back)

    def on_load(self):
        iml = ImageLoader('sprites/')
        Globals.images.update(iml.load([('bg', 'HowToPlay.png'),
                                        ('ui_button', 'ui_menubutton.png'),
                                        ('ui_button_h', 'ui_menubutton_h.png'),
                                        ('ui_button_p', 'ui_menubutton_p.png')]))

    def run(self):
        self.on_load()
        self.init_ui()
        Globals.logger('o', 'HowToPlay.run() - loading ok')

        running = True
        while running:
            Globals.input.update()
            Globals.ui.update()
            if pygame.K_ESCAPE in Globals.input.k_pressed:
                return Constants.EXC_MENU
            if Globals.input.quit:
                return Constants.EXC_EXIT

            if self.btn_back.doing_action:
                return Constants.EXC_MENU

            Globals.screen.blit(Globals.images['bg'], (0, 0))
            Globals.ui.draw(Globals.screen)

            pygame.display.update()
            Globals.clock.tick(30)

if __name__ == '__main__':
    pygame.init()
    sc = HowToPlayScene()
    sc.run()