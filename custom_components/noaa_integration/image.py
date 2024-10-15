import aiohttp
from homeassistant.components.image import ImageEntity
from homeassistant.helpers.entity import DeviceInfo
from datetime import timedelta, datetime

DOMAIN = 'noaa_integration'
SCAN_INTERVAL = timedelta(minutes=5)  # Update the image every 5 minutes

BASE_IMAGE_URL = 'https://services.swpc.noaa.gov/images/animations/geoelectric/InterMagEarthScope/EmapGraphics_1m/latest.png'
AURORA_URL = 'https://services.swpc.noaa.gov/experimental/images/aurora_dashboard/tonights_static_viewline_forecast.png'


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Geoelectric Field Image entity."""
    geoelectric_image_entity = GeoelectricFieldImageEntity(hass)
    aurora_image_entity = AuroraForecastImageEntity(hass)

    # Add both image entities
    add_entities([geoelectric_image_entity, aurora_image_entity])

class GeoelectricFieldImageEntity(ImageEntity):
    """Representation of the Geoelectric Field Image."""

    def __init__(self, hass):
        """Initialize the image entity."""
        super().__init__(hass)
        self.hass = hass
        self._image_url = self.get_cache_busted_url()

    @property
    def name(self):
        """Return the name of the entity."""
        return 'Geoelectric Field Image'

    @property
    def entity_picture(self):
        """Return the URL of the latest geoelectric field image."""
        return self._image_url

    @property
    def unique_id(self):
        """Return a unique ID for this entity."""
        return 'noaa_geoelectric_image'

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, "noaa_geoelectric_field")},
            name="NOAA Geoelectric Field",
            manufacturer="NOAA"
        )

    def get_cache_busted_url(self):
        """Add a timestamp to the URL to prevent caching."""
        timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f"{BASE_IMAGE_URL}?t={timestamp}"

    async def async_update(self):
        """Fetch and update the latest image content asynchronously."""
        try:
            # Fetch the image and update with cache busting
            self._image_url = self.get_cache_busted_url()
            self.async_write_ha_state()  # Notify Home Assistant of the state change
        except aiohttp.ClientError as e:
            print(f"Error during image update: {e}")

    async def async_image(self) -> bytes:
        """Return the bytes of the latest image."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self._image_url) as response:
                    if response.status == 200:
                        return await response.read()
        except aiohttp.ClientError as e:
            print(f"Error fetching image bytes: {e}")
        return b""


class GeoelectricFieldImageEntity(ImageEntity):
    """Representation of the Geoelectric Field Image."""

    def __init__(self, hass):
        """Initialize the image entity."""
        super().__init__(hass)
        self.hass = hass
        self._image_url = self.get_cache_busted_url()

    @property
    def name(self):
        """Return the name of the entity."""
        return 'Geoelectric Field Image'

    @property
    def entity_picture(self):
        """Return the URL of the latest geoelectric field image."""
        return self._image_url

    @property
    def unique_id(self):
        """Return a unique ID for this entity."""
        return 'noaa_geoelectric_image'

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, "noaa_geoelectric_field")},
            name="NOAA Geoelectric Field",
            manufacturer="NOAA"
        )

    def get_cache_busted_url(self):
        """Add a timestamp to the URL to prevent caching."""
        timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f"{BASE_IMAGE_URL}?t={timestamp}"

    async def async_update(self):
        """Fetch and update the latest image content asynchronously."""
        try:
            # Fetch the image and update with cache busting
            self._image_url = self.get_cache_busted_url()
            self.async_write_ha_state()  # Notify Home Assistant of the state change
        except aiohttp.ClientError as e:
            print(f"Error during image update: {e}")

    async def async_image(self) -> bytes:
        """Return the bytes of the latest image."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self._image_url) as response:
                    if response.status == 200:
                        return await response.read()
        except aiohttp.ClientError as e:
            print(f"Error fetching image bytes: {e}")
        return b""


class AuroraForecastImageEntity(ImageEntity):
    """Representation of the aurora Field Image."""

    def __init__(self, hass):
        """Initialize the image entity."""
        super().__init__(hass)
        self.hass = hass
        self._image_url = self.get_cache_busted_url()

    @property
    def name(self):
        """Return the name of the entity."""
        return 'Aurora Forecast Image'

    @property
    def entity_picture(self):
        """Return the URL of the latest aurora forecast image."""
        return self._image_url

    @property
    def unique_id(self):
        """Return a unique ID for this entity."""
        return 'noaa_aurora_image'

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, "noaa_aurora_field")},
            name="NOAA Aurora Forecast",
            manufacturer="NOAA"
        )

    def get_cache_busted_url(self):
        """Add a timestamp to the URL to prevent caching."""
        timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f"{AURORA_URL}?t={timestamp}"

    async def async_update(self):
        """Fetch and update the latest image content asynchronously."""
        try:
            # Fetch the image and update with cache busting
            self._image_url = self.get_cache_busted_url()
            self.async_write_ha_state()  # Notify Home Assistant of the state change
        except aiohttp.ClientError as e:
            print(f"Error during image update: {e}")

    async def async_image(self) -> bytes:
        """Return the bytes of the latest image."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self._image_url) as response:
                    if response.status == 200:
                        return await response.read()
        except aiohttp.ClientError as e:
            print(f"Error fetching image bytes: {e}")
        return b""
