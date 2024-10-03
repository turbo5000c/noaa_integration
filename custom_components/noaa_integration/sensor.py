# sensor.py
import requests
from homeassistant.helpers.entity import Entity

DOMAIN = 'noaa_integration'

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Geomagnetic Storm sensor."""
    add_entities([MyWeatherSensor(), PlanetaryKIndexSensor()])

class GeomagneticSensor(Entity):
    """Representation of a MyWeather sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Geomagnetic Storm'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor."""
        response = requests.get('https://services.swpc.noaa.gov/json/geospace/geospace_dst_1_hour.json')
        data = response.json()
        self._state = data[0].get('dst', 'Error')

class PlanetaryKIndexSensor(Entity):
    """Representation of the Planetary K-index sensor."""

    def __init__(self):
        """Initialize the Planetary K-index sensor."""
        self._state = None
        self._rating = None  # To store the rating based on the K-index

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'NOAA Planetary K-index'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'NOAA Planetary K-index Rating'

    @property
    def extra_state_attributes(self):
        """Return additional state attributes, such as the rating."""
        return {
            'rating': self._rating  # Include rating as an additional attribute
        }

    def update(self):
        """Fetch new state data for the K-index."""
        response = requests.get('https://services.swpc.noaa.gov/json/planetary_k_index_1m.json')
        if response.status_code == 200:
            data = response.json()
            self._state = data[-1].get('kp_index', 'unknown')

            # Determine the rating based on the K-index value
            if self._state != 'unknown':  # Ensure valid state
                if self._state < 2:
                    self._rating = 'low'
                elif 2 <= self._state < 5:
                    self._rating = 'moderate'
                else:
                    self._rating = 'high'
            else:
                self._rating = 'unknown'
