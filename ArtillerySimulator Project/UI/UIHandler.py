class UIHandler():
    def __init__(self):
        super().__init__()
        self.elements = []

    def add(self, *ui_elems):
        for el in ui_elems:
            self.elements.append(el)

    def update(self):
        for el in self.elements:
            el.update()

    def draw(self, surf):
        for el in self.elements:
            el.draw(surf)

    def clear(self):
        self.elements = []