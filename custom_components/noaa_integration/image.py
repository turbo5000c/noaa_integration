import requests
from homeassistant.components.image import ImageEntity
from homeassistant.helpers.entity import DeviceInfo

DOMAIN = 'noaa_integration'

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Geoelectric Field Image entity."""
    geoelectric_image_entity = GeoelectricFieldImageEntity(hass)

    # Add the geoelectric image entity
    add_entities([geoelectric_image_entity])

class GeoelectricFieldImageEntity(ImageEntity):
    """Representation of the Geoelectric Field Image."""

    def __init__(self, hass):
        """Initialize the image entity."""
        super().__init__()
        self.hass = hass
        self._image_url = 'https://services.swpc.noaa.gov/images/animations/geoelectric/InterMagEarthScope/EmapGraphics_1m/latest.png'

    @property
    def name(self):
        """Return the name of the entity."""
        return 'Geoelectric Field Image'

    @property
    def unique_id(self):
        """Return a unique ID for this entity."""
        return 'noaa_geoelectric_image'

    @property
    def image_url(self) -> str:
        """Return the URL of the latest geoelectric field image."""
        return self._image_url

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, "noaa_geoelectric_field")},
            name="NOAA Geoelectric Field",
            manufacturer="NOAA"
        )

    def update(self):
        """Update the latest image URL."""
        self._image_url = 'https://services.swpc.noaa.gov/images/animations/geoelectric/InterMagEarthScope/EmapGraphics_1m/latest.png'
