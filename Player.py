import random

import pygame as pg
import time
from src import Country, Map


class Player:
    def __init__(self, world: Map, color):
        self.turn_is = None
        self.world = world
        self.color = color
        self.timer = pg.time.get_ticks()
        self.controlled_countries = []
        self.bordering_countries()
        self.player_units = 0
        self.inland = ""
        self.outland = ""
        self.moved_troops = 0

    def update(self, mode):
        if mode == "pu":
            self.place_units()
        elif mode == "mu":
            self.move_units()
        elif mode == "au":
            self.attack_country()

    def place_units(self):
        self.bordering_countries()
        if self.world.current_hov is None:
            pass
        else:
            if self.world.current_hov.sum() == 0 and pg.mouse.get_pressed()[0]:
                time.sleep(0.005)
                self.controlled_countries.append(self.world.current_hov)
                self.world.current_hov.color = self.color
                self.world.current_hov.Infantry += 1
            elif self.world.current_hov.sum() > 0 and pg.mouse.get_pressed()[
                0] and self.world.current_hov in self.controlled_countries:
                time.sleep(0.005)
                self.world.current_hov.Infantry += 1
            elif self.world.current_hov.sum() > 1 and pg.mouse.get_pressed()[
                2] and self.world.current_hov in self.controlled_countries:
                time.sleep(0.005)
                self.world.current_hov.Infantry -= 1
            elif self.world.current_hov.sum() == 1 and pg.mouse.get_pressed()[
                2] and self.world.current_hov in self.controlled_countries:
                time.sleep(0.005)
                self.controlled_countries.remove(self.world.current_hov)
                self.world.current_hov.color = (random.randrange(70, 250),
                                                random.randrange(65, 245),
                                                random.randrange(55, 220))
                self.world.current_hov.Infantry -= 1
            else:
                pass

    def move_units(self):
        mouse_pressed = pg.mouse.get_pressed()
        key_pressed = pg.key.get_pressed()
        current_hov_country = None

        if mouse_pressed[2]:
            self.inland = ""
            self.outland = ""
            self.moved_troops = 0

        if self.world.current_hov:
            for country in self.controlled_countries:
                if self.world.current_hov == country:
                    current_hov_country = country.name
                    break

        if not self.outland and self.inland and current_hov_country and current_hov_country != self.inland:
            self.outland = current_hov_country
        elif not self.inland and current_hov_country and mouse_pressed[0]:
            self.inland = current_hov_country

        if self.inland and self.outland:
            outland_class = self.world.countries[self.outland]
            inland_class = self.world.countries[self.inland]

            if key_pressed[pg.K_SPACE]:
                inland_class.Infantry -= self.moved_troops
                outland_class.Infantry += self.moved_troops
                self.moved_troops = 0
                self.inland = ""
                self.outland = ""

            if key_pressed[pg.K_w] and (inland_class.Infantry - self.moved_troops > 1):
                self.moved_troops += 1

            if key_pressed[pg.K_s] and self.moved_troops > 0:
                self.moved_troops -= 1

    def attack_country(self):
        '''mouse_pressed = pg.mouse.get_pressed()
        key_pressed = pg.key.get_pressed()
        current_hov_country = None

        if mouse_pressed[2]:
            self.inland = ""
            self.outland = ""
            self.moved_troops = 0

        if self.world.current_hov:
            for country in self.controlled_countries:
                if self.world.current_hov == country:
                    current_hov_country = country.name
                    break

        if not self.outland and self.inland and current_hov_country and current_hov_country != self.inland:
            self.outland = current_hov_country
        elif not self.inland and current_hov_country and mouse_pressed[0]:
            self.inland = current_hov_country

        if self.inland and self.outland:
            outland_class = self.world.countries[self.outland]
            inland_class = self.world.countries[self.inland]

            if key_pressed[pg.K_SPACE]:
                inland_class.Infantry -= self.moved_troops
                outland_class.Infantry += self.moved_troops
                self.moved_troops = 0
                self.inland = ""
                self.outland = ""

            if key_pressed[pg.K_w] and (inland_class.Infantry - self.moved_troops > 1):
                self.moved_troops += 1

            if key_pressed[pg.K_s] and self.moved_troops > 0:
                self.moved_troops -= 1'''

    def bordering_countries(self) -> list:
        l = []
        for k, v in self.world.boders_dic.items():
            for names in self.controlled_countries:
                if k == names.name:
                    l.append(v)
        return l

    def turn(self, turn):
        self.turn_is = turn
