import pygame

class Input:
    def __init__(self):
        self.k_pressed   = set()
        self.k_hold      = set()
        self.k_unpressed = set()
        self.m_pos       = (0, 0)
        self.m_pressed   = set()
        self.m_hold      = set()
        self.m_unpressed = set()

        self.events = []
        self.quit = False

    def update(self):
        self.m_hold.update(self.m_pressed)
        self.m_pressed.clear()

        self.k_hold.update(self.k_pressed)
        self.k_pressed.clear()

        for e in pygame.event.get():
            if e.type == pygame.MOUSEMOTION:
                self.m_pos = e.pos
            elif e.type == pygame.MOUSEBUTTONDOWN:
                self.m_pressed.add(e.button)
            elif e.type == pygame.MOUSEBUTTONUP:
                self.m_hold.discard(e.button)
                self.m_unpressed.add(e.button)

            elif e.type == pygame.KEYDOWN:
                self.k_pressed.add(e.key)
            elif e.type == pygame.KEYUP:
                self.k_hold.discard(e.key)
                self.k_unpressed.add(e.key)

            elif e.type == pygame.QUIT:
                self.quit = True
