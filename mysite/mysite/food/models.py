from django.db import models

# Create your models here.

class Item(models.Model):
    def __str__(self):            # this bit of code is written for become avilable the name of the items insted of id. in shell
        return self.item_name
    item_name = models.CharField(max_length=200)
    item_disc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default='https://as1.ftcdn.net/v2/jpg/01/39/27/58/1000_F_139275828_rbxUIXbenjmNCTHGPcuVEGu2x7mCN4J5.jpg')