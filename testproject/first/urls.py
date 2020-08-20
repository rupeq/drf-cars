from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'cars'
urlpatterns = [
    path('cars/', CarView.as_view()),
    path('cars/create/', CarCreate.as_view()),
    path('cars/<int:id>/', CarRetrieveUpdateDestroy.as_view()),
]
