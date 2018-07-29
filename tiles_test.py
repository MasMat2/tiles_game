import pygame, sys
from pygame.locals import *

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (87, 199, 208)
GREEN = (150, 253, 109)
PURPLE = (203, 103, 211)
ORANGE = (255, 176, 97)
YELLOW = (238, 226, 0)



class Grid:

    def __init__(self):
        self._array = [[0]*4]*4
        self.size = self.weight, self.height = 100, 100
        self.init_pos = self.init_x, self.init_y = 0,0
        self.center_grid()
        self.tiles_pos = [[], []]
        self.get_pos()

    # Get initial x and y coordinates of the grid
    def center_grid(self):
        center_weight, center_height = (magnitude/2 for magnitude in theGame.size)
        self.init_x = center_weight - self.weight * 2
        self.init_y = center_height - self.height * 2

    # Get a list with limiter of the tiles in the grid
    def get_pos(self):
        for i in range(len(self._array[0])):
            self.tiles_pos[0].append(self.init_x + self.weight*(i))
        for j in range(len(self._array)):
            self.tiles_pos[1].append(self.init_y + self.height*(j))

    # Draw each tile after knowing it's position
    def draw(self):
        for j in range(len(self._array)):
            for i in range(len(self._array[j])):
                left, top = self.tiles_pos[0][i], self.tiles_pos[1][j]
                tile = pygame.Rect(left, top, self.weight, self.height)
                if self._array[j][i] == 0:
                    pygame.draw.rect(theGame._display_surf, BLACK, tile, 0)


class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 512, 512

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0, 32)
        self._running = True
        self.my_grid = Grid()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill(BLUE)
        self.my_grid.draw()
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
    theGame = Game()
    theGame.on_execute()
