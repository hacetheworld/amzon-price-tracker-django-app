from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Item(models.Model):
    user = models.ForeignKey(
        User, related_name="productlist", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    price = models.FloatField()
    currentPrice = models.FloatField()

    # def __str__(self):
    #     return self.user
