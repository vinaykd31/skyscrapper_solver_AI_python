import pygame


class Button:
    def __init__(self, x, y, width, height,  colour=(73, 73, 73), function=None,text=None):
        self.image = pygame.Surface((width, height))
        self.pos = (x, y)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.text = text
        self.colour = colour
        self.highlightedColour = (189, 189, 189)
        self.function = function
        self.highlighted = False
        self.width = width
        self.height = height

    def update(self, mouse):
        if self.rect.collidepoint(mouse):
            self.highlighted = True
        else:
            self.highlighted = False

    def draw(self, window):
        self.image.fill(self.highlightedColour if self.highlighted else self.colour)
        if self.text:
            self.drawText(self.text)
        window.blit(self.image, self.pos)

    def click(self):
        if self.function:
            self.function()
        else:
            print('its none' + str(self.pos[0]))
            self.function()

    def drawText(self, text):
        font = pygame.font.SysFont("arial", 20, bold=1)
        text = font.render(text, False, (0,0,0))
        width, height = text.get_size()
        x = (self.width-width)//2
        y = (self.height-height)//2
        self.image.blit(text, (x, y))
