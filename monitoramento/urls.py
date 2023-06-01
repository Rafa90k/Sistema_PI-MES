from django.urls import path
from . import views

urlpatterns = [
    path('monitoramento/', views.monitoramento, name='monitoramento'),
    path('', views.logout, name='logout'),
    path('monitoramento/maquina/', views.maquina, name='maquina'),       
]