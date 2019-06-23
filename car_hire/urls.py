from django.urls import path
from . import views


app_name = "car_hire"
urlpatterns = [
    path('', views.overview, name='overview'),
    path('details/', views.detailedview, name='detailed'),
]
