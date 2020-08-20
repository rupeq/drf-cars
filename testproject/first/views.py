from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import ValidationError

from .serializers import *
from .models import Cars
from .permissions import IsOwnerOrReadOnly

class CarPagination(LimitOffsetPagination):
    default_size = 10
    max_size = 100

class CarView(ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', )
    search_fields = ('car_brand', 'color')
    pagination_class = CarPagination

class CarCreate(CreateAPIView):
    serializer_class = CarSerializer

    def create(self, request, *args, **kwargs):
        try:
            number = request.data.get('number')
            if number is not None and not (number.isdigit or number.isalpha):
                raise ValidationError({'number':'Number must consists of letters and numbers'})
        except ValueError:
            raise ValidationError({'number':'A valid number is required'})
        return super().create(request, *args, **kwargs)

class CarRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Cars.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminUser, IsOwnerOrReadOnly)

    def delete(self, request, *args, **kwargs):
        car_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('car_data_{}'.format(car_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            car = response.data
            from django.core.cache import cache
            cache.set('car_data{}'.format(car['id']),{
                'car_brand': car['car_brand'],
                'number': car['number'],
                'color': car['color'],
                'car_type': car['car_type'],
            })
        return response