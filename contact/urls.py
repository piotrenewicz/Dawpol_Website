from django.urls import path
from . import views


app_name = "contact"
urlpatterns = [
    path('', views.info, name='info'),
    path('map', views.map, name='map'),
    path('map/fullscreen', views.full_map, name='fullmap'),
]
