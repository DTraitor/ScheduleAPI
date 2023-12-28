"""
URL configuration for ScheduleAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from schedule import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/find_groups/', views.search_groups, name='search_groups'),
    path('api/get_group/', views.get_group, name='get_group'),
    path('api/create_group/', views.create_group, name='create_group'),
    path('api/delete_group/', views.delete_group, name='delete_group'),
    path('api/add_lesson/', views.add_lesson, name='add_lesson'),
    path('api/delete_lesson/', views.delete_lesson, name='delete_lesson'),
    path('api/get_lessons/', views.get_lessons_at_date, name='get_lessons'),
]
