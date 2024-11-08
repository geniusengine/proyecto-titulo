"""
URL configuration for Causa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Causa1 import views

urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('Dashboard/', views.dashboard, name='dashboard'),
    path('notificar/<int:causa_id>/', views.notificar, name='notificar'),
   
    path('estampado/<int:estampado_id>/', views.estampado, name='estampado'),
    path('estampado/<int:estampado_id>/descargar/<str:tipo_estampado>/', views.generar_documento, name='generar_documento'),
]
