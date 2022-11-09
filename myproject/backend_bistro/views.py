from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import backend_bistro
# Create your views here.

def get_menu(request):
    bistro_menu = list(backend_bistro.objects.values())

    return JsonResponse ({'data': bistro_menu})
