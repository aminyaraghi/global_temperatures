from django.test import TestCase
from datetime import datetime

from core import models


class ModelTests(TestCase):
    def test_globalLandTemperaturesByCity_str(self):
        """test the GlobalLandTemperaturesByCity string representation"""
        dt = datetime.strptime("1743-11-01", '%Y-%m-%d')
        AverageTemperature = 6.068
        AverageTemperatureUncertainty = 1.737
        City = "Isfahan"
        Country = "Iran"
        Latitude = "32.65N"
        Longitude = "51.66E"

        obj = models.GlobalLandTemperaturesByCity.objects.create(
            dt=dt,
            AverageTemperature=AverageTemperature,
            AverageTemperatureUncertainty=AverageTemperatureUncertainty,
            City=City,
            Country=Country,
            Latitude=Latitude,
            Longitude=Longitude
        )

        expected_str = f"dt={str(dt)}, AverageTemperature={AverageTemperature}, \
            AverageTemperatureUncertainty={AverageTemperatureUncertainty}, City={City}, \
            Country={Country}, Latitude={Latitude}, Longitude={Longitude}"

        self.assertEqual(str(obj), expected_str)
