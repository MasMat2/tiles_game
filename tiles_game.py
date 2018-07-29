import pygame, sys
from pygame.locals import *

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (87, 199, 208)
GREEN = (150, 253, 109)
PURPLE = (203, 103, 211)
ORANGE = (255, 176, 97)
YELLOW = (238, 226, 0)

class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0, 32)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill(BLUE)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()
        sys.exit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = Game()
    theApp.on_execute()
