from homeassistant.components.sensor import SensorEntity

class NOAAKpIndexSensor(SensorEntity):
    def __init__(self, name):
        self._name = name
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    def update(self):
        # Set a static value for testing purposes
        self._state = 5

def setup_platform(hass, config, add_entities, discovery_info=None):
    add_entities([NOAAKpIndexSensor("NOAA Kp Index")])
