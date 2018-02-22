import pygame, importlib
import GlobalVariables as gv
import Constants as consts
from Engine.ImageLoader import ImageLoader
from UI.Button import Button


class StartScreen:
    def __init__(self):
        pass

    def init_ui(self):
        self.res_lbl = Button(20, 'left', 20, 'up', 'tooltip', scale=3)
        self.res_lbl.set_text('Res: (1234, 5678)', 80)
        self.res_lbl.set_text_rect(0, 'center', 0, 'center')

        self.fs_lbl = Button(20, 'left', 20 + self.res_lbl.rect.height, 'up', 'tooltip', scale=3)
        self.fs_lbl.set_text('Fullscreen ON', 80)
        self.fs_lbl.set_text_rect(0, 'center', 0, 'center')

        self.res_1 = Button(0, 'center', 75,
                            'up', 'ui_button', 'ui_button_h', 'ui_button_p', 2)
        self.res_1.set_text('1280x720', 80)
        self.res_1.set_text_rect(0, 'center', 0, 'center')

        self.res_2 = Button(0, 'center', 80 + self.res_1.rect.height, 'up', 'ui_button', 'ui_button_h', 'ui_button_p', 2)
        self.res_2.set_text('1366x768', 80)
        self.res_2.set_text_rect(0, 'center', 0, 'center')

        self.res_3 = Button(0, 'center', 85 + 2 * self.res_1.rect.height, 'up', 'ui_button', 'ui_button_h', 'ui_button_p', 2)
        self.res_3.set_text('1920x1080', 80)
        self.res_3.set_text_rect(0, 'center', 0, 'center')

        self.fs = Button(0, 'center', 90 + 3 * self.res_1.rect.height, 'up', 'ui_button', 'ui_button_h', 'ui_button_p', 2)
        self.fs.set_text('Fullscreen ON', 80)
        self.fs.set_text_rect(0, 'center', 0, 'center')

        self.go = Button(10, 'right', 10, 'bottom', 'ui_button', 'ui_button_h', 'ui_button_p', 2)
        self.go.set_text('PLAY', 80)
        self.go.set_text_rect(0, 'center', 0, 'center')

        gv.Globals.ui.add(self.res_lbl, self.fs_lbl, self.res_1, self.res_2, self.res_3, self.fs, self.go)

    def on_load(self):
        iml = ImageLoader('sprites/')
        gv.Globals.images.update(iml.load([('background',  'background_menu.png'),
                                        ('ui_button',   'ui_menubutton.png'),
                                        ('ui_button_h', 'ui_menubutton_h.png'),
                                        ('ui_button_p', 'ui_menubutton_p.png'),
                                        ('tooltip',     'ui_tooltip.png')]))

    def run(self):
        self.on_load()
        self.init_ui()
        pygame.display.set_caption('Artillery Simulator: settings')

        scr_res = (1280, 720)
        self.res_lbl.set_text('Res: ({}, {})'.format(*scr_res))

        fullsceen = False
        self.fs.set_text('Fullscreen OFF')
        self.fs_lbl.set_text('Fullscreen OFF')

        running = True
        while running:
            gv.Globals.screen.fill((0, 0, 0))

            gv.Globals.input.update()
            gv.Globals.ui.update()
            if gv.Globals.input.quit:
                running = False
            if pygame.K_ESCAPE in gv.Globals.input.k_pressed:
                running = False

            if self.fs.doing_action:
                fullsceen = not fullsceen
                if fullsceen:
                    self.fs.set_text('Fullscreen ON')
                    self.fs_lbl.set_text('Fullscreen ON')
                else:
                    self.fs.set_text('Fullscreen OFF')
                    self.fs_lbl.set_text('Fullscreen OFF')

            if self.res_1.doing_action:
                scr_res = (1280, 720)
                self.res_lbl.set_text('Res: ({}, {})'.format(*scr_res))
            elif self.res_2.doing_action:
                scr_res = (1366, 768)
                self.res_lbl.set_text('Res: ({}, {})'.format(*scr_res))
            elif self.res_3.doing_action:
                scr_res = (1920, 1080)
                self.res_lbl.set_text('Res: ({}, {})'.format(*scr_res))

            if self.go.doing_action:
                consts.SCR_W, consts.SCR_H = scr_res
                consts.SCR_SCALE = consts.SCR_W / consts.ABS_W
                consts.FULLSCREEN = fullsceen
                importlib.reload(gv)
                return 2

            gv.Globals.ui.draw(gv.Globals.screen)

            pygame.display.update()
            gv.Globals.clock.tick(20)
        return 1