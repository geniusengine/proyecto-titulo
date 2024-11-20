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
    path('crear_demanda/', views.crear_demanda, name='crear_demanda'),
    
    path('estampar/<int:causa_id>/', views.estampar, name='estampar'),
    path('descargar_documento/<int:estampado_id>/<str:tipo_estampado>/', views.descargar_documento, name='descargar_documento'),
    path('dashboard_historico/', views.dashboard_historico, name='dashboard_historico'),
    path('logout/', views.logout_view, name='logout'),
]
