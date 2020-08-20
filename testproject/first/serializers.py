from rest_framework import serializers
from .models import Cars

class CarSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Cars
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data