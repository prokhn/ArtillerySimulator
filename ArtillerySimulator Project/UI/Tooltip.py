import pygame
from GlobalVariables import Globals


class Tooltip:
    def __init__(self, ui_listener, dx, dy, img_tag, text_rows, font_size=30):
        self.ui_listener = ui_listener
        self.image = Globals.images[img_tag]
        self.rect = self.image.get_rect()
        self.rect.centerx = self.ui_listener.rect.centerx + dx
        self.rect.centery = self.ui_listener.rect.centery + dy
        self.font = pygame.font.Font(None, font_size)

        self.set_text(text_rows)

        self.active = True

    def set_text(self, text_rows, hor_border=5, vert_border=5):
        self.text_rows = text_rows
        self.text_rendered = []
        for text in text_rows:
            text_rendered = self.font.render(text, 0, pygame.Color('black'))
            text_rect = text_rendered.get_rect()
            text_rect.x = self.rect.x + hor_border
            self.text_rendered.append((text_rendered, text_rect))

        all_height = sum([text_rect.height for text_rendered, text_rect in self.text_rendered])
        border = max(0, (self.rect.height - all_height - 2 * vert_border) // 2)
        print(border)
        curr_y = vert_border
        for text_rendered, text_rect in self.text_rendered:
            text_rect.y = self.rect.y + curr_y
            curr_y += text_rect.height + border

    def set_font_size(self, font_size):
        self.font = pygame.font.Font(None, font_size)

    def update(self):
        if self.ui_listener.hovered or self.ui_listener.clicked:
            self.active = True
        else:
            self.active = False

    def draw(self, screen: pygame.Surface):
        if self.active:
            screen.blit(self.image, self.rect.topleft)
            for text_rendered, text_rect in self.text_rendered:
                screen.blit(text_rendered, text_rect.topleft)