import json
import pygame as pg
import random

from Continent import Continent
from Country import Country


class Map:
    M_WIDTH = 2.05 * 4000 * 0.25
    M_HEIGHT = 1.0 * 4000 * 0.25
    territory = {'West Europe': ['France.', 'Spain.', 'Portugal.'],
                 'Great Britain': ['United Kingdom.', 'Ireland.'],
                 'Iceland': ['Iceland.'],
                 'Southern Europe': ['Italy.', 'Switzerland.', 'Austria.', 'Greece.', 'Albania.',
                                     'North Macedonia.', 'Kosovo.', 'Montenegro.', 'Bosnia and Herzegovina.',
                                     'Croatia.', 'Serbia.', 'Slovenia.', 'Hungary.', 'Romania.', 'Bulgaria.'],
                 'Northern Europe': ['Germany.', 'Netherlands.', 'Belgium.', 'Denmark.', 'Poland.', 'Slovakia.', 'Czechia.'],
                 'Ukraine': ['Ukraine.', 'Moldova.', 'Belarus.', 'Lithuania.', 'Latvia.', 'Estonia.', 'Russia.'],
                 'Scandinavia': ['Sweden.', 'Norway.', 'Finland.'],
                 'Greenland': ['Greenland.']}
    continents = {'Europe':  ['West Europe', 'Great Britain',
                  'Southern Europe', 'North Europe', 'Scandinavia', 'Iceland']}
    random_colors = [c for c in range(0, 250, 1)]
    continents_class_europe = []
    continents_class_europe1 = []

    def __init__(self):
        self.geo_data = None
        self.json_map()
        self.countries = self.create_countries()
        self.long_scan = pg.Vector2(1000, 50)

    def json_map(self):
        with open("./polygon_xy_flat.json", "r") as f:
            self.geo_data = json.load(f)

    def create_countries(self):
        countries = {}
        for name, coords in self.geo_data.items():
            xy_coords = []
            for coord in coords:
                x = (self.M_WIDTH / 360) * (180 + coord[0])
                y = (self.M_HEIGHT / 180) * (90 - coord[1])
                xy_coords.append(pg.Vector2(x, y))
            if name in self.territory['West Europe']:
                countries[name] = Country(name, xy_coords, (255, 255, self.random_colors[0]))
                self.continents_class_europe.append(name)
            elif name in self.territory['Great Britain']:
                countries[name] = Country(name, xy_coords, (255, 255, self.random_colors[1]))
                self.continents_class_europe1.append(name)
            elif name in self.territory['Iceland']:
                countries[name] = Country(name, xy_coords, (255, 255, self.random_colors[2]))
            elif name in self.territory['Southern Europe']:
                countries[name] = Country(name, xy_coords, (255, self.random_colors[0], 255))
            elif name in self.territory['Ukraine']:
                countries[name] = Country(name, xy_coords, (255, self.random_colors[1], 255))
            elif name in self.territory['Scandinavia']:
                countries[name] = Country(name, xy_coords, (255, self.random_colors[2], 255))
            elif name in self.territory['Northern Europe']:
                countries[name] = Country(name, xy_coords, (self.random_colors[0], 255, 255))
            elif name in self.territory['Greenland']:
                countries[name] = Country(name, xy_coords, (self.random_colors[1], 255, 255))
            elif name == 'Antarctica':
                pass
            else:
                countries[name] = Country(name, xy_coords, (random.randrange(0,250),
                                                            random.randrange(0,250),
                                                            random.randrange(0,250)))
        return countries

    def draw(self, screen: pg.Surface):
        screen.fill((14,135,204))
        for country in self.countries.values():
            country.draw(screen, self.long_scan)

    def update(self):
        self.update_camera_long()
        self.update_zoom()

    def update_camera_long(self):
        button = pg.key.get_pressed()

        if self.long_scan.x < 300:
            if button[pg.K_d]:
                self.long_scan.x += 200
            if button[pg.K_w]:
                self.long_scan.y -= 200
            if button[pg.K_s]:
                self.long_scan.y += 200
        elif self.long_scan.x > 600:
            if button[pg.K_a]:
                self.long_scan.x -= 200
            if button[pg.K_w]:
                self.long_scan.y -= 200
            if button[pg.K_s]:
                self.long_scan.y += 200
        else:
            if button[pg.K_a]:
                self.long_scan.x -= 200
            elif button[pg.K_d]:
                self.long_scan.x += 200

    def update_zoom(self):
        button = pg.key.get_pressed()
        if button[pg.K_UP]:
            self.M_WIDTH *= 0.2
            self.M_HEIGHT *= 0.2
            self.create_countries()


