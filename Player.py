import pygame as pg
import time

from src import Country, Map

# Work in progress. If it isn't working, just delete Player class!
class Player:
    def __init__(self, country):
        self.my_countries = ["Brazil"]

    def military_placements(self, units):
        if self.world.current_hov == n and pg.mouse.get_pressed()[0]:
            for country in self.my_countries:
                self.world.countries[country].Infantry += units
                time.sleep(0.3)
