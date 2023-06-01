from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_of/', views.cadastrar_of, name='cadastrar_of'),    
    path('ofs_cadastradas/', views.ofs_cadastradas, name='ofs_cadastradas'),
    path('ofs_cadastradas/editar_of/<int:id>', views.editar_of, name='editar_of'),
    path('ofs_cadastradas/update/<int:id>', views.update, name='update'),
    path('ofs_cadastradas/delete/<int:id>', views.delete, name='delete'),
]