import pygame as pg
import time
import sys

from src.Map import Map


class Gameplay:
    def __init__(self, screen):
        self.screen = screen
        self.is_play = True
        self.map = Map()

    def run(self):
        while self.is_play:
            time.sleep(0.01)
            self.events()
            self.update()
            self.draw()
            pg.display.update()

    def update(self):
        self.map.update()

    def events(self):
        for e in pg.event.get():
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    self.is_play = False
            if e.type == pg.QUIT:
                self.is_play = False

    def draw(self):
        self.map.draw(self.screen)


if __name__ == "__main__":
    pg.init()

    screen = pg.display.set_mode(pg.Vector2(1280, 720), pg.FULLSCREEN)

    game = Gameplay(screen)
    game.run()

    pg.quit()
    sys.exit()
