from django.contrib import admin

from .models import MenuItem, Category, Cuisine, RestaurantName


admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(RestaurantName)

# Register your models here.
