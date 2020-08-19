from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'cars'
urlpatterns = [
    path('cars/', CarViewCreate.as_view()),
    path('cars/<int:pk>', CarDetailView.as_view()),
]
