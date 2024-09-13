# sensor.py
import requests
from homeassistant.helpers.entity import Entity

DOMAIN = 'noaa_integration'

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the MyWeather sensor."""
    add_entities([MyWeatherSensor()])

class MyWeatherSensor(Entity):
    """Representation of a MyWeather sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'My Weather Temperature'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor."""
        response = requests.get('https://api.weatherapi.com/v1/current.json?key=your_api_key&q=London')
        data = response.json()
        self._state = data['current']['temp_c']
