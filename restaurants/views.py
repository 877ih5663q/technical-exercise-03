from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from statistics import mean, pstdev


class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class Statistics(APIView):
    def get(self, request, format=None):
        longitude = float(request.GET.get('longitude', None))
        latitude = float(request.GET.get('latitude', None))
        radius = float(request.GET.get('radius', None))
        query = f'SELECT id, lng, lat, rating FROM restaurants_restaurant WHERE ST_DWithin(ST_MakePoint({longitude}, {latitude})::geography, ST_MakePoint(lng, lat)::geography, {radius})'
        within_radius = Restaurant.objects.raw(query)
        response = {\
            'count': len(within_radius),\
            'avg': mean([restaurant.rating for restaurant in within_radius]),\
            'std': pstdev([restaurant.rating for restaurant in within_radius]),
        }
        return Response(response, status=status.HTTP_201_CREATED)
