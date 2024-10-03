import requests
from homeassistant.helpers.entity import Image

DOMAIN = 'noaa_integration'

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Geoelectric Field Image entity."""
    geoelectric_image_entity = GeoelectricFieldImage()

    # Add the geoelectric image entity
    add_entities([geoelectric_image_entity])

class GeoelectricFieldImage(Image):
    """Representation of the Geoelectric Field Image."""

    def __init__(self):
        """Initialize the image entity."""
        super().__init__()
        self._image_url = None

    @property
    def name(self):
        """Return the name of the entity."""
        return 'Geoelectric Field Image'

    @property
    def image_url(self):
        """Return the URL of the latest geoelectric field image."""
        return self._image_url

    def update(self):
        """Fetch the latest geoelectric field image."""
        self._image_url = 'https://services.swpc.noaa.gov/images/animations/geoelectric/InterMagEarthScope/EmapGraphics_1m/latest.png'
