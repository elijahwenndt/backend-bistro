from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import MenuItem, Category, Cuisine, RestaurantName, Ingredients

class RestaurantNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantName
        fields = ['name']

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['description']

class CategorySerializer(serializers.ModelSerializer):
    # items = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['title']
# 'items'
    # def get_items(self, instance):
    #     queryset = MenuItem.objects.filter(category_id__id=instance.id)
    #     return MenuItemSerializer(queryset, many=True).data

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['title']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(source='category_id')
    cuisine = CuisineSerializer(source='cuisine_id')
    restaurant = RestaurantNameSerializer(many=True)
    ingredients = IngredientsSerializer(many=True)
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'description', 'price', 'category', 'cuisine', 'ingredients', 'restaurant']