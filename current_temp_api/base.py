from abc import ABC, abstractmethod


class WeatherAPIBASE(ABC):
    def __init__(self, latitude, longitude, **kwargs):
        pass

    @abstractmethod
    def get_current_temperature(self):
        pass
