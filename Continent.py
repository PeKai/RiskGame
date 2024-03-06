from src.Country import Country


class Continent:

    def __init__(self, countries: list, name):
        self.countries = countries
        self.name = name

    def in_Continent(self, country: Country):
        return self.countries.__contains__(country)
