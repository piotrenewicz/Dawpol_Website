"""dawpol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import static, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .settings import MEDIA_ROOT, MEDIA_URL
from . import settings
from django.views.static import serve

urlpatterns = [
    path('', include('main.urls')),
    path('busy_wynajem/', include('car_hire.urls')),
    path('uslugi/', include('services.urls')),
    path('czesci/', include("car_parts.urls")),
    path('kontakt/', include('contact.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += [ url(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT, }), url(r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_ROOT }), ]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static.static(MEDIA_URL,
document_root=MEDIA_ROOT)