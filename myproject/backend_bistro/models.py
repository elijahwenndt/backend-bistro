from django.db import models

class RestaurantName(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Ingredients(models.Model):
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.description

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
    ingredients = models.ManyToManyField(Ingredients)


    def __str__(self):
        return self.title
        
    def json(self):
        location = [i.name for i in MenuItem.objects.get(pk=self.id).items.all()]
        ingredients = [i.description for i in MenuItem.objects.get(pk=self.id).ingredients.all()]
        return {
            'id': self.id,
            'title': self.title,
            'descriptions': self.description,
            'ingredients': ingredients,
            'price': self.price,
            'category': {'title': self.category_id.name},
            'cuisine': {'title': self.cuisine_id.types},
            'restaurants': location
        }


