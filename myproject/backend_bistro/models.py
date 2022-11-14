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
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Cuisine(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
# Create your models here.

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(null=True, blank=True)
    spice_level = models.IntegerField(null=True, blank=True)
    category_id = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    cuisine_id = models.ForeignKey(Cuisine, related_name='cuisine', on_delete=models.CASCADE)
    restaurant = models.ManyToManyField(RestaurantName)
    ingredients = models.ManyToManyField(Ingredients)


    def __str__(self):
        return self.title
        
# REFERENCE https://www.yellowduck.be/posts/outputting-django-queryset-json
    # def json(self):
    #     location = [i.name for i in MenuItem.objects.get(pk=self.id).items.all()]
    #     ingredients = [i.description for i in MenuItem.objects.get(pk=self.id).ingredients.all()]
    #     return {
    #         'id': self.id,
    #         'title': self.title,
    #         'description': self.description,
    #         'ingredients': ingredients,
    #         'price': self.price,
    #         'category': {'title': self.category_id.name},
    #         'cuisine': {'title': self.cuisine_id.types},
    #         'restaurants': location
    #     }

