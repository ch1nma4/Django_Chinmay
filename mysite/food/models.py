from django.db import models

# Create your models here.


class Item(models.Model):
    Item_name = models.CharField(max_length=50)
    Item_desc = models.CharField(max_length=200)
    Item_price = models.IntegerField()
    Item_image = models.CharField(
        max_length=500 ,
        default="https://w7.pngwing.com/pngs/277/489/png-transparent-fast-food-eating-maps-location-placeholder-pin-icon.png"
    )

    def __str__(self):
        return self.Item_name 

