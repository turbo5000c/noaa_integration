import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from homeassistant.helpers.entity import Entity
from datetime import datetime

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
        self._latest_image_time = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Geoelectric Field Image'

    @property
    def state(self):
        """Return the URL of the latest image."""
        return self._image_url

    def update(self):
        """Fetch the latest geoelectric field image."""
        base_url = 'https://services.swpc.noaa.gov/images/animations/geoelectric/InterMagEarthScope/EmapGraphics_1m/'
        
        # Dynamically form the latest image URL using the current date/time
        now = datetime.utcnow()
        latest_timestamp = now.strftime('%Y%m%dT%H%M%S')

        # Try fetching the image in reverse by checking the latest timestamps
        for i in range(5):
            image_url = f"{base_url}{latest_timestamp}-7-emap-empirical-EMTF-2022.12-v2022.12.png"
            response = requests.get(image_url)
            if response.status_code == 200:
                self._image_url = image_url
                self._latest_image_time = latest_timestamp
                self.show_image(image_url)
                break
            # Decrement the timestamp in case the exact match isn't available
            latest_timestamp = (now.replace(second=now.second - (i + 1))).strftime('%Y%m%dT%H%M%S')

    def show_image(self, url):
        """Display the image."""
        response = requests.get(url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            plt.imshow(img)
            plt.axis('off')  # Hide axes for image
            plt.show()
        else:
            print(f"Failed to retrieve image: {response.status_code}")
