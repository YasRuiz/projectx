from django.contrib import admin
from .models import Mascota, SolicitudAdopcion

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'edad', 'disponible')
    list_filter = ('tipo', 'disponible')


@admin.register(SolicitudAdopcion)
class SolicitudAdopcionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'rut', 'correo', 'telefono', 'mascota', 'fecha_solicitud')
    list_filter = ('fecha_solicitud', 'mascota')
    search_fields = ('nombre', 'apellido', 'correo', 'rut')
