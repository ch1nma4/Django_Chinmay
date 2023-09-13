from django.db import models

# Create your models here.


class Item(models.Model):
    prod_code = models.IntegerField(default=100)
    for_user = models.CharField(
        max_length=100 ,
        default='xyz')
    Item_name = models.CharField(max_length=50)
    Item_desc = models.CharField(
        max_length=500,
        default= 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum ullam quam esse iste, ea consectetur eaque optio laboriosam  illum necessitatibus eveniet voluptas, voluptatibus sint quasi? Ut nesciunt laborum quo impedit?'
        )
    Item_price = models.IntegerField()
    Item_image = models.CharField(
        max_length=500 ,
        default="https://w7.pngwing.com/pngs/277/489/png-transparent-fast-food-eating-maps-location-placeholder-pin-icon.png"
    )

    def __str__(self):
        return self.Item_name 

