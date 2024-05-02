from Country import Country


class Continent:
    """
    This instance is not in use, but represents the Continents in the Risk Game. 
    Plan was to loop through all countries in the Gameplay.py file, create the continent instance, and create a list of continents, similar to 
    the list of countries in the Gameplay.py class.
    """
    def __init__(self, countries: list, name):
        self.countries = countries
        self.name = name

    def in_Continent(self, country: Country):
        """
        Checks if country is in the continent.
        """
        return self.countries.__contains__(country)
