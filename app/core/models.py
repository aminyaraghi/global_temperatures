from django.db import models


class GlobalLandTemperaturesByCity(models.Model):
    """
    Model for Global Land Temperatures By City
    """
    dt = models.DateField()
    AverageTemperature = models.FloatField(null=True)
    AverageTemperatureUncertainty = models.FloatField(null=True)
    City = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Latitude = models.CharField(max_length=100)
    Longitude = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"dt={str(self.dt)}, AverageTemperature={self.AverageTemperature}, \
            AverageTemperatureUncertainty={self.AverageTemperatureUncertainty}, City={self.City}, \
            Country={self.Country}, Latitude={self.Latitude}, Longitude={self.Longitude}"

    class Meta:
        db_table = 'Global_Land_Temperatures_By_City'
        managed = True
        verbose_name = 'GlobalLandTemperaturesByCity'
        verbose_name_plural = 'GlobalLandTemperaturesByCitys'
