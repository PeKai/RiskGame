import json
import pygame as pg
import random
from shapely import Point, Polygon

from Continent import Continent
from Country import Country
from Waterlines import Waterlines


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

    def __init__(self):
        self.geo_data = None
        self.json_map()
        self.countries = self.create_countries()
        self.long_scan = pg.Vector2(1000, 50)
        self.waterlines = self.create_waterlines()
        self.waterlines_csv = None
        self.current_hov = None

    def json_map(self):
        with open("./polygon_xy_flat.json", "r") as f:
            self.geo_data = json.load(f)
        with open("./polygon_xy_flat_wl.json", "r") as f:
            self.waterlines_csv = json.load(f)

    def create_waterlines(self):
        wl = {}
        for name, coords in self.waterlines_csv.items():
            xy_coords = []
            for coord in coords:
                x = (self.M_WIDTH / 360) * (180 + coord[0])
                y = (self.M_HEIGHT / 180) * (90 - coord[1])
                xy_coords.append(pg.Vector2(x, y))
            wl[name] = Waterlines(name, xy_coords, (30, 25, 10))
        return wl

    def create_countries(self):
        countries = {}
        for name, coords in self.geo_data.items():
            xy_coords = []
            for coord in coords:
                x = (self.M_WIDTH / 360) * (180 + coord[0])
                y = (self.M_HEIGHT / 180) * (90 - coord[1])
                xy_coords.append(pg.Vector2(x, y))
            countries[name] = Country(name, xy_coords, (random.randrange(60, 250),
                                                        random.randrange(55, 245),
                                                        random.randrange(35, 220)))
        return countries

    def draw(self, screen: pg.Surface):
        screen.fill((194, 178, 128))
        for country in self.countries.values():
            country.draw(screen, self.long_scan)
        for waterline in self.waterlines.values():
            waterline.draw(screen, self.long_scan)
        hover_surface = pg.Surface((500, 120), pg.SRCALPHA)
        hover_surface.fill((70, 65, 50, 100))
        screen.blit(hover_surface, (390, 650))
        mouse_pos = pg.mouse.get_pos()
        self.current_hov = None
        for country in self.countries.values():
            if Point(pg.Vector2(self.long_scan.x + mouse_pos[0] - 150, self.long_scan.y + mouse_pos[1] - 35))\
                    .within(Polygon(country.coords)):
                self.current_hov = country
        if self.current_hov is not None:
            drawn_text = pg.font.SysFont(None, 20).render(str(self.current_hov.name), True, (230, 225, 210))
            text_area = drawn_text.get_rect()
            text_area.topleft = (410, 670)
            screen.blit(drawn_text, text_area)
            drawn_text = pg.font.SysFont(None, 20).render(("Infantry: " + str(self.current_hov.Infantry)),
                                                          True, (30, 25, 10))
            text_area = drawn_text.get_rect()
            text_area.topleft = (410, 690)
            screen.blit(drawn_text, text_area)
            drawn_text = pg.font.SysFont(None, 20).render(("Cavalry: " + str(self.current_hov.Cavalry)), True, (30, 25, 10))
            text_area = drawn_text.get_rect()
            text_area.topleft = (410, 710)
            screen.blit(drawn_text, text_area)
            drawn_text = pg.font.SysFont(None, 20).render(("Artillery: " + str(self.current_hov.Artillery)),
                                                          True, (30, 25, 10))
            text_area = drawn_text.get_rect()
            text_area.topleft = (410, 730)
            screen.blit(drawn_text, text_area)

    def update(self):
        self.update_camera_long()
        self.update_zoom()

    def update_camera_long(self):
        button = pg.key.get_pressed()

        if self.long_scan.x < 300:
            if button[pg.K_d]:
                self.long_scan.x += 200
        elif self.long_scan.x > 850:
            if button[pg.K_a]:
                self.long_scan.x -= 200
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


