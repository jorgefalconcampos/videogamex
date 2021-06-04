from . import views
from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

urlpatterns = [   
    path('', views.base, name='base'),
    path('inicio', views.index, name='index'),
    # path('buscar', views.search, name='search'),
    path('efectivo', views.efectivo, name='efectivo'),
    path('metodosPago', views.metodos_de_pago, name='metodos_pago'),
    path('categorias', views.categorias, name='categorias'),
    path('categorias/<slug:slug>', views.categorias_detalle, name='categorias_detalle'),

    path('productos', views.productos, name='productos'),
    path('tarjeta', views.tarjeta, name='tarjeta'),
    path('usuario/login', views.login, name='login'),
    path('usuario/perfil', views.perfil, name='perfil'),
    path('usuario/ajustes', views.ajustes, name='ajustes'),
    path('usuario/categoria/nueva', views.categoria_nueva, name='categoria_nueva'),
    path('usuario/logout', views.logout, name='logout'),
    path('usuario/dashboard', views.dashboard, name='dashboard'),
]
