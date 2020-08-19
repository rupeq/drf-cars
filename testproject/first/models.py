from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Cars(models.Model):
    car_brand = models.CharField(max_length=64)
    number = models.IntegerField(unique=True, db_index=True)
    color = models.CharField(max_length=64)
    property = [
        (1, 'Sedan'),
        (2, 'Hatchback'),
        (3, 'Crossover'),
        (4, 'Coupe'),
    ]
    car_type = models.IntegerField(choices=property, default='Coupe')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
