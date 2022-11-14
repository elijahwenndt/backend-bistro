from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, MenuItemSerializer, CategorySerializer
from .models import MenuItem, Category



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MenuItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows menu items to be viewed or edited
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows menu items to be viewed or edited
    """
    queryset = Category.objects.prefetch_related('category').all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from .models import MenuItem, RestaurantName
# import json
# # Create your views here.

# # REFERENCE https://www.yellowduck.be/posts/outputting-django-queryset-json
# def get_menu(request):
#     # data = list(MenuItem.objects.values('title', 'description', 'price', 'spice_level', 'category_id__name', 'cuisine_id__types'))
#     # return JsonResponse(data, safe=False)
#     data = [i.json() for i in MenuItem.objects.all()]

#     return HttpResponse(json.dumps(data), content_type="application/json")

# # def get_name(request):

# #     data = [i.json() for i in RestaurantName.objects.all()]

# #     return HttpResponse(json.dumps(data), content_type="application/json")
