from homeassistant.helpers.discovery import load_platform

def setup(hass, config):
    load_platform(hass, 'sensor', 'noaa_integration', {}, config)
    return True