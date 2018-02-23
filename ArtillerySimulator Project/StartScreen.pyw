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

        Globals.ui.add(self.res_lbl, self.fs_lbl, self.res_1, self.res_2, self.res_3, self.fs, self.go)

    def on_load(self):
        iml = ImageLoader('sprites/')
        Globals.images.update(iml.load([('background',  'background_menu.png'),
                                        ('ui_button',   'ui_menubutton.png'),
                                        ('ui_button_h', 'ui_menubutton_h.png'),
                                        ('ui_button_p', 'ui_menubutton_p.png'),
                                        ('tooltip',     'ui_tooltip.png')]))

    @staticmethod
    def save_settings(resolution, fullscreen):
        with open('Constants.py', 'r', encoding='utf-8') as file:
            file_data = file.readlines()
            for ind, line in enumerate(file_data):
                if line.rstrip().startswith('SCR_W'):
                    file_data[ind] = 'SCR_W = {}\n'.format(resolution[0])
                elif line.rstrip().startswith('SCR_H'):
                    file_data[ind] = 'SCR_H = {}\n'.format(resolution[1])
                elif line.rstrip().startswith('FULLSCREEN'):
                    if fullscreen:
                        file_data[ind] = 'FULLSCREEN = True\n'
                    else:
                        file_data[ind] = 'FULLSCREEN = False\n'

        with open('Constants.py', 'w', encoding='utf-8') as file:
            file.write(''.join(file_data))

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
            Globals.screen.fill((0, 0, 0))

            Globals.input.update()
            Globals.ui.update()
            if Globals.input.quit:
                running = False
            if pygame.K_ESCAPE in Globals.input.k_pressed:
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
                self.save_settings(scr_res, fullsceen)
                return 1

            Globals.ui.draw(Globals.screen)

            pygame.display.update()
            Globals.clock.tick(20)
        return 0

if __name__ == '__main__':
    StartScreen().save_settings((600, 300), False)
    import pygame, subprocess, os
    from GlobalVariables import Globals
    from Engine.ImageLoader import ImageLoader
    from UI.Button import Button

    pygame.init()
    sc = StartScreen()
    exit_code = sc.run()
    pygame.quit()
    if exit_code == 0:
        exit(0)
    else:
        try:
            if os.name == 'nt':
                game = subprocess.Popen('ArtillerySimulator.bat')
            else:
                game = subprocess.Popen(['$nohup', 'GameMain.pyw &'])
        except Exception as e:
            with open('_ERROR_.txt', 'w', encoding='utf-8') as file:
                file.write('Some error occured when trying to lauch GameMain.pyw\n')
                file.write('Ask developers for help\n')
                file.write('Error args: %s' % str(e.args))