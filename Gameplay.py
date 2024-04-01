import pygame
import pygame as pg
import time
import sys

from src.Map import Map
from src.Player import Player


class Gameplay:
    def __init__(self, screen):
        self.recttb = None
        self.hoveredtb = None
        self.tb = None
        self.rectmb = None
        self.hoveredmb = None
        self.finish_phase_image = None
        self.mbutton = None
        self.current_phase_rect = None
        self.current_phase_image = None
        self.modes = ["pu", "mu", "au"]
        self.screen = screen
        self.is_play = True
        self.mid = 0
        self.mode = self.modes[self.mid]
        self.map = Map(self.screen, self)
        self.player = Player(self.map, (255, 0, 0))
        self.AIplayer = Player(self.map, (0, 255, 0))
        self.turnid = 0
        self.turn = None

    def run(self):
        while self.is_play:
            time.sleep(0.005)
            self.events()
            self.update()
            self.draw()
            pg.display.update()

    def update(self):
        self.map.update()
        if self.turn == self.player:
            self.player.update(self.mode)
        elif self.turn == self.AIplayer:
            self.AIplayer.update(self.mode)

        self.hoveredmb = False
        if self.rectmb is not None and self.rectmb.collidepoint(pg.mouse.get_pos()):
            self.hoveredmb = True
        else:
            pass

        self.hoveredtb = False
        if self.recttb is not None and self.recttb.collidepoint(pg.mouse.get_pos()):
            self.hoveredtb = True
        else:
            pass

    def events(self):
        for e in pg.event.get():
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    self.is_play = False
            if e.type == pg.QUIT:
                self.is_play = False

    def draw(self):
        self.map.draw(self.screen)
        self.phase_gui()
        self.player_turn_gui()

    def phase_gui(self):

        self.mbutton = pg.Surface((50, 20), pg.SRCALPHA)
        self.mbutton.fill((0, 0, 0, 0))
        self.rectmb = self.mbutton.get_rect(topleft=(504, 667))
        pygame.draw.rect(self.mbutton, (255, 0, 0, 100), self.mbutton.get_rect(), border_radius=7)
        screen.blit(self.mbutton, (504, 667))

        if self.hoveredmb:
            pygame.draw.rect(self.mbutton, (0, 0, 0, 100), self.mbutton.get_rect(), border_radius=7)
            screen.blit(self.mbutton, (504, 667))
        else:
            pygame.draw.rect(self.mbutton, (255, 0, 0, 100), self.mbutton.get_rect(),
                             border_radius=7)
            screen.blit(self.mbutton, (504, 667))

        if self.hoveredmb and pygame.mouse.get_pressed()[0]:
            self.turn.inland = ""
            self.turn.outland = ""
            self.turn.moved_troops = 0
            self.mid += 1
            if self.mid >= len(self.modes):
                self.mid = 0

        drawn_text = pg.font.SysFont(None, 20).render("Phase", True, (230, 225, 210))
        text_area = drawn_text.get_rect()
        text_area.topleft = (510, 670)
        screen.blit(drawn_text, text_area)

        self.mode = self.modes[self.mid]
        if self.mode == "pu":
            drawn_text = pg.font.SysFont(None, 20).render("Placing", True, (130, 225, 110))
            text_area = drawn_text.get_rect()
            text_area.topleft = (510, 690)
            screen.blit(drawn_text, text_area)

            drawn_text = pg.font.SysFont(None, 20).render("Move", True, (230, 125, 110))
            text_area = drawn_text.get_rect()
            text_area.topleft = (510, 710)
            screen.blit(drawn_text, text_area)

            drawn_text = pg.font.SysFont(None, 20).render("Attack", True, (230, 125, 110))
            text_area = drawn_text.get_rect()
            text_area.topleft = (510, 730)
            screen.blit(drawn_text, text_area)
        elif self.mode == "mu":
            drawn_text = pg.font.SysFont(None, 20).render("Move", True, (130, 225, 110))
            text_area = drawn_text.get_rect()
            text_area.topleft = (510, 710)
            screen.blit(drawn_text, text_area)

            drawn_text = pg.font.SysFont(None, 20).render("Placing", True, (230, 125, 110))
            text_area = drawn_text.get_rect()
            text_area.topleft = (510, 690)
            screen.blit(drawn_text, text_area)

            drawn_text = pg.font.SysFont(None, 20).render("Attack", True, (230, 125, 110))
            text_area = drawn_text.get_rect()
            text_area.topleft = (510, 730)
            screen.blit(drawn_text, text_area)
        elif self.mode == "au":
            drawn_text = pg.font.SysFont(None, 20).render("Move", True, (230, 125, 110))
            text_area = drawn_text.get_rect()
            text_area.topleft = (510, 710)
            screen.blit(drawn_text, text_area)

            drawn_text = pg.font.SysFont(None, 20).render("Placing", True, (230, 125, 110))
            text_area = drawn_text.get_rect()
            text_area.topleft = (510, 690)
            screen.blit(drawn_text, text_area)

            drawn_text = pg.font.SysFont(None, 20).render("Attack", True, (130, 225, 110))
            text_area = drawn_text.get_rect()
            text_area.topleft = (510, 730)
            screen.blit(drawn_text, text_area)

    def player_turn_gui(self):

        self.tb = pg.Surface((50, 20), pg.SRCALPHA)
        self.tb.fill((0, 0, 0, 0))
        self.recttb = self.tb.get_rect(topleft=(654, 667))
        pygame.draw.rect(self.tb, (255, 0, 0, 100), self.tb.get_rect(),
                         border_radius=7)
        screen.blit(self.tb, (654, 667))

        if self.hoveredtb:
            pygame.draw.rect(self.tb, (0, 0, 0, 100), self.tb.get_rect(),
                             border_radius=7)
            screen.blit(self.tb, (654, 667))
        else:
            pygame.draw.rect(self.tb, (255, 0, 0, 100), self.tb.get_rect(),
                             border_radius=7)
            screen.blit(self.tb, (654, 667))

        drawn_text = pg.font.SysFont(None, 20).render("PTurn", True, (230, 230, 230))
        text_area = drawn_text.get_rect()
        text_area.topleft = (660, 670)
        screen.blit(drawn_text, text_area)

        drawn_text_player = pg.font.SysFont(None, 20).render("Player", True, (230, 230, 230))
        text_area_player = drawn_text.get_rect()
        text_area_player.topleft = (660, 690)
        screen.blit(drawn_text_player, text_area_player)

        drawn_text_AIPlayer = pg.font.SysFont(None, 20).render("AIPlayer", True, (230, 230, 230))
        text_area_AIPlayer = drawn_text.get_rect()
        text_area_AIPlayer.topleft = (660, 710)
        screen.blit(drawn_text_AIPlayer, text_area_AIPlayer)

        if self.hoveredtb and pygame.mouse.get_pressed()[0]:
            time.sleep(0.1)
            self.turnid += 1
            if self.turnid % 2:
                self.turn = self.AIplayer
                drawn_text_player = pg.font.SysFont(None, 20).render("Player", True, (230, 230, 230))
                text_area_player = drawn_text.get_rect()
                text_area_player.topleft = (660, 690)
                screen.blit(drawn_text_player, text_area_player)

                drawn_text_AIPlayer = pg.font.SysFont('Arial', 20).render("AIPlayer", True, (130, 225, 110))
                text_area_AIPlayer = drawn_text.get_rect()
                text_area_AIPlayer.topleft = (660, 710)
                screen.blit(drawn_text_AIPlayer, text_area_AIPlayer)
            else:
                self.turn = self.player
                drawn_text_player = pg.font.SysFont('Arial', 20).render("Player", True, (130, 225, 110))
                text_area_player = drawn_text.get_rect()
                text_area_player.topleft = (660, 690)
                screen.blit(drawn_text_player, text_area_player)

                drawn_text_AIPlayer = pg.font.SysFont(None, 20).render("AIPlayer", True, (230, 230, 230))
                text_area_AIPlayer = drawn_text.get_rect()
                text_area_AIPlayer.topleft = (660, 710)
                screen.blit(drawn_text_AIPlayer, text_area_AIPlayer)


if __name__ == "__main__":
    pg.init()

    screen = pg.display.set_mode(pg.Vector2(1280, 720), pg.FULLSCREEN)

    game = Gameplay(screen)
    game.run()

    pg.quit()
    sys.exit()
