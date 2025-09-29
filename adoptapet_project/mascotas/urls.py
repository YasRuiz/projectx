# mascotas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('adopcion/', views.adopcion, name='adopcion'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('adopcion/', views.adopcion, name='adopcion'),
    path('adoptar_modal/', views.adoptar_modal, name='adoptar_modal'),
    path('adoptar/', views.adoptar_modal, name='adoptar_modal'),
]
