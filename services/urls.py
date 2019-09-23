from django.urls import path
from . import views


app_name = "services"
urlpatterns = [
    path('', views.wip, name='wip'),
    # path('details/<int:car_id>', views.detailedview, name='detailed'),
]
