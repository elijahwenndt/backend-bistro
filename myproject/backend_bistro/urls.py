from django.urls import path

from . import views

urlpatterns = [
    path('bistro/', views.get_menu),
    # path('merica', views.)
]

