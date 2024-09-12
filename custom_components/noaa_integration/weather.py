import requests
from homeassistant.components.sensor import SensorEntity

API_URL = "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json"

class NOAAKpIndexSensor(SensorEntity):
    def __init__(self, name):
        self._name = name
        self._state = None
        self._data = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    def update(self):
        try:
            response = requests.get(API_URL)
            if response.status_code == 200:
                self._data = response.json()
                # Get the latest Kp index value (most recent entry)
                latest_data = self._data[-1]  # Assuming the latest data is the last entry
                self._state = latest_data.get("k_index", None)
        except Exception as e:
            self._state = None
            print(f"Error fetching NOAA Kp data: {e}")