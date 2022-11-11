from django.contrib import admin

from .models import MenuItem, Category, Cuisine, RestaurantName, Ingredients


admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(RestaurantName)
admin.site.register(Ingredients)

# Register your models here.
