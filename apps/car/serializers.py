from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Car
        fields = '__all__'


class CarListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('preview', 'title', 'year', 'mileage', 'price')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        data = {
            'preview': repr['preview'],
            'title': repr['title'],
            'year': repr['year'],
            'mileage': repr['mileage'],
            'price': repr['price']
        }
        return data



