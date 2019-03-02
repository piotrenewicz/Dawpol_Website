from django.urls import path
from . import views


app_name = "main"
urlpatterns = [
    path('', views.index, name='index'),
    path('opinie', views.com_list, name='comments'),
    path('AutoParts/', views.parts_gallery, name='parts')
]
