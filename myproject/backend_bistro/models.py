from django.db import models

class RestaurantName(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


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
    items = models.ManyToManyField(RestaurantName)

    def __str__(self):
        return self.title
        
    def json(self):
        location = [i.name for i in MenuItem.objects.get(pk=self.id).items.all()]
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'category': {'title': self.category_id.name},
            'cuisine': {'title': self.cuisine_id.types},
            'restaurants': location
        }


