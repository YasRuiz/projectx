from django.db import models

class Mascota(models.Model):
    TIPO_MASCOTA = (
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    )
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=TIPO_MASCOTA)
    descripcion = models.TextField()
    disponible = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='mascotas/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

# Modelo actualizado de Solicitud de Adopción
class SolicitudAdopcion(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='solicitudes')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    motivo = models.TextField(help_text="Explica por qué deseas adoptar a esta mascota")
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    aceptado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.mascota.nombre}"
