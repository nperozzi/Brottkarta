
class Area:
    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng

def create_areas_list():                 #TODO: The lat and lng are not exacly the center of the areas
    areas = [
        Area("Västernorrlands län", 63.2900474, 18.7166166),
        Area("Gävleborgs län", 60.621607, 16.775918),
        Area("Västra Götalands län", 58.2834894, 12.2858206),
        Area("Västerbottens län", 63.6391526, 19.6214906),
        Area("Uppsala län", 59.8585638, 17.6389267),
        Area("Stockholms län", 59.3293235, 18.0685808),
        Area("Norrbottens län", 67.1393869, 20.6939425),
        Area("Skåne län", 55.6402145, 13.0886413),
        Area("Västmanlands län", 59.6083314, 16.4915159),
        Area("Värmlands län", 60.03437, 13.694508),
        Area("Jämtlands län", 63.1702049, 14.6898762),
        Area("Örebro län", 59.2596448, 15.1801502),
        Area("Gotlands län", 57.6870345, 18.7629865),
        Area("Hallands län", 57.19448, 12.34814),
        Area("Kalmar län", 57.49484, 15.8416513),
        Area("Jönköpings län", 57.7708211, 13.8333062),
        Area("Östergötlands län", 58.706761, 15.7959176),
        Area("Södermanlands län", 59.3815818, 16.531456),
        Area("Dalarnas län", 60.14533, 16.1738399),
        Area("Kronobergs län", 56.8865238, 14.7995606),
        Area("Blekinge län", 56.3549902, 14.5875959)
    ]
    return areas
