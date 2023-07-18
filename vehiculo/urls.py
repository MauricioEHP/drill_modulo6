from django.urls import path
from .views import indexView, agregarView, registro_view, registro_view2, login_view, listar_vehiculo, logout_view

urlpatterns = [
        path('', indexView, name='index'),
        path('add/', agregarView, name = 'agregar'),
        path('registro/', registro_view, name = "registro"),
        path('registro2/', registro_view2, name = "registro2"),
        path('login/', login_view, name = "login"),
        path('listar/', listar_vehiculo, name = "listar"),
         path('logout/', logout_view, name = "logout"),
]
