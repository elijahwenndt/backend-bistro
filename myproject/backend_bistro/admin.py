from django.contrib import admin

from .models import MenuItem, Category, Cuisine, RestaurantName, RestaurantNameMenuItem


admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(RestaurantName)
admin.site.register(RestaurantNameMenuItem)
# Register your models here.
