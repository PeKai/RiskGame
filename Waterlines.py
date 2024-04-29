import random

import pygame as pg


class Waterlines:
    def __init__(self, name: str, coords: list, color):
        self.name = name
        self.coords = coords
        self.color = color
        self.bordering = name.split()
        self.xymin, self.xymax = self.getMiniMax()

    def getMiniMax(self):
        xmin, ymin = -100000, -100000
        xmax, ymax = 100000, 100000
        for r in self.coords:
            if xmin < r.x.real:
                xmin = r.x.real
                ymin = r.y.real
            if xmax > r.x.real:
                xmax = r.x.real
                ymax = r.y.real
        return pg.Vector2(xmin, ymin), pg.Vector2(xmax, ymax)

    def draw(self, screen, long_scan):
        pg.draw.line(screen, self.color, (self.xymin.x - long_scan.x + 150,
                                          self.xymin.y - long_scan.y + 35),
                     (self.xymax.x - long_scan.x + 150,
                      self.xymax.y - long_scan.y + 35), width=2)