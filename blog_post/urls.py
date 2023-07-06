"""
URL configuration for blog_post project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from src import views

urlpatterns = [
    path("sign_up", views.sign_up, name="sign_up"),
    path("particular_user/<str:id>", views.get_particular_user, name="particular_user"),
    path("all_users", views.all_users, name="all_user"),
    path("update_user/<str:id>", views.updating_user, name="update_user"),
    path("delete_user/<str:id>", views.deleting_user, name="delete_user"),
    path("login", views.login, name="login"),
    path("admin/", admin.site.urls),
]
