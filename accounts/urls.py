from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login),
    path("register/", views.register),
    path("logout/", views.logout),
    path("info/", views.get_user_data),
    path("delete/", views.delete_account),
    path("password/", views.change_password),
]
