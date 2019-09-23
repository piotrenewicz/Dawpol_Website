from django.urls import path
from . import views


app_name = "main"
urlpatterns = [
    path('', views.index, name='index'),
    path('e', views.e404, name='not_found'),
    path('AutoParts/', views.parts_gallery, name='parts'),
    path('TopSecretList/<str:item_manager_name>', views.items_view, name='secret'),
]
