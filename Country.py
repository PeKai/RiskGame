import pygame as pg


class Country:
    def __init__(self, name, coords, color):
        self.name = name
        self.coords = coords
        self.color = color

    def draw(self, screen, long_scan):
        pg.draw.polygon(
            screen,
            self.color,
            [(x - long_scan.x, y - long_scan.y + 35) for x, y in self.coords],
        )
