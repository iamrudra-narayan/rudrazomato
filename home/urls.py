from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [    
    path('', views.home, name="Home"),
    path('search/', views.search, name='search'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)