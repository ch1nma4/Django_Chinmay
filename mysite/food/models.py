from django.db import models

# Create your models here.


class Item(models.Model):
    Item_name = models.CharField(max_length=50)
    Item_desc = models.CharField(max_length=200)
    Item_price = models.IntegerField()