from __future__ import division

import numpy as np
import pygame as pg
import opensimplex as simp
import time



BACKGROUND = pg.Color("darkslategray")
SCREEN_SIZE = (1200, 650)

BASE_POINTS = np.array([[(-1, -1), (1, -1), (1, 1), (-1, 1)]])

TERRAIN = [("Map", 0.3),("Polygon", 0.8), ("Robot", 1), ("Start", 1), ("Goal", 1), ("Diamond", 1)]


TERRAIN_COLORS = {"Map" : pg.Color("white"),
                  "Polygon" : pg.Color("red"),
                  "Robot" : pg.Color("blue"),
                  "Start" : pg.Color("yellow"),
                  "Goal" : pg.Color("green"),
                  "Diamond": pg.Color("yellow")}


TERRAIN_HEIGHTS = {"Map" : 5,
                   "Polygon": 10,
                   "Robot": 20,
                   "Start": 20,
                   "Goal": 20,
                   "Diamond": 15}
                   
                   
def text_objects(text, font):
    textSurface = font.render(text, True, pg.Color("black"))
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pg.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((SCREEN_SIZE[0]/2),(SCREEN_SIZE[1]/2))

class MapGen(object):    
    def __init__(self, size, map):
        self.size = self.width, self.height = size
        self.map = map
        self.terrain = self.gen_map()

    def gen_map(self):
        mapping = [["Map"]*self.height for _ in range(self.width)]
        for i in range(self.width):
            for j in range(self.height):
                if self.map[i][j] == 1 or self.map[i][j] == 11 or self.map[i][j] == 12 or self.map[i][j] == 13 or self.map[i][j] == 14:
                    mapping[i][j] = "Polygon"
                elif self.map[i][j] == 2:
                    mapping[i][j] = "Robot"
                elif self.map[i][j] == 3:
                    mapping[i][j] = "Start"
                elif self.map[i][j] == 4:
                    mapping[i][j] = "Goal"
                elif self.map[i][j] == 6:
                    mapping[i][j] = "Diamond"
        return mapping


class RectTile(pg.sprite.Sprite):
    def __init__(self, biome, index, *groups):
        super(RectTile, self).__init__(*groups)
        self.index = index
        self.image = None
        self.rect = None
        self.biome = biome

    def update(self, tiles, offset, point_array):
        self.image = tiles[self.biome]
        self.rect = self.image.get_rect()
        point = point_array[0][self.index]
        self.rect.bottomleft = point[0] - offset[0], point[1] + offset[1]

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Map(object):
    def __init__(self, size, center, map):
        self.width, self.height = size
        self.angle = 0
        self.squash_ratio = 0.5
        self.scale = 10
        self.mapping = MapGen(size, map)
        self.draw_order = None
        self.tiles, self.points = self.make_map()
        self.start_points = self.points.copy()
        self.recenter(center)
        self.change = True
        self.angle_delta = 60

    def changeData(self, center, map):
        self.mapping = MapGen(self.mapping.size, map)
        self.tiles, self.points = self.make_map()
        self.start_points = self.points.copy()
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
                recttile = RectTile(biome, i*self.height+j, tiles)
                if i == self.width//2 and j == self.height//2:
                    self.center = pos
        points = np.array([points], dtype=float)
        return tiles, points

    def reset(self):
        self.angle = 0
        self.squash_ratio = 0.5
        self.scale = 10
        self.change = True

    def recenter(self, new_center):
        current = self.center
        offset = new_center[0] - current[0], new_center[1] - current[1]
        self.points += offset
        self.start_points += offset
        self.center = new_center

    def azimuthal(self, direction, inc=0.1):
        self.squash_ratio = max(0.1, min(1, self.squash_ratio + inc*direction))
        self.change = True

    def rotate(self, angle):
        self.angle = (self.angle + angle) % (360)
        self.change = True

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
            if event.key == pg.K_LEFT:
                self.rotate(-self.angle_delta)
            elif event.key == pg.K_RIGHT:
                self.rotate(self.angle_delta)
            elif event.key == pg.K_DOWN:
                self.azimuthal(1)
            elif event.key == pg.K_UP:
                self.azimuthal(-1)
            elif event.key in (pg.K_PLUS, pg.K_KP_PLUS, pg.K_EQUALS):
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
    def __init__(self, n, m, map, res, run_time):
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.done = False
        self.map = Map((n,m), self.screen_rect.center, map)
        self.res = res
        self.run_time = run_time
        
    def update(self):
        self.map.update()

    def render(self):
        self.screen.fill(BACKGROUND)
        self.map.draw(self.screen)
        smallText = pg.font.Font('freesansbold.ttf',30)
        TextSurf, TextRect = text_objects("Run time: " + str(round(self.run_time*1000,5)) + "ms", smallText)
        TextRect.center = ((SCREEN_SIZE[0]-200),(SCREEN_SIZE[1]-50))
        self.screen.blit(TextSurf, TextRect)
        if (len(self.res) == 0):
            largeText = pg.font.Font('freesansbold.ttf',115)
            TextSurf, TextRect = text_objects("Can't find the way", largeText)
            TextRect.center = ((SCREEN_SIZE[0]/2),(SCREEN_SIZE[1]/1.5))
            self.screen.blit(TextSurf, TextRect)
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
            self.render()
            self.clock.tick(10)

    def list_main_loop(self, n, m, maps):
        for map in maps:
            self.map.changeData(self.screen_rect.center, map)
            self.event_loop()
            self.update()
            self.render()
            time.sleep(0.2)
        self.main_loop()

def make_tiles(rot, scale, squash):
    border = 2 if scale > 8 else 1
    points = (np.dot(BASE_POINTS[0]*scale, rot.T) * (1, squash))
    min_x, min_y = np.min(points[:,0]), np.min(points[:,1])
    points -= min_x, min_y
    points = np.ceil(points)
    max_x, max_y = np.max(points[:,0]), np.max(points[:,1])
    footprint = pg.Rect((0, 0, max_x, max_y))
    tiles = {}
    for biome,_ in TERRAIN:
        color = TERRAIN_COLORS[biome]
        bottom_color = [0.5 * col for col in color[:3]]
        height = TERRAIN_HEIGHTS[biome]*(scale/5)
        surf = pg.Surface((max_x+border,max_y+height+border), flags=pg.SRCALPHA)
        top = points.tolist()
        poly = sorted(top, key=lambda p: p[1], reverse=True)
        top_order = sorted(poly[:3])
        bottom_order = [(x,y+height) for x,y in top_order]
        poly_order = bottom_order + top_order[::-1]
        pg.draw.polygon(surf, bottom_color, poly_order)
        pg.draw.polygon(surf, color, top)
        pg.draw.lines(surf, pg.Color("black"), 0, bottom_order, border)
        pg.draw.lines(surf, pg.Color("black"), 1, top, border)
        for pair in zip(bottom_order, top_order):
            pg.draw.line(surf, pg.Color("black"), pair[0], pair[1], border)
        tiles[biome] = surf
    return tiles, (footprint.w//2, footprint.h//2)
    

import os

def draw3DMap(n, m, map, res, title, run_time):
    x = 100
    y = 0    
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    pg.init()
    pg.display.set_caption(title)
    pg.display.set_mode(SCREEN_SIZE)
    App(n, m, map, res, run_time).main_loop()
    pg.quit()

def draw3DMapList(n, m, maps, title, run_time):
    x = 100
    y = 0    
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    pg.init()
    pg.display.set_caption(title)
    pg.display.set_mode(SCREEN_SIZE)
    App(n,m, maps[0], maps, run_time).list_main_loop(n, m, maps)
    pg.quit()