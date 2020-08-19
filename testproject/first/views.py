from django.shortcuts import render
from .serializers import *
from .models import Cars
from rest_framework.generics import *
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class CarDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CreateSerializer
    queryset = Cars.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
    authentication_classes = (TokenAuthentication, )

class CarViewCreate(ListCreateAPIView):
    permission_classes = (IsAdminUser, )
    serializer_class = ListSerializer
    queryset = Cars.objects.all()