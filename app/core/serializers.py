from rest_framework import serializers
from core.models import GlobalLandTemperaturesByCity


class GlobalLandTemperaturesByCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalLandTemperaturesByCity
        fields = ('id', 'dt', 'AverageTemperature', 'AverageTemperatureUncertainty',
                  'City', 'Country', 'Latitude', 'Longitude')
