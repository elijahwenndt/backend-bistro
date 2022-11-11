from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import MenuItem, RestaurantName
import json
# Create your views here.

def get_menu(request):
    # data = list(MenuItem.objects.values('title', 'description', 'price', 'spice_level', 'category_id__name', 'cuisine_id__types'))
    # return JsonResponse(data, safe=False)
    data = [i.json() for i in MenuItem.objects.all()]

    return HttpResponse(json.dumps(data), content_type="application/json")

# def get_name(request):

#     data = [i.json() for i in RestaurantName.objects.all()]

#     return HttpResponse(json.dumps(data), content_type="application/json")

# REFERENCE https://www.yellowduck.be/posts/outputting-django-queryset-json