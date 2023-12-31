"""
URL configuration for ToDo project.

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
from base.views import home
from base.views import create
from base.views import edit
from base.views import delete
from base.views import delete_all


urlpatterns = [
    path('rajiv_website/', admin.site.urls),
    path("homepage",home,name="home") ,#needed to add new url
    path("create",create, name="create"),
    path("edit/<int:pk>/",edit, name="edit"),#<int:pk>/ this passes the id, value of the row form table
    path("delete/<int:pk>/",delete, name="delete"), 
    path("delete_all/",delete_all, name="delete_all"), 
]

