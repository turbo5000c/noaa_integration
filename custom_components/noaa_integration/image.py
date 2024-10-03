import requests
from homeassistant.helpers.entity import Entity

DOMAIN = 'noaa_integration'

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Geoelectric Field Image sensor."""
    geoelectric_image_sensor = GeoelectricFieldImageSensor()

    # Add the geoelectric image sensor entity
    add_entities([geoelectric_image_sensor])

class GeoelectricFieldImageSensor(Entity):
    """Representation of the Geoelectric Field Image Sensor."""

    def __init__(self):
        """Initialize the Geoelectric Field Image sensor."""
        self._image_url = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Geoelectric Field Image'

    @property
    def entity_picture(self):
        """Return the URL of the latest image."""
        return self._image_url

    def update(self):
        """Fetch the latest geoelectric field image."""
        image_url = 'https://services.swpc.noaa.gov/images/animations/geoelectric/InterMagEarthScope/EmapGraphics_1m/latest.png'
        response = requests.get(image_url)
        if response.status_code == 200:
            self._image_url = image_url
