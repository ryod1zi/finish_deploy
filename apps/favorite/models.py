from django.db import models
from apps.car.models import Car
from django.contrib.auth import get_user_model

User = get_user_model()


class Favorite(models.Model):
    owner = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, related_name='favorites', on_delete=models.CASCADE)
    # car = models.ManyToManyField(Car, related_name='favorites')

    class Meta:
        unique_together = ('owner', 'car')
