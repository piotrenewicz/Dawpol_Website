from django.urls import path
from . import views


app_name = "car_parts"
urlpatterns = [
    path('', views.part, name='czesci'),
    # path('details/<int:car_id>', views.detailedview, name='detailed'),
]
