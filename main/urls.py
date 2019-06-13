from django.urls import path
from . import views


app_name = "main"
urlpatterns = [
    path('', views.index, name='index'),
    path('opinie', views.com_list, name='comments'),
    path('AutoParts/', views.parts_gallery, name='parts'),
    path('Wypozycz', views.bus_rental, name='rent'),
    path('TopSecretList/<str:item_manager_name>', views.items_view, name='secret'),
]
