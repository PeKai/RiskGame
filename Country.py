import pygame as pg


class Country:
    def __init__(self, name, coords, color):
        self.name = name
        self.coords = coords
        self.color = color
        self.Infantry = random.randint(1, 5)
        self.Cavalry = random.randint(1, 5)
        self.Artillery = random.randint(1, 5)

    def draw(self, screen, long_scan):
        pg.draw.polygon(
            screen,
            self.color,
            [(x - long_scan.x + 150, y - long_scan.y + 35) for x, y in self.coords],
        )
        pg.draw.polygon(
            screen,
            (50, 45, 30),
            [(x - long_scan.x + 150, y - long_scan.y + 35) for x, y in self.coords],
            width=1
        )
        drawn_text = pg.font.SysFont(None, 20).render(str(sum([self.Infantry, self.Cavalry, self.Artillery])), True, (0,0,0))
        text_area = drawn_text.get_rect()
        yvaried = 0
        xvaried = 0
        if self.name == "Japan":
            yvaried += 3
        if self.name == "Kamchatka":
            yvaried -= 25
        if self.name == "Alberta":
            yvaried -= 25
        if self.name == "North West territory":
            yvaried += 25
        if self.name == "Alaska":
            yvaried -= 15
        if self.name == "Central America":
            xvaried -= 15
        text_area.center = tuple(sum(values) / len(values)
                                 for values in zip(*[(x - long_scan.x + 150 + xvaried, y - long_scan.y + 35 + yvaried) for x, y in self.coords]))
        screen.blit(drawn_text, text_area)
