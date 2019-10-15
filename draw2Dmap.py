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

BACKGROUND = pg.Color("darkslategray")
SCREEN_SIZE = (1200, 650)

def draw_map(n, m, listPoint, size):    
    done = False
    clock = pg.time.Clock()
    
    while not done:
        clock.tick(10)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done=True

        screen = pg.display.get_surface()
        screen.fill(WHITE)
        for i in range(0, len(listPoint)):
            for j in range(0, len(listPoint[i])):
                if listPoint[i][j] == 0:
                    pg.draw.rect(screen, BLACK, [i*size, j*size, size, size], 2)
                elif listPoint[i][j] == 1:
                    pg.draw.rect(screen, RED, [i*size, j*size, size, size])
                else:
                    pg.draw.rect(screen, BLUE, [i*size, j*size, size, size])
        
        pg.display.flip()
    
    pg.quit()

class Map(object):
    def __init__(self, size, center, listPoint):
        self.width, self.height = size
        self.squash_ratio = 0.5
        self.scale = 10
        #self.mapping = MapGen(size, listPoint)
        n, m = size
        draw_map(n, m, listPoint, 20)
        self.draw_order = None
        #self.tiles, self.points = self.make_map()
        #self.start_points = self.points.copy()
        self.recenter(center)
        
        self.change = True

    def make_map(self):
        tiles = pg.sprite.Group()
        row_offset = 2
        col_offset = 2
        points = []
        for i in range(self.width):
            for j in range(self.height):
                biome = self.mapping.terrain[i][j]
                pos = (col_offset*i, row_offset*j)
                points.append(pos)
                hextile = RectTile(biome, i*self.height+j, tiles)
                if i == self.width//2 and j == self.height//2:
                    self.center = pos
        points = np.array([points], dtype=float)
        return tiles, points

    def reset(self):
        self.squash_ratio = 0.5
        self.scale = 10
        self.change = True

    def recenter(self, new_center):
        current = self.center
        offset = new_center[0] - current[0], new_center[1] - current[1]
        self.points += offset
        self.start_points += offset
        self.center = new_center

    def zoom(self, ammount):
        self.scale = max(3, min(20, self.scale + ammount))
        self.change = True

    def transform(self, rot):
        points = (self.start_points - self.center)*self.scale
        points = np.dot(points, rot.T)
        points = points * (1, self.squash_ratio) + self.center
        return points
    
    def draw(self, surface):
        for tile in self.draw_order:
            tile.draw(surface)

    def update(self):
        rel = pg.mouse.get_rel()
        if pg.mouse.get_pressed()[2]:
            self.rotate(-rel[0]/2)
            self.azimuthal(1, rel[1]*0.0025)
        if self.change:
            angle = np.radians(self.angle)
            cos = np.cos(angle)
            sin = np.sin(angle)
            rot = np.array([[cos, -sin], [sin, cos]])
            self.points = self.transform(rot)
            tile_images, center = make_tiles(rot, self.scale, self.squash_ratio)
            self.tiles.update(tile_images, center, self.points)
            self.draw_order = sorted(self.tiles, key=lambda t: t.rect.bottom)
            self.change = False

    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_PLUS, pg.K_KP_PLUS, pg.K_EQUALS):
                self.zoom(2)
            elif event.key in (pg.K_MINUS, pg.K_KP_MINUS):
                self.zoom(-2)
            elif event.key == pg.K_SPACE:
                self.reset()
        elif event.type == pg.MOUSEBUTTONDOWN:
            pg.mouse.get_rel()
            if event.button == 4:
                self.zoom(1)
            elif event.button == 5:
                self.zoom(-1)
            

class App(object):
    def __init__(self, n, m, listPoint):
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.done = False
        self.map = Map((n,m), self.screen_rect.center, listPoint)
        
    # def update(self):
    #     self.map.update()

    # def render(self):
    #     self.screen.fill(BACKGROUND)
    #     self.map.draw(self.screen)
    #     pg.display.update()

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.map.get_event(event)

    def main_loop(self):
        while not self.done:
            self.event_loop()
            #self.update()
            #self.render()
            self.clock.tick(10)

def main():
    pg.init()
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    n = 4
    m = 4
    map = np.full((n, m),0)
    map[2][2] = 1
    map[1][1]=2
    App(n, m, map).main_loop()
    pg.quit()

if __name__ == "__main__":
    main()