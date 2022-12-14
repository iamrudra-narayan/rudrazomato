from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [    
    #path("delivery", views.delivery, name="delivery"),
    #path("dining", views.dining, name="dining"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("edit_profile_details/", views.editprofile, name="edit-profile"),
    path("add_profile_details/", views.addprofile, name="add-profile"),
    #path("edit_profile_picture/", views.update_pic, name="edit-profile-picture"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)