# __init__.py
import logging

from homeassistant.helpers import discovery

_LOGGER = logging.getLogger(__name__)

DOMAIN = "noaa_integration"

def setup(hass, config):
    """Set up the MyWeather component."""
    _LOGGER.info("Setting up MyWeather integration")

    # Load the platform for sensor
    discovery.load_platform(hass, 'sensor', DOMAIN, {}, config)

    return True
