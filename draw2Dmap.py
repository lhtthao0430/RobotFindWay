import pygame as pg
from math import pi
import numpy as np

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
CAPTION = "Map 2D"

BACKGROUND = pg.Color("white")
SCREEN_SIZE = (1200, 650)

class Map(object):
    def __init__(self, sizeMap, map):
        self.width, self.height = sizeMap
        self.map = map
        self.scale = int(min(SCREEN_SIZE[0]/(self.width+10), SCREEN_SIZE[1]/(self.height+10)))
        self.draw_map()
        self.change = True

    def draw_map(self):
        start_point = ((SCREEN_SIZE[0] - self.scale * self.width) / 2, (SCREEN_SIZE[1] - self.scale * self.height) / 2)
        screen = pg.display.get_surface()
        screen.fill(BACKGROUND)
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
                if self.map[i][j] == 0:
                    pg.draw.rect(screen, BLACK, [start_point[0] + i*self.scale, start_point[1] + j*self.scale, self.scale, self.scale], 2)
                elif self.map[i][j] == 1:
                    pg.draw.rect(screen, RED, [start_point[0] + i*self.scale, start_point[1] + j*self.scale, self.scale, self.scale])
                else:
                    pg.draw.rect(screen, BLUE, [start_point[0] + i*self.scale, start_point[1] + j*self.scale, self.scale, self.scale])
        self.change = True

    def reset(self):
        self.scale = int(min(SCREEN_SIZE[0]/(self.width+10), SCREEN_SIZE[1]/(self.height+10)))
        self.change = True

    def zoom(self, ammount):
        self.scale = max(30, min(200, self.scale + ammount))
        self.change = True

    def draw(self):
        self.draw_map()

    def update(self):
        if self.change:
            self.draw_map()
            self.change = False

    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_PLUS, pg.K_KP_PLUS, pg.K_EQUALS):
                self.zoom(20)
            elif event.key in (pg.K_MINUS, pg.K_KP_MINUS):
                self.zoom(-20)
            elif event.key == pg.K_SPACE:
                self.reset()
        elif event.type == pg.MOUSEBUTTONDOWN:
            pg.mouse.get_rel()
            if event.button == 4:
                self.zoom(10)
            elif event.button == 5:
                self.zoom(-10)

class App(object):
    def __init__(self, n, m, listPoint):
        self.clock = pg.time.Clock()
        self.done = False
        self.map = Map((n,m), listPoint)
        
    def update(self):
        self.map.update()
        pg.display.update()

    def render(self):
        self.screen.fill(BACKGROUND)
        self.map.draw()
        pg.display.update()

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.map.get_event(event)

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.update()
            self.clock.tick(10)

def draw2Dmap(n, m, map):
    pg.init()
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    App(n, m, map).main_loop()
    pg.quit()

map = np.full([23, 19], 0)
map[1][1] = 2
map[2][2] = 1
draw2Dmap(23, 19, map)