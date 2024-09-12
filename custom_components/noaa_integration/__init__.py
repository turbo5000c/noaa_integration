from homeassistant.helpers.discovery import load_platform

def setup(hass, config):
    # No need to load the sensor via the platform
    return True