from django.urls import path
from . import views


app_name = "car_hire"
urlpatterns = [
    path('', views.overview, name='overview'),
    path('details/<int:car_id>', views.detailedview, name='detailed'),
]
