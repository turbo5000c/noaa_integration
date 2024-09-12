from homeassistant.helpers.discovery import load_platform

def setup(hass, config):
    # Load the sensor platform defined in sensor.py
    load_platform(hass, 'sensor', 'noaa_integration', {}, config)
    return True