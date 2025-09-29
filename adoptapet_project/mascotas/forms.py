from django import forms
from .models import Mascota
from .models import SolicitudAdopcion

class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'edad', 'tipo', 'descripcion', 'foto']




class SolicitudAdopcionForm(forms.ModelForm):
    class Meta:
        model = SolicitudAdopcion
        fields = ['nombre', 'apellido', 'rut', 'correo', 'telefono', 'motivo']
        widgets = {
            'motivo': forms.Textarea(attrs={'rows':4, 'placeholder':'Escribe por qué quieres adoptar...'}),
            'nombre': forms.TextInput(attrs={'placeholder':'Tu nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder':'Tu apellido'}),
            'rut': forms.TextInput(attrs={'placeholder':'Tu RUT'}),
            'correo': forms.EmailInput(attrs={'placeholder':'Tu email'}),
            'telefono': forms.TextInput(attrs={'placeholder':'Número de contacto'}),
        }
