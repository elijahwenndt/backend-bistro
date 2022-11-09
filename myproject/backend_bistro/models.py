from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Cuisine(models.Model):
    types = models.CharField(max_length=50)

    def __str__(self):
        return self.types
# Create your models here.

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(null=True, blank=True)
    spice_level = models.IntegerField(null=True, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    cuisine_id = models.ForeignKey(Cuisine, on_delete=models.CASCADE)

    def __str__(self):
        return self.title