from django.urls import path
from . import views


app_name = "car_parts"
urlpatterns = [
    path('', views.wip, name='wip'),
    # path('details/<int:car_id>', views.detailedview, name='detailed'),
]
