from django.contrib import admin

from .models import MenuItem, Category, Cuisine


admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Cuisine)
# Register your models here.
