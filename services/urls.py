from django.urls import path
from . import views


app_name = "services"
urlpatterns = [
    path('', views.service, name='uslugi'),
    # path('details/<int:car_id>', views.detailedview, name='detailed'),
]
