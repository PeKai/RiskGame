import pygame as pg
import time

from src import Country, Map

# Work in progress. If it isn't working, just delete Player class!
class Player:
    def __init__(self, country):
        self.my_countries = ["Brazil"]

    def military_placements(self):
        for country in self.my_countries:
            if self.world.current_hov == n and pg.mouse.get_pressed()[0]:
                self.world.countries[country].Infantry += 2
                time.sleep(0.3)
