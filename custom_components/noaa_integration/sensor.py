import requests
from homeassistant.helpers.entity import Entity
from datetime import timedelta, datetime

DOMAIN = 'noaa_integration'
SCAN_INTERVAL = timedelta(minutes=5)  # Update the image every 5 minutes

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Geomagnetic Storm sensor."""
    # Instantiate the processor for K-index and Dst interpretation
    planetary_k_index_rating = PlanetaryKIndexSensorRating()
    geomagnetic_interpretation = GeomagneticSensorInterpretation()

    # Pass the processors to the sensors that will use them
    add_entities([GeomagneticSensor(geomagnetic_interpretation), PlanetaryKIndexSensor(planetary_k_index_rating), planetary_k_index_rating, geomagnetic_interpretation])

class GeomagneticSensor(Entity):
    """Representation of the Geomagnetic Storm sensor."""

    def __init__(self, interpreter):
        """Initialize the sensor."""
        self._state = None
        self.interpreter = interpreter  # Store the interpreter

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
        if response.status_code == 200:
            data = response.json()
            self._state = data[0].get('dst', 'Error')
            self.interpreter.process_geomagnetic_data(self._state)

class GeomagneticSensorInterpretation(Entity):
    """Representation of the Geomagnetic Storm Interpretation sensor."""

    def __init__(self):
        """Initialize the interpretation sensor."""
        self._state = None
        self._interpretation = None

    @property
    def state(self):
        """Return the interpretation of the geomagnetic storm."""
        return self._interpretation

    @property
    def name(self):
        """Return the name of the interpretation sensor."""
        return 'Geomagnetic Storm Interpretation'

    def process_geomagnetic_data(self, dst_value):
        """Process the Dst value and determine the interpretation."""
        self._state = dst_value
        #print(f"Processed Dst value: {self._state}")

        # Interpretation based on the Dst value
        if isinstance(self._state, (int, float)):  # Ensure it's a valid numeric value
            if self._state > -20:
                self._interpretation = 'No Storm (Quiet conditions)'
            elif -20 > self._state >= -50:
                self._interpretation = 'Minor Storm'
            elif -50 > self._state >= -100:
                self._interpretation = 'Moderate Storm'
            elif -100 > self._state >= -200:
                self._interpretation = 'Strong Storm'
            else:
                self._interpretation = 'Severe Storm'
        else:
            self._interpretation = 'Error: Invalid Dst value'

class PlanetaryKIndexSensor(Entity):
    """Representation of the Planetary K-index sensor."""

    def __init__(self, processor):
        """Initialize the Planetary K-index sensor and pass in the processor."""
        self._state = None
        self.processor = processor  # Store the processor

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Planetary K-index'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the K-index."""
        response = requests.get('https://services.swpc.noaa.gov/json/planetary_k_index_1m.json')
        if response.status_code == 200:
            data = response.json()
            self._state = data[-1].get('kp_index', 'unknown')
            # Call the processor to handle the solar flux value
            self.processor.process_solar_flux(self._state)

class PlanetaryKIndexSensorRating(Entity):
    """Representation of the Planetary K-index Rating sensor."""

    def __init__(self):
        """Initialize the Planetary K-index Rating."""
        self._state = None
        self._rating = None

    @property
    def state(self):
        """Return the state of the sensor rating."""
        return self._rating

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Planetary K-index Rating'

    def process_solar_flux(self, solar_flux_value):
        """Process the Solar Flux value."""
        self._state = solar_flux_value
        #print(f"Processed solar flux value: {self._state}")

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
