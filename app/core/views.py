from django.db.models import query
from rest_framework.serializers import Serializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.models import GlobalLandTemperaturesByCity
from core.serializers import GlobalLandTemperaturesByCitySerializer
from django.db.models.query import QuerySet


@api_view(['POST', 'GET'])
def get_post_global_land_temperatures_by_city(request):
    """This endpoint is used for PATCH and GET method of the API"""

    # get all
    if request.method == 'GET':

        count = int(request.GET.get("count", "0"))
        date_from = request.GET.get("date_from", "")
        date_to = request.GET.get("date_to", "")

        queryset = QuerySet(GlobalLandTemperaturesByCity)

        where_clause = {}
        if date_from:
            where_clause["dt__gte"] = date_from
        if date_to:
            where_clause["dt__lte"] = date_to

        queryset = queryset.filter(**where_clause)
        queryset = queryset.order_by("-AverageTemperature")
        if count:
            lst = queryset.values()[:count]
        else:
            lst = queryset.values()

        serializer = GlobalLandTemperaturesByCitySerializer(
            lst, many=True)
        return Response(serializer.data)

    # insert a new record for a GlobalLandTemperaturesByCity
    if request.method == 'POST':
        data = {
            'dt': request.data.get('dt'),
            'AverageTemperature': float(request.data.get('AverageTemperature')),
            'AverageTemperatureUncertainty': float(request.data.get('AverageTemperatureUncertainty')),
            'City': request.data.get('City'),
            'Country': request.data.get('Country'),
            'Latitude': request.data.get('Latitude'),
            'Longitude': request.data.get('Longitude'),
        }
        serializer = GlobalLandTemperaturesByCitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'GET'])
def get_patch_global_land_temperatures_by_city(request, city, date):
    """
        This endpoint is used for PATCH and GET method of the API
        by :
            -City
            -Date

    """
    try:
        obj = GlobalLandTemperaturesByCity.objects.get(City=city, dt=date)
    except GlobalLandTemperaturesByCity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single puppy
    if request.method == 'GET':
        serializer = GlobalLandTemperaturesByCitySerializer(obj)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = GlobalLandTemperaturesByCitySerializer(
            obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
