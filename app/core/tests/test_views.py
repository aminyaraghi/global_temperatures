import json
from typing import KeysView
from django.http import response
from rest_framework import status
from django.test import TestCase, Client, testcases
from django.urls import reverse
from rest_framework.serializers import Serializer
from core.models import GlobalLandTemperaturesByCity
from core.serializers import GlobalLandTemperaturesByCitySerializer
from datetime import datetime
from django.db.models import Max

# Initialize the APIClient app
client = Client()
URL_GET_POST = 'get_post_global_land_temperatures_by_city'
URL_GET_PATCH = 'get_patch_global_land_temperatures_by_city'


class GetAllPuppiesTest(TestCase):

    def setUp(self) -> None:
        GlobalLandTemperaturesByCity.objects.create(
            dt=datetime.strptime("1743-11-01", '%Y-%m-%d'),
            AverageTemperature=7.068,
            AverageTemperatureUncertainty=2.737,
            City="Isfahan",
            Country="Iran",
            Latitude="32.65N",
            Longitude="51.66E"
        )
        GlobalLandTemperaturesByCity.objects.create(
            dt=datetime.strptime("1743-10-01", '%Y-%m-%d'),
            AverageTemperature=6.068,
            AverageTemperatureUncertainty=1.737,
            City="Isfahan",
            Country="Iran",
            Latitude="32.65N",
            Longitude="51.66E"
        )
        GlobalLandTemperaturesByCity.objects.create(
            dt=datetime.strptime("1743-11-01", '%Y-%m-%d'),
            AverageTemperature=4.65,
            AverageTemperatureUncertainty=0.455,
            City="Tehran",
            Country="Iran",
            Latitude="31.65N",
            Longitude="50.66E"
        )

    def test_get_all_api(self):
        # get api client
        response = client.get(reverse(URL_GET_POST))
        # get data from db
        lst = GlobalLandTemperaturesByCity.objects.all()
        serializer = GlobalLandTemperaturesByCitySerializer(lst, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_highest_average_temperature_api(self):
        response = client.get(
            reverse(URL_GET_POST), {'count': 1}
        )

        obj = GlobalLandTemperaturesByCity.objects.order_by(
            "-AverageTemperature").all()[0]
        serializer = GlobalLandTemperaturesByCitySerializer([obj], many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_api(self):

        payload = {
            "dt": "2021-10-01",
            "AverageTemperature": 4.65,
            "AverageTemperatureUncertainty": 0.455,
            "City": "Tehran",
            "Country": "Iran",
            "Latitude": "31.65N",
            "Longitude": "50.66E"
        }
        response = client.post(
            reverse(URL_GET_POST),
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_valid_update_api(self):
        payload = {
            "AverageTemperature": 10.32,
            "AverageTemperatureUncertainty": 5.455,
        }
        response = client.patch(
            reverse(URL_GET_PATCH,
                    kwargs={'city': "Isfahan", "date": "1743-10-01"}),
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
